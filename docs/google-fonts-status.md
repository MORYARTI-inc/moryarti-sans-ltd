# Google Fonts readiness — Moryarti Sans LTD

Checked with fontbakery 1.1 `check-googlefonts` on fonts/ttf/MoryartiSansLTD-Regular.ttf with METADATA.pb, OFL.txt and the description.

## Coverage
- GF Latin Core: 319 / 319 (plus U+25CC dotted circle). Accented letters are components (base + mark, aligned by anchors);
  marks attach in running text through the `mark` feature. Built by `tools/accents.py` (in the master repository); Æ Œ Ø Ð Þ ẞ Ł Ħ § ¶ ª º ‹ › are
  first drafts assembled from existing outlines, for the designer to refine.

## Expected at submission (not real problems)
- broken_links (repository not yet on GitHub), and the checks that call fonts.google.com (no network here) — they pass once submitted.

## Warnings (acceptable / by design)
- unitsPerEm 4000 (not a power of 2) — allowed; needed for the halftone detail.
- contour_count, outline_* — the halftone dots and the designer's construction.
- vendor_id "MRYT" is not registered with Microsoft — optional to register.
- sTypoAscender 3353 is below the accented capitals (Á reaches ~3630): kept on purpose so line spacing stays as designed; win ascent 4277 covers Å, so nothing is clipped.
