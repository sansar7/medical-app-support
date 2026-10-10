"""Check selective publication, public links, and wrapped workflow lists."""
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.hrefs.extend(value for key, value in attrs if key == "href")


class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.site = Path(self.temporary.name) / "site"
        shutil.copytree(ROOT, self.site, ignore=shutil.ignore_patterns(".git", "__pycache__"))

    def render(self, *args):
        return subprocess.run(
            [sys.executable, str(self.site / "scripts/render.py"), *args],
            check=True, capture_output=True, text=True,
        )

    def test_selective_refresh_preserves_other_sources_and_manifest(self):
        sources = Path(self.temporary.name) / "sources"
        selected = sources / "EasySTL"
        selected.mkdir(parents=True)
        (selected / "SUPPORT.md").write_text("# Updated help\n\nNew instructions.\n")
        (selected / "PRIVACY_POLICY.md").write_text("# Updated privacy\n\nLocal processing.\n")
        retained = {
            str(p.relative_to(self.site)): p.read_bytes()
            for p in self.site.glob("*/*.md") if p.parent.name != "easy3d"
        }
        self.render("--source-root", str(sources), "--app", "easy3d")
        for relative, content in retained.items():
            self.assertEqual((self.site / relative).read_bytes(), content, relative)
        manifest = json.loads((self.site / "source-sha256.json").read_text())
        for relative, expected in manifest.items():
            self.assertEqual(hashlib.sha256((self.site / relative).read_bytes()).hexdigest(), expected)
        self.assertEqual((self.site / "easy3d/SUPPORT.md").read_bytes(), (selected / "SUPPORT.md").read_bytes())

    def test_render_is_deterministic_and_all_local_links_resolve(self):
        self.render()
        first = {str(p.relative_to(self.site)): p.read_bytes() for p in self.site.rglob("*.html")}
        self.render()
        for relative, content in first.items():
            page = self.site / relative
            self.assertEqual(page.read_bytes(), content, relative)
            parser = Links()
            parser.feed(content.decode())
            for href in parser.hrefs:
                parsed = urlsplit(href)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                target = page.parent / unquote(parsed.path)
                if target.is_dir():
                    target /= "index.html"
                self.assertTrue(target.is_file(), f"{relative}: broken link {href}")

    def test_wrapped_workflow_list_keeps_items_together(self):
        guide = self.site / "cbct/ENDODONTICS.md"
        guide.write_text("# Workflow\n\n1. First step with\n   continued guidance.\n2. Second step.\n\n- One warning with\n  a continuation.\n- Another warning.\n")
        self.render()
        html = (self.site / "cbct/endodontics.html").read_text()
        self.assertIn("<ol><li>First step with continued guidance.</li><li>Second step.</li></ol>", html)
        self.assertIn("<ul><li>One warning with a continuation.</li><li>Another warning.</li></ul>", html)


if __name__ == "__main__":
    unittest.main()
