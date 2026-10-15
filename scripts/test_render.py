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
TOOTHFORM_NOTICES = (
    "ACTA_DIRECT_ATTRIBUTION.txt", "ATTRIBUTION.txt", "BERN007_ATTRIBUTION.txt",
    "DENTAL_SCOPE_CREDITS.txt", "DENTAL_SCOPE_LICENSE.txt", "DUNDEE_ATTRIBUTION.txt",
    "KATO2009_ATTRIBUTION.txt", "LIAO2018_ATTRIBUTION.txt", "ODONTOIQ_SOURCE_LICENSE.txt",
    "OPENMANDIBLE_ATTRIBUTION.txt", "RCAP_LAYERED_ATTRIBUTION.txt",
    "RCAP_PREMOLAR_ATTRIBUTION.txt", "SCANNED_ATTRIBUTION.txt", "TOOTHNROLL_ATTRIBUTION.txt",
)


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

    def toothform_sources(self):
        sources = Path(self.temporary.name) / "sources"
        selected = sources / "DentalMorphology"
        models = selected / "DentalMorphology/Resources/Models"
        models.mkdir(parents=True)
        (selected / "SUPPORT.md").write_text("# ToothForm support\n\nRead [Licensing](LICENSES.md).\n")
        (selected / "PRIVACY_POLICY.md").write_text("# ToothForm privacy\n\nOffline atlas.\n")
        rows = "\n".join(
            f"| [{name}](DentalMorphology/Resources/Models/{name}) | See notice |"
            for name in TOOTHFORM_NOTICES
        )
        (selected / "LICENSES.md").write_text(
            "# ToothForm licensing\n\n| Source | Terms |\n|---|---|\n" + rows + "\n\n"
            "Read [Licensing](LICENSES.md), [private](STATUS.md), "
            "[extra](DentalMorphology/Resources/Models/SECRET.txt), "
            "[mesh](DentalMorphology/Resources/Models/tooth.stl), "
            "and [upstream](https://example.com/license).\n"
        )
        for number, name in enumerate(TOOTHFORM_NOTICES):
            (models / name).write_bytes(
                f'Notice {number}: {name}\r\n<script>alert("unsafe")</script> & ©\r\n'.encode()
            )
        (models / "SECRET.txt").write_text("DO_NOT_PUBLISH_MODEL_SENTINEL")
        (models / "tooth.stl").write_bytes(b"DO_NOT_PUBLISH_MODEL_SENTINEL\x00\xff")
        (models / "private").mkdir()
        (models / "private/ATTRIBUTION.txt").write_text("DO_NOT_PUBLISH_MODEL_SENTINEL")
        (selected / "STATUS.md").write_text("DO_NOT_PUBLISH_MODEL_SENTINEL")
        return sources, selected, models

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

    def test_public_support_renders_tables_without_private_links(self):
        guide = self.site / "dentalmorphology/SUPPORT.md"
        guide.write_text(
            "# Controls\n\n| Platform | Move |\n|---|---|\n| Mac | Drag <safely> |\n\n"
            "Read [privacy](PRIVACY_POLICY.md), [internal status](../STATUS.md), "
            "and [model notes](../Tools/README.md).\n"
        )
        self.render()
        html = (self.site / "dentalmorphology/index.html").read_text()
        self.assertIn('<th scope="col">Platform</th>', html)
        self.assertIn('<td>Drag &lt;safely&gt;</td>', html)
        self.assertIn('<a href="privacy.html">privacy</a>, internal status, and model notes.', html)
        self.assertNotIn('../STATUS.md', html)
        self.assertNotIn('../Tools/README.md', html)

    def test_prototype_refresh_copies_only_public_documents(self):
        sources = Path(self.temporary.name) / "sources"
        selected = sources / "PhoneResponder"
        selected.mkdir(parents=True)
        (selected / "SUPPORT.md").write_text("# Foundry Call Studio support\n\nFictional practice only.\n")
        (selected / "PRIVACY_POLICY.md").write_text("# Foundry Call Studio privacy\n\nProvider processing.\n")
        (selected / "clinic.json").write_text('{"private":"DO_NOT_PUBLISH_SENTINEL"}')
        (selected / "STATUS.md").write_text("DO_NOT_PUBLISH_SENTINEL")
        (selected / "README.md").write_text("DO_NOT_PUBLISH_SENTINEL")
        self.render("--source-root", str(sources), "--app", "foundrycallstudio")
        self.assertEqual(
            {p.name for p in (self.site / "foundrycallstudio").iterdir()},
            {"SUPPORT.md", "PRIVACY_POLICY.md", "index.html", "privacy.html"},
        )
        for page in self.site.rglob("*.html"):
            self.assertNotIn("DO_NOT_PUBLISH_SENTINEL", page.read_text(), str(page))
        self.assertIn("Foundry Call Studio (local prototype)", (self.site / "index.html").read_text())
        self.assertIn("ToothForm: Dental Anatomy 3D", (self.site / "index.html").read_text())

    def test_toothform_refresh_exports_exact_notices_and_preserves_bytes(self):
        sources, selected, models = self.toothform_sources()
        retained = {
            str(p.relative_to(self.site)): p.read_bytes()
            for p in self.site.rglob("*")
            if p.is_file() and p.suffix in (".html", ".md")
            and len(p.relative_to(self.site).parts) > 1
            and p.relative_to(self.site).parts[0] not in ("dentalmorphology", "scripts")
        }
        self.render("--source-root", str(sources), "--app", "dentalmorphology")
        dest = self.site / "dentalmorphology"
        self.assertEqual((dest / "LICENSES.md").read_bytes(), (selected / "LICENSES.md").read_bytes())
        self.assertEqual(
            {p.name for p in (dest / "model-notices").iterdir()},
            set(TOOTHFORM_NOTICES) | {Path(name).stem + ".html" for name in TOOTHFORM_NOTICES},
        )
        manifest = json.loads((self.site / "source-sha256.json").read_text())
        expected = {"dentalmorphology/LICENSES.md"} | {
            "dentalmorphology/model-notices/" + name for name in TOOTHFORM_NOTICES
        }
        self.assertEqual(
            {key for key in manifest if key.startswith("dentalmorphology/")},
            expected | {"dentalmorphology/SUPPORT.md", "dentalmorphology/PRIVACY_POLICY.md"},
        )
        for name in TOOTHFORM_NOTICES:
            content = (models / name).read_bytes()
            self.assertEqual((dest / "model-notices" / name).read_bytes(), content)
            self.assertEqual(manifest["dentalmorphology/model-notices/" + name], hashlib.sha256(content).hexdigest())
            html = (dest / "model-notices" / (Path(name).stem + ".html")).read_text()
            self.assertIn('&lt;script&gt;alert(&quot;unsafe&quot;)&lt;/script&gt; &amp; ©', html)
            self.assertNotIn('<script>', html)
            self.assertIn(f'href="{name}"', html)
            self.assertIn('white-space:pre-wrap', html)
            self.assertIn('href="../licenses.html"', html)
            if name in ("ATTRIBUTION.txt", "DUNDEE_ATTRIBUTION.txt", "KATO2009_ATTRIBUTION.txt"):
                self.assertIn("Historical ", html)
                self.assertIn("current ToothForm app package", html)
            elif name == "DENTAL_SCOPE_CREDITS.txt":
                self.assertIn("not a dependency inventory for ToothForm", html)
            elif name == "DENTAL_SCOPE_LICENSE.txt":
                self.assertIn("MIT license covers the Dental Scope software", html)
                self.assertIn("does not license ToothForm&#x27;s original application code", html)
            else:
                self.assertIn("Current source-family notice.", html)
        for page in dest.rglob("*"):
            if page.is_file():
                self.assertNotIn(b"DO_NOT_PUBLISH_MODEL_SENTINEL", page.read_bytes(), str(page))
        for relative, content in retained.items():
            self.assertEqual((self.site / relative).read_bytes(), content, relative)

    def test_toothform_bundled_render_preserves_links_and_scopes_styles(self):
        sources, _, _ = self.toothform_sources()
        other = self.site / "cbct/SUPPORT.md"
        other.write_text("# Support\n\nRead [private license](LICENSES.md).\n")
        self.render("--source-root", str(sources), "--app", "dentalmorphology")
        first = {
            str(p.relative_to(self.site)): p.read_bytes()
            for p in self.site.rglob("*")
            if p.is_file() and p.suffix in (".html", ".md", ".txt", ".json")
        }
        shutil.rmtree(sources)
        self.render()
        for relative, content in first.items():
            self.assertEqual((self.site / relative).read_bytes(), content, relative)
        licensing = (self.site / "dentalmorphology/licenses.html").read_text()
        self.assertIn('aria-label="Tooth model sources and license status"', licensing)
        self.assertNotIn('aria-label="Controls by platform"', licensing)
        self.assertIn('<a href="licenses.html">Licensing</a>, private, extra, mesh,', licensing)
        self.assertIn('<a href="https://example.com/license">upstream</a>', licensing)
        self.assertNotIn('white-space:pre-wrap', licensing)
        for name in TOOTHFORM_NOTICES:
            self.assertIn(f'href="model-notices/{Path(name).stem}.html"', licensing)
        for filename in ("index.html", "privacy.html"):
            html = (self.site / "dentalmorphology" / filename).read_text()
            self.assertIn('href="licenses.html">Licensing</a>', html)
            self.assertNotIn('white-space:pre-wrap', html)
        self.assertIn('Read private license.', (self.site / "cbct/index.html").read_text())
        self.assertNotIn('>Licensing</a>', (self.site / "cbct/index.html").read_text())
        for page in (self.site / "dentalmorphology").rglob("*.html"):
            parser = Links()
            parser.feed(page.read_text())
            for href in parser.hrefs:
                parsed = urlsplit(href)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                target = page.parent / unquote(parsed.path)
                if target.is_dir():
                    target /= "index.html"
                self.assertTrue(target.is_file(), f"{page.name}: broken link {href}")

    def test_toothform_refresh_requires_complete_allowlist(self):
        sources, _, models = self.toothform_sources()
        (models / TOOTHFORM_NOTICES[-1]).unlink()
        before = {
            str(p.relative_to(self.site / "dentalmorphology")): p.read_bytes()
            for p in (self.site / "dentalmorphology").rglob("*") if p.is_file()
        }
        with self.assertRaises(subprocess.CalledProcessError):
            self.render("--source-root", str(sources), "--app", "dentalmorphology")
        after = {
            str(p.relative_to(self.site / "dentalmorphology")): p.read_bytes()
            for p in (self.site / "dentalmorphology").rglob("*") if p.is_file()
        }
        self.assertEqual(after, before)


if __name__ == "__main__":
    unittest.main()
