# Google Fonts readiness — Moryarti Sans Limited

Checked 2026-10-28 with Font Bakery 1.1.0 `check-googlefonts` on `fonts/ttf/MoryartiSansLimited-Regular.ttf` (built with
`gftools builder sources/config.yaml`), with METADATA.pb, OFL.txt and the description: **0 FAIL, 0 ERROR**, 11 WARN (with `documentation/article/`).
Validated in a Google Fonts family-directory layout with METADATA.pb, OFL.txt and article/; the article replaces DESCRIPTION.en_us.html for this check.
Full report: `docs/qa/rev17-fontbakery.md`.

## Version 1.002 — designer rev17

- Built from `MoryartiSans-rev17.glyphs`, preserving its kerning edits: the plain capital N no longer has a left kerning group.
- Retained the existing Limited metadata, OFL, vertical metrics and removal of the five company/logo glyphs and liga/dlig features.
- All 327 glyph outlines and the 322 Unicode mappings match version 1.001; ss01 remains functional.
- Export preparation and checks assisted by OpenAI Codex; no new glyph outlines were generated.

## Coverage
- GF Latin Core: 319 / 319 (plus U+25CC dotted circle). Accented letters are components (base + mark, aligned by anchors);
  marks attach in running text through the `mark` feature.
- Version 1.001 (designer's rev16): `ss01` gives solid 1, 3 and 5 (until 1.000 the .ss01 figures were copies of the halftone ones).
- Æ Œ Ø Ð Þ ẞ Ł Ħ § ¶ ª º ‹ › were assembled from existing outlines and reviewed and approved by the designer as they are in rev15.

## Vertical metrics
- Typo = hhea 3977 / −1024, line gap 0, USE_TYPO_METRICS: capitals centred in the line, 125% of UPM 4000. Only the line
  spacing changed; no outline was touched. Win 4277 / 1420 covers Å and the deepest descender.

## Warnings (acceptable / by design)
- unitsPerEm 4000 (not a power of 2) — allowed; needed for the halftone detail.
- contour_count, overlapping_path_segments, outline_jaggy_segments, outline_semi_vertical — the halftone dots and the designer's construction.
- vendor_id "MRYT" is not registered with Microsoft — optional to register.
- designer_profiles — KENT MORI's profile was sent through Google's form on 2026-10-22 (`docs/designer-profile.md`); the warning stays until Google adds it.
- metadata/category_hints — the name says "Sans", METADATA says DISPLAY; DISPLAY is intended.
- metadata/unreachable_subsetting — the spacing marks U+02D8 / U+02D9 fall outside the latin subsets; harmless.
- glyphsets/shape_languages, meta/script_lang_tags — informational.

## Before submitting
- Family name: "Moryarti Sans Limited". The Google Fonts submission form asks that the name not include the copyright
  holder's full name or acronyms; "Moryarti" is the copyright holder's name (MORYARTI inc.). Raise it with the Google Fonts
  team in the submission issue, and be ready to rename.
- Disclose in the submission how AI tools were used (the form requires it): the text is in `docs/google-fonts-submission.md`.
- Version 1.002 is prepared for review; tag the release after merging.
