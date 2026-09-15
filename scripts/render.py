#!/usr/bin/env python3
"""Render the public support pages from their bundled Markdown or canonical app docs."""
from pathlib import Path
import argparse
from html import escape
import re, shutil, hashlib, json
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--source-root', type=Path, help='Optional parent directory containing the app repositories')
args = parser.parse_args()
base = args.source_root
output = Path(__file__).resolve().parents[1]
apps=[('cbct','Dental CBCT Studio','CBCTApp'),('easy3d','Dental 3D','EasySTL'),('casebook','Casebook','DentalCaseTracker'),('denthesia','Denthesia','DosageCalculatorApp/DentalDosage'),('enamel','Enamel','DentalEducation')]
style='''*{box-sizing:border-box}body{margin:0;background:#f6faf9;color:#183630;font:17px/1.7 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}main{max-width:800px;margin:auto;padding:40px 24px 72px}h1{font-size:2.25rem;line-height:1.15;color:#075e58}h2{font-size:1.3rem;margin-top:2rem}nav{display:flex;flex-wrap:wrap;gap:20px;font-size:15px}a{color:#254caf;overflow-wrap:anywhere}a:focus-visible{outline:3px solid #0b796f;outline-offset:4px}p,li{max-width:72ch}code{font-size:.92em}footer{margin-top:40px;border-top:1px solid #c7d8d3;padding-top:18px;font-size:14px}li{margin:8px 0}@media(prefers-color-scheme:dark){body{background:#10231f;color:#e2f0eb}h1{color:#88d7c8}a{color:#a4bfff}footer{border-color:#3a5149}}'''
def inline(s):
 s=escape(s)
 s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',lambda m:f'<a href="{m[2] if m[2] not in ("PRIVACY_POLICY.md", "PRIVACY.md") else "privacy.html"}">{m[1]}</a>',s)
 s=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',s)
 s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s)
 s=re.sub(r'(?<!["=>])(https://[^\s<)]+)',r'<a href="\1">\1</a>',s)
 # Existing Markdown mail links retain their own labels.
 s=re.sub(r'(?<![\w:"/>])([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})(?![\w"<])',r'<a href="mailto:\1">\1</a>',s)
 return s

def markdown(s):
 chunks=[]
 for block in re.split(r'\n\s*\n',s.strip()):
  if block.startswith('For release, host this support content'):continue
  if block.startswith('# '):chunks.append('<h1>'+inline(block[2:])+'</h1>')
  elif block.startswith('## '):chunks.append('<h2>'+inline(block[3:])+'</h2>')
  elif block.startswith(('- ','* ')):chunks.append('<ul>'+''.join('<li>'+inline(x[2:])+'</li>' for x in block.splitlines())+'</ul>')
  else:chunks.append('<p>'+inline(' '.join(block.splitlines()))+'</p>')
 return '\n'.join(chunks)

def page(title,body,nav):
 return f'<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="referrer" content="no-referrer"><title>{escape(title)}</title><style>{style}</style></head><body><main><nav aria-label="Site">{nav}</nav>{body}<footer>App support from Sansar Gupta. Contact <a href="mailto:sansargupta10@gmail.com">sansargupta10@gmail.com</a>. Please do not send patient information.</footer></main></body></html>\n'
manifest={}
for slug,name,repo in apps:
 dest=output/slug;dest.mkdir(exist_ok=True)
 nav='<a href="../">All apps</a><a href="./">Support</a><a href="privacy.html">Privacy policy</a>'
 for source,filename in [('PRIVACY_POLICY.md','privacy.html'),('SUPPORT.md','index.html')]:
  canonical_source='PRIVACY.md' if slug=='enamel' and source=='PRIVACY_POLICY.md' else source
  p=(base/repo/canonical_source) if base else (dest/source);text=p.read_text();manifest[slug+'/'+source]=hashlib.sha256(p.read_bytes()).hexdigest()
  (dest/source).write_text(text)
  body=markdown(text.split('## Publisher preparation')[0].replace('Unsupported formats and limits are described in [README.md](README.md).', 'See the in-app Help for supported formats and import limits.'))
  if source=='SUPPORT.md' and slug in ('easy3d','cbct'):
   sample='Dental-3D-Demo.stl' if slug=='easy3d' else 'CBCT-Synthetic-Review.zip'
   helptext='Open the STL file in Dental 3D.' if slug=='easy3d' else 'Unzip the archive, then use Open CBCT Folder and choose CBCT-Release-Synthetic.'
   body+=f'<h2>Fictional review sample</h2><p><a href="../samples/{sample}">Download the synthetic sample</a>. {helptext} It contains only computer-generated geometry, with no patient data. It is for demonstrating the software and does not validate clinical accuracy.</p>'
  (dest/filename).write_text(page(name+' — '+('Privacy' if source.startswith('PRIVACY') else 'Support'),body,nav))
body='<h1>Dental app support</h1><p>Privacy policies, help, and contact information for apps by Sansar Gupta.</p><ul>'+''.join(f'<li><a href="{slug}/">{name} support</a> · <a href="{slug}/privacy.html">Privacy policy</a></li>' for slug,name,_ in apps)+'</ul><p>For urgent clinical needs, use your established clinical protocols and local emergency services. This site provides software support.</p>'
(output/'index.html').write_text(page('Dental app support',body,''))
(output/'.nojekyll').write_text('')
(output/'source-sha256.json').write_text(json.dumps(manifest,indent=2)+'\n')
(output/'README.md').write_text('# Medical app support\n\nPublic privacy policies, support pages, and entirely synthetic review samples for Dental CBCT Studio, Dental 3D, Casebook, Denthesia, and Enamel. No application source, patient data, credentials, or analytics scripts are included.\n\nHosted by GitHub Pages from main at the repository root. Update the per-app Markdown and run `python3 scripts/render.py` to regenerate HTML together when practices change. To refresh from the app repositories, use `python3 scripts/render.py --source-root /path/to/repositories`. The source directory is never published. `source-sha256.json` records the source document checksums at publication. Enamel uses `DentalEducation/PRIVACY.md` as the canonical source of its bundled `enamel/PRIVACY_POLICY.md` copy.\n\nContact: sansargupta10@gmail.com\n')
print(f'Rendered {len(apps)} privacy pages, {len(apps)} support pages and app index.')
