# Moryarti Sans — halftone rules (read from rev04)

The halftone is a cast shadow, drawn as rows of small round dots.

- Grid: rows every ~59 units (some glyphs 52–58), dots on a diagonal lattice.
- Gradient: the stroke is solid at the bottom; above it, black dots (≈86 → 33 units across, rows 6–20) overlap into the solid and shrink upward, so the stroke dissolves upward into the shadow's edge. (rev04 also has tiny specks inside the solid at rows 0–5; they don't show.)
- Generator: tools/halftone.py reproduces M's block; tools/ht_numerals.py makes the 7 / 1 study variants.
- Start heights (top of the halftone) are restricted to a few fixed positions:
  - **1748**: M, L, N, W, K, X (K/X from 630, the rest from 570) — the shared standard height
  - **lowered for design**: R 836, P 611, Q 576, H 1488, Y 1176
  - **F** runs higher, 308–2092
  - **4** has its own position: 1040–2218 (the only figure with halftone)
- New glyphs that carry halftone must use one of these heights and the same lattice and size gradient.
