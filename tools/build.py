"""Build Moryarti Sans LTD from sources/MoryartiSansLTD.glyphs, without touching outlines.
python3 tools/build.py   ->  fonts/ttf/, fonts/webfonts/"""
import copy, os, subprocess, sys, shutil, tempfile
from glyphsLib import GSFont
from fontTools.ttLib import TTFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = 'https://github.com/kentree3/moryarti-sans-ltd'
YEAR = 2026
NOEXPORT = ['newGlyph']                      # a working glyph in the source: kept there, not shipped

def clean(f):
    M = f.masters[0].id
    for n in NOEXPORT:
        if f.glyphs[n] is not None: f.glyphs[n].export = False
    # stray single-node open paths (no outline): they break overlap removal
    for g in f.glyphs:
        for L in g.layers:
            L.paths = [p for p in L.paths if p.closed or len(p.nodes) > 1]
    # smcp only mapped the lowercase (already capitals) onto the capitals: it does nothing; aalt pointed at it
    f.features = [ft for ft in f.features if ft.name not in ('smcp', 'aalt')]
    ss = next((ft for ft in f.features if ft.name == 'ss01'), None)
    if ss is not None:
        ss.notes = 'Name: Solid figures 1 3 5'
        if 'featureNames' not in ss.code:
            ss.code = 'featureNames { name "Solid figures 1 3 5"; };\n' + ss.code

def info(f, family, copyright, license, license_url):
    f.familyName = family
    f.copyright = copyright
    f.designer = 'MORYARTI inc.'; f.designerURL = 'https://moryarti.design'
    f.manufacturer = 'MORYARTI inc.'; f.manufacturerURL = 'https://moryarti.design'
    f.versionMajor = 1; f.versionMinor = 0
    cp = f.customParameters
    cp['vendorID'] = 'MRYT'
    cp['license'] = license; cp['licenseURL'] = license_url
    cp['fsType'] = []                                     # installable embedding
    cp['Use Typo Metrics'] = True
    for k in ('Disable Subroutines',): pass

def ltd(f):
    info(f, 'Moryarti Sans LTD', f'Copyright {YEAR} The Moryarti Sans LTD Project Authors ({REPO})',
         'This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at https://openfontlicense.org',
         'https://openfontlicense.org')

def build():
    f = GSFont(os.path.join(ROOT, 'sources', 'MoryartiSansLTD.glyphs'))
    clean(f); ltd(f)
    out = os.path.join(ROOT, 'fonts'); shutil.rmtree(out, ignore_errors=True)
    os.makedirs(out + '/ttf'); os.makedirs(out + '/webfonts')
    with tempfile.TemporaryDirectory() as td:
        src = os.path.join(td, f.familyName.replace(' ', '') + '.glyphs'); f.save(src)
        subprocess.run(['fontmake', '-g', src, '-o', 'ttf', '--output-dir', out + '/ttf', '--overlaps-backend', 'pathops',
                        '--flatten-components', '--filter', 'DecomposeTransformedComponentsFilter'], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for fn in os.listdir(out + '/ttf'):
        p = os.path.join(out, 'ttf', fn)
        subprocess.run(['gftools', 'fix-font', p, '-o', p, '--include-source-fixes'], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        t = TTFont(p); t['head'].fontRevision = 1.0
        t.save(p)
        t.flavor = 'woff2'; t.save(os.path.join(out, 'webfonts', fn.replace('.ttf', '.woff2')))
    return out

if __name__ == '__main__':
    print(build())
