#!/usr/bin/env python3
"""Render the public support pages from their bundled Markdown or canonical app docs."""
from pathlib import Path
import argparse
from html import escape
import re, shutil, hashlib, json
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--source-root', type=Path, help='Optional parent directory containing the app repositories')
parser.add_argument('--app', action='append', choices=['cbct', 'easy3d', 'denthesia', 'enamel', 'dentalfacescan', 'denthesia-web', 'dentalmorphology', 'foundrycallstudio'], help='Refresh only this app from --source-root; repeat for several apps. Other bundled documents are retained.')
args = parser.parse_args()
if args.app and not args.source_root:
 parser.error('--app requires --source-root')
base = args.source_root
output = Path(__file__).resolve().parents[1]
apps=[('cbct','Dental CBCT Studio','CBCTApp'),('easy3d','Dental 3D','EasySTL'),('denthesia','Denthesia','DosageCalculatorApp/DentalDosage'),('enamel','Enamel','DentalEducation'),('dentalfacescan','Easy3D Capture','FacialScanner'),('denthesia-web','Denthesia website','DosageCalculatorWebsite'),('dentalmorphology','ToothForm: Dental Anatomy 3D','DentalMorphology'),('foundrycallstudio','Foundry Call Studio (local prototype)','PhoneResponder')]
toothform_notices = (
 'ACTA_DIRECT_ATTRIBUTION.txt', 'ATTRIBUTION.txt', 'BERN007_ATTRIBUTION.txt',
 'DENTAL_SCOPE_CREDITS.txt', 'DENTAL_SCOPE_LICENSE.txt', 'DUNDEE_ATTRIBUTION.txt',
 'KATO2009_ATTRIBUTION.txt', 'LIAO2018_ATTRIBUTION.txt', 'ODONTOIQ_SOURCE_LICENSE.txt',
 'OPENMANDIBLE_ATTRIBUTION.txt', 'RCAP_LAYERED_ATTRIBUTION.txt',
 'RCAP_PREMOLAR_ATTRIBUTION.txt', 'SCANNED_ATTRIBUTION.txt', 'TOOTHNROLL_ATTRIBUTION.txt',
)
toothform_notice_context = {
 'ATTRIBUTION.txt': 'Historical geometry notice. BodyParts3D / Dental Scope geometry is a retired development family and is not in the current ToothForm app package. This notice describes those separately licensed adapted assets.',
 'DUNDEE_ATTRIBUTION.txt': 'Historical surface-model notice. The current ToothForm app package contains no Dundee geometry; these surfaces remain local fallback and development resources.',
 'DENTAL_SCOPE_CREDITS.txt': 'Retained upstream credits. This is historical Dental Scope documentation, not a dependency inventory for ToothForm. It describes the upstream project, whose geometry and runtime differ from the current ToothForm app.',
 'DENTAL_SCOPE_LICENSE.txt': 'Upstream software license. This MIT license covers the Dental Scope software described below. It does not license ToothForm\'s original application code or the separately licensed tooth geometry.',
}
style='''*{box-sizing:border-box}body{margin:0;background:#f6faf9;color:#183630;font:17px/1.7 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}main{max-width:800px;margin:auto;padding:40px 24px 72px}h1{font-size:2.25rem;line-height:1.15;color:#075e58}h2{font-size:1.3rem;margin-top:2rem}nav{display:flex;flex-wrap:wrap;gap:20px;font-size:15px}a{color:#254caf;overflow-wrap:anywhere}a:focus-visible{outline:3px solid #0b796f;outline-offset:4px}p,li{max-width:72ch}code{font-size:.92em}footer{margin-top:40px;border-top:1px solid #c7d8d3;padding-top:18px;font-size:14px}li{margin:8px 0}@media(prefers-color-scheme:dark){body{background:#10231f;color:#e2f0eb}h1{color:#88d7c8}a{color:#a4bfff}footer{border-color:#3a5149}}'''
table_style = '.table-scroll{overflow-x:auto;margin:1.5rem 0}table{width:100%;border-collapse:collapse;font-size:.95em}th,td{border:1px solid #8ba9a1;padding:10px 12px;text-align:left;vertical-align:top}th{font-weight:600}td:first-child{min-width:8rem}'
notice_style = '.source-notice{white-space:pre-wrap;overflow-wrap:anywhere;font:14px/1.6 ui-monospace,SFMono-Regular,Menlo,monospace}'

def public_link(match, app=None):
 label, target = match[1], match[2]
 routes = {'PRIVACY_POLICY.md':'privacy.html', 'PRIVACY.md':'privacy.html', 'SUPPORT.md':'./', 'LOCALIZATION.md':'../languages.html', 'docs/LANGUAGES.md':'../languages.html', 'docs/LOCALIZATION.md':'../languages.html', 'Docs/LOCALIZATION.md':'../languages.html', 'docs/ENDODONTICS.md':'endodontics.html'}
 if app == 'dentalmorphology':
  routes['LICENSES.md'] = 'licenses.html'
  routes.update({f'DentalMorphology/Resources/Models/{name}':f'model-notices/{Path(name).stem}.html' for name in toothform_notices})
 if target in routes:
  target = routes[target]
 elif not re.match(r'(?:https?://|mailto:|#)', target):
  # Internal source notes and audit records are not public support pages.
  return label
 return f'<a href="{target}">{label}</a>'

def inline(s, app=None):
 s=escape(s)
 s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',lambda match: public_link(match, app),s)
 s=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',s)
 s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s)
 s=re.sub(r'(?<!["=>])(https://[^\s<)]+)',r'<a href="\1">\1</a>',s)
 # Existing Markdown mail links retain their own labels.
 s=re.sub(r'(?<![\w:"/>])([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})(?![\w"<])',r'<a href="mailto:\1">\1</a>',s)
 return s

def markdown(s, app=None, table_label='Controls by platform'):
 chunks=[]
 for block in re.split(r'\n\s*\n',s.strip()):
  if block.startswith('For release, host this support content'):continue
  if block.startswith('# '):chunks.append('<h1>'+inline(block[2:], app)+'</h1>')
  elif block.startswith('## '):chunks.append('<h2>'+inline(block[3:], app)+'</h2>')
  elif block.startswith('|') and len(block.splitlines()) >= 2 and re.fullmatch(r'\s*\|?[\s:|\-]+\|?\s*', block.splitlines()[1]):
   rows = [[cell.strip() for cell in line.strip().strip('|').split('|')] for line in block.splitlines()]
   header = '<thead><tr>'+''.join('<th scope="col">'+inline(cell, app)+'</th>' for cell in rows[0])+'</tr></thead>'
   body = '<tbody>'+''.join('<tr>'+''.join('<td>'+inline(cell, app)+'</td>' for cell in row)+'</tr>' for row in rows[2:])+'</tbody>'
   chunks.append('<div class="table-scroll" tabindex="0" role="region" aria-label="'+escape(table_label, quote=True)+'"><table>'+header+body+'</table></div>')
  elif re.match(r'(?:[-*] |\d+\. )', block):
   ordered = bool(re.match(r'\d+\. ', block))
   pattern = r'^\d+\.\s+' if ordered else r'^[-*]\s+'
   items=[]
   for line in block.splitlines():
    if re.match(pattern, line):items.append(re.sub(pattern, '', line))
    elif items:items[-1]+=' '+line.strip()
   tag='ol' if ordered else 'ul'
   chunks.append('<'+tag+'>'+''.join('<li>'+inline(item, app)+'</li>' for item in items)+'</'+tag+'>')
  else:chunks.append('<p>'+inline(' '.join(block.splitlines()), app)+'</p>')
 return '\n'.join(chunks)

def page(title,body,nav,extra_style=''):
 page_style = style + (table_style if '<table>' in body else '') + extra_style
 return f'<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="referrer" content="no-referrer"><title>{escape(title)}</title><style>{page_style}</style></head><body><main><nav aria-label="Site">{nav}</nav>{body}<footer>App support from Sansar Gupta. Contact <a href="mailto:sansargupta10@gmail.com">sansargupta10@gmail.com</a>. Please do not send patient information.</footer></main></body></html>\n'
manifest={}
for slug,name,repo in apps:
 dest=output/slug;dest.mkdir(exist_ok=True)
 nav='<a href="../">All apps</a><a href="./">Support</a><a href="privacy.html">Privacy policy</a><a href="../languages.html">Languages</a>'
 refresh = base and (not args.app or slug in args.app)
 licensing_source = (base/repo/'LICENSES.md') if refresh else dest/'LICENSES.md'
 has_licensing = slug == 'dentalmorphology' and (refresh or licensing_source.exists())
 if has_licensing:
  notice_sources = {notice: (base/repo/'DentalMorphology/Resources/Models'/notice) if refresh else dest/'model-notices'/notice for notice in toothform_notices}
  # Read the complete explicit publication set before writing any licensing output.
  licensing_bytes = licensing_source.read_bytes()
  notice_bytes = {notice: source.read_bytes() for notice,source in notice_sources.items()}
  licensing_text = licensing_bytes.decode('utf-8')
  notice_text = {notice: content.decode('utf-8') for notice,content in notice_bytes.items()}
  nav += '<a href="licenses.html">Licensing</a>'
 for source,filename in [('PRIVACY_POLICY.md','privacy.html'),('SUPPORT.md','index.html')]:
  canonical_source='PRIVACY.md' if slug=='enamel' and source=='PRIVACY_POLICY.md' else source
  p=(base/repo/canonical_source) if base and (not args.app or slug in args.app) else (dest/source);text=p.read_text();manifest[slug+'/'+source]=hashlib.sha256(p.read_bytes()).hexdigest()
  (dest/source).write_text(text)
  body=markdown(text.split('## Publisher preparation')[0].replace('Unsupported formats and limits are described in [README.md](README.md).', 'See the in-app Help for supported formats and import limits.'), slug)
  if source=='SUPPORT.md' and slug in ('easy3d','cbct'):
   sample='Dental-3D-Demo.stl' if slug=='easy3d' else 'CBCT-Synthetic-Review.zip'
   helptext='Open the STL file in Dental 3D.' if slug=='easy3d' else 'Unzip the archive, then use Open CBCT Study / Choose DICOM File or Folder and choose CBCT-Release-Synthetic.'
   body+=f'<h2>Fictional review sample</h2><p><a href="../samples/{sample}">Download the synthetic sample</a>. {helptext} It contains only computer-generated geometry, with no patient data. It is for demonstrating the software and does not validate clinical accuracy.</p>'
  (dest/filename).write_text(page(name+' — '+('Privacy' if source.startswith('PRIVACY') else 'Support'),body,nav))
 if has_licensing:
  (dest/'LICENSES.md').write_bytes(licensing_bytes)
  manifest[slug+'/LICENSES.md'] = hashlib.sha256(licensing_bytes).hexdigest()
  (dest/'licenses.html').write_text(page(name+' — Licensing', markdown(licensing_text, slug, 'Tooth model sources and license status'), nav))
  notices_dest = dest/'model-notices';notices_dest.mkdir(exist_ok=True)
  notice_nav='<a href="../../">All apps</a><a href="../">Support</a><a href="../privacy.html">Privacy policy</a><a href="../licenses.html">Licensing</a><a href="../../languages.html">Languages</a>'
  for notice in toothform_notices:
   (notices_dest/notice).write_bytes(notice_bytes[notice])
   manifest[slug+'/model-notices/'+notice] = hashlib.sha256(notice_bytes[notice]).hexdigest()
   context = toothform_notice_context.get(notice, 'Current source-family notice. This copy retains the bundled attribution, processing and reuse information. The licensing overview describes current positions and unresolved distribution permissions.')
   body='<h1>'+escape(Path(notice).stem.replace('_', ' '))+'</h1><p>'+escape(context)+'</p><p><a href="'+notice+'">Download raw notice (.txt)</a></p><pre class="source-notice">'+escape(notice_text[notice])+'</pre>'
   (notices_dest/(Path(notice).stem+'.html')).write_text(page(name+' — '+Path(notice).stem, body, notice_nav, notice_style))
# Publish the Endo workflow linked from CBCT support alongside the canonical copy.
endo_source = (base/'CBCTApp/docs/ENDODONTICS.md') if base and (not args.app or 'cbct' in args.app) else output/'cbct/ENDODONTICS.md'
if endo_source.exists():
 endo_text = endo_source.read_text()
 (output/'cbct/ENDODONTICS.md').write_text(endo_text)
 manifest['cbct/ENDODONTICS.md'] = hashlib.sha256(endo_source.read_bytes()).hexdigest()
 (output/'cbct/endodontics.html').write_text(page('Dental CBCT Studio — Endo workflow', markdown(endo_text), '<a href="../">All apps</a><a href="./">CBCT support</a><a href="privacy.html">Privacy policy</a>'))
body='<h1>Dental app support</h1><p>Privacy policies, help, and contact information for apps by Sansar Gupta.</p><ul>'+''.join(f'<li><a href="{slug}/">{name} support</a> · <a href="{slug}/privacy.html">Privacy policy</a></li>' for slug,name,_ in apps)+'</ul><p>For urgent clinical needs, use your established clinical protocols and local emergency services. This site provides software support.</p>'
body += '<p><a href="languages.html">Language support across the apps and website</a></p>'
(output/'index.html').write_text(page('Dental app support',body,''))
language_body = '''<h1>Language support</h1><p>The updated source for Dental CBCT Studio, Dental 3D, Denthesia, Enamel, Easy3D Capture, and the Denthesia website shares 15 interface languages: English, Spanish, French, German, Italian, Brazilian Portuguese, Simplified Chinese, Traditional Chinese, Japanese, Korean, Hindi, Arabic, Indonesian, Turkish, and Vietnamese. Russian is removed from this set.</p><p>Language support is available in builds containing the new language resources. Older App Store installations can have earlier coverage. Publishing source and support documents does not update an installed app or establish an App Store release.</p><p>ToothForm: Dental Anatomy 3D and the local Foundry Call Studio prototype are currently available in English only. Foundry Call Studio is for fictional practice calls and is not connected to clinic phones or patient records.</p><h2>Changing language</h2><p>Native apps follow the operating system's supported-language preferences and per-app language setting when available. The website follows the browser's ordered language preferences. Reopen the app or browser when needed. There is no separate translation button. Unsupported preferences try the next supported language, then English.</p><h2>Coverage and offline use</h2><p>Core controls are bundled. Enamel and native Denthesia may use Apple's on-device Translation framework only for a small allowlist of public nonclinical interface text on supported systems; Apple can request a language-model download. Clinical text needs a bundled reviewed translation or remains in English, and unreviewed older clinical translation caches are ignored. Availability varies by platform and language pair. Other native apps and the website use bundled resources. Some instructions and clinical reference passages deliberately remain in English when a reliable reviewed translation is unavailable.</p><h2>Privacy and accuracy</h2><p>Language changes do not translate patient names, private notes, custom templates, filenames, scan data, geometry, or stored records. Numeric values, units, clinical calculations, stable identifiers, and original references remain protected. Translation review and layout tests do not establish independent clinical validation. Follow each app's privacy policy for storage and optional system services.</p><h2>Reporting a translation issue</h2><p>Include the app version, device, operating system or browser, selected language and region, screen name, and the original app-authored wording. A redacted screenshot can help. Do not send patient information, private notes, clinical images, or scan files through ordinary support email.</p>'''
language_body = language_body.replace('<h2>Privacy and accuracy</h2>', '<h2>English and translation accuracy</h2><p>English is the primary language of these apps. Translations into other languages may be inaccurate; each app provides a language notice. Easy3D Capture capture and export instructions and some medication or education passages can intentionally remain in English while specialist review is pending. A bundled language does not mean every passage is translated or independently certified.</p><h2>Privacy and accuracy</h2>')
(output/'languages.html').write_text(page('Dental apps — Language support', language_body, '<a href="./">All apps</a>'))
(output/'.nojekyll').write_text('')
(output/'source-sha256.json').write_text(json.dumps(manifest,indent=2)+'\n')
(output/'README.md').write_text('# Medical app support\n\nPublic privacy policies, support pages, and entirely synthetic review samples for Dental CBCT Studio, Dental 3D, Denthesia, Enamel, Easy3D Capture, ToothForm: Dental Anatomy 3D, the Denthesia website, and the local Foundry Call Studio prototype. ToothForm and Foundry Call Studio are English only. The multilingual products share English, Spanish, French, German, Italian, Brazilian Portuguese, Simplified and Traditional Chinese, Japanese, Korean, Hindi, Arabic, Indonesian, Turkish, and Vietnamese. These public support documents remain in English. No application source, patient data, credentials, or analytics scripts are included.\n\nHosted by GitHub Pages from main at the repository root. Update the per-app Markdown and run `python3 scripts/render.py` to regenerate HTML together when practices change. To refresh from the app repositories, use `python3 scripts/render.py --source-root /path/to/repositories`. To refresh only selected apps, repeat `--app`, for example `--source-root /path/to/repositories --app cbct --app dentalfacescan --app dentalmorphology --app foundrycallstudio`; other apps keep their bundled documents. The linked CBCT Endo workflow is published with its support page. Only explicitly selected public documents are copied: support/privacy documents, the CBCT Endo workflow, and ToothForm’s LICENSES.md with an explicit allowlist of 14 model attribution/license .txt notices. ToothForm notice pages retain unchanged plain-text copies and provide readable HTML; historical upstream notices are labeled separately from current sources. Tooth geometry, scan volumes, application source, internal status records and clinic configuration are never published. Links to internal Markdown records are rendered as plain text in the public HTML. `source-sha256.json` records the source document checksums at publication. Enamel uses `DentalEducation/PRIVACY.md` as the canonical source of its bundled `enamel/PRIVACY_POLICY.md` copy.\n\nContact: sansargupta10@gmail.com\n')
print(f'Rendered {len(apps)} privacy pages, {len(apps)} support pages and app index.')
