# Google Fonts readiness — Moryarti Sans Limited

Checked 2026-10-21 with Font Bakery 1.1.0 `check-googlefonts` on `fonts/ttf/MoryartiSansLimited-Regular.ttf` (built with
`gftools builder sources/config.yaml`), with METADATA.pb, OFL.txt and the description: **0 FAIL**, 12 WARN.

## Coverage
- GF Latin Core: 319 / 319 (plus U+25CC dotted circle). Accented letters are components (base + mark, aligned by anchors);
  marks attach in running text through the `mark` feature.
- Æ Œ Ø Ð Þ ẞ Ł Ħ § ¶ ª º ‹ › are first drafts assembled from existing outlines, for the designer to refine before submission.

## Vertical metrics
- Typo = hhea 3977 / −1024, line gap 0, USE_TYPO_METRICS: capitals centred in the line, 125% of UPM 4000. Only the line
  spacing changed; no outline was touched. Win 4277 / 1420 covers Å and the deepest descender.

## Warnings (acceptable / by design)
- unitsPerEm 4000 (not a power of 2) — allowed; needed for the halftone detail.
- contour_count, overlapping_path_segments, outline_jaggy_segments, outline_semi_vertical — the halftone dots and the designer's construction.
- vendor_id "MRYT" is not registered with Microsoft — optional to register.
- article/images — no `documentation/article/` yet (optional, recommended).
- designer_profiles — MORYARTI inc. has no Google Fonts designer profile yet (submitted through Google's form).
- metadata/category_hints — the name says "Sans", METADATA says DISPLAY; DISPLAY is intended.
- metadata/unreachable_subsetting — the spacing marks U+02D8 / U+02D9 fall outside the latin subsets; harmless.
- glyphsets/shape_languages, meta/script_lang_tags — informational.

## Before submitting
- Family name: "Moryarti Sans Limited". The Google Fonts submission form asks that the name not include the copyright
  holder's full name or acronyms; "Moryarti" is the copyright holder's name (MORYARTI inc.). Raise it with the Google Fonts
  team in the submission issue, and be ready to rename.
- Disclose in the submission how AI tools were used in making the project (the form requires it).
- Tag the release (v1.000) once this is merged.
