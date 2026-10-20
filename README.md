# Moryarti Sans LTD

A display typeface from the MORYARTI inc. logotype: heavy geometric capitals with a halftone shadow.
Capitals only (lowercase input sets the same forms). Figures 1–5 carry the halftone; `ss01` gives solid 1, 3 and 5.

## Build

```bash
pip install -r requirements.txt
python3 tools/build.py            # → fonts/ttf/MoryartiSansLTD-Regular.ttf, fonts/webfonts/MoryartiSansLTD-Regular.woff2
fontbakery check-googlefonts fonts/ttf/*.ttf
```

## Web

```css
@font-face{font-family:"Moryarti Sans LTD";src:url(MoryartiSansLTD-Regular.woff2) format("woff2");font-weight:400;font-display:swap}
.figures-solid{font-feature-settings:"ss01" 1}      /* 1 3 5 without halftone */
```

## Notes

- Metrics: UPM 4000, cap height 2953; ascender 3353 / descender −400 / line gap 0 (hhea = typo, USE_TYPO_METRICS); win 3916 / 1420.
- Halftone rules: `docs/halftone-rules.md`. Google Fonts readiness: `docs/google-fonts-status.md`.

## Licence

This Font Software is licensed under the SIL Open Font License, Version 1.1 (`OFL.txt`).
