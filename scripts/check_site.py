"""Validate local routes/assets/anchors and deployment boundary without dependencies."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/'site'
class Document(HTMLParser):
 def __init__(self):
  super().__init__(); self.refs=[]; self.ids=[]; self.h1=0; self.lang=None; self.title=False; self.description=False
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='html': self.lang=a.get('lang')
  if tag=='h1': self.h1+=1
  if tag=='title': self.title=True
  if tag=='meta' and a.get('name')=='description': self.description=True
  if 'id' in a:self.ids.append(a['id'])
  for k in ('href','src'):
   if k in a:self.refs.append(a[k])
docs={}
for p in SITE.rglob('*.html'):
 d=Document();d.feed(p.read_text());docs[p.resolve()]=d
errors=[]; links=0
for p,d in docs.items():
 if d.h1!=1:errors.append(f'{p.name}: expected one H1, found {d.h1}')
 if d.lang!='en-GB':errors.append(f'{p.name}: missing British English language')
 if not d.title:errors.append(f'{p.name}: missing title')
 if len(d.ids)!=len(set(d.ids)):errors.append(f'{p.name}: duplicate IDs')
 for ref in d.refs:
  u=urlsplit(ref)
  if u.scheme or u.netloc:continue
  links+=1
  if u.path.startswith('/'):errors.append(f'{p.name}: root-relative link incompatible with project subpath: {ref}')
  dest=(p.parent/unquote(u.path)).resolve() if u.path else p
  if not dest.is_relative_to(SITE.resolve()):errors.append(f'{p.name}: link outside public site: {ref}')
  if not dest.exists():errors.append(f'{p.name}: missing target {ref}')
  if u.fragment and dest in docs and u.fragment not in docs[dest].ids:errors.append(f'{p.name}: missing anchor {ref}')
 for forbidden in ('/Users/','/workspace/','7748 395','SLR’s Responsible Finance'):
  if forbidden in p.read_text():errors.append(f'{p.name}: private or application-specific content: {forbidden}')
workflow=(ROOT/'.github/workflows/pages.yml').read_text()
assert 'workflow_dispatch:' in workflow and 'push:' not in workflow
assert "if: inputs.approval == 'APPROVE PUBLICATION'" in workflow
assert 'path: site' in workflow
if errors:raise SystemExit('\n'.join(errors))
print(f'PASS: {len(docs)} HTML documents; {links} local references; unique IDs, headings, language and local targets checked.')
print('PASS: manual-only deployment, explicit approval input, public site directory only.')
