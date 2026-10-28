## FontBakery report

fontbakery version: 1.1.0







## Check results



<details><summary>[11] MoryartiSansLimited-Regular.ttf</summary>
<div>
<details>
    <summary>⚠️ <b>WARN</b> Checking unitsPerEm value is reasonable. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-unitsperem">opentype/unitsperem</a></summary>
    <div>


> 
> According to the OpenType spec:
> 
> The value of unitsPerEm at the head table must be a value
> between 16 and 16384. Any value in this range is valid.
> 
> In fonts that have TrueType outlines, a power of 2 is recommended
> as this allows performance optimizations in some rasterizers.
> 
> But 1000 is a commonly used value. And 2000 may become
> increasingly more common on Variable Fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>In order to optimize performance on some legacy renderers, the value of unitsPerEm at the head table should ideally be a power of 2 between 16 to 16384. And values of 1000 and 2000 are also common and may be just fine as well. But we got 4000 instead.</p>
 [code: suboptimal]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>


> 
> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only
> be constructured in a handful of ways. This means a glyph's contour count
> will only differ slightly amongst different fonts, e.g a 'g' could either
> be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs
> to a display family.
> 
> This check currently does not cover variable fonts because there's plenty
> of alternative ways of constructing glyphs with multiple outlines for each
> feature in a VarFont. The expected contour count data for this check is
> currently optimized for the typical construction of glyphs in static fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: ampersand	Contours detected: 8	Expected: 1, 2 or 3

- Glyph name: zero	Contours detected: 91	Expected: 2 or 3

- Glyph name: one	Contours detected: 105	Expected: 1

- Glyph name: two	Contours detected: 41	Expected: 1

- Glyph name: three	Contours detected: 145	Expected: 1

- Glyph name: four	Contours detected: 140	Expected: 1 or 2

- Glyph name: five	Contours detected: 176	Expected: 1

- Glyph name: six	Contours detected: 182	Expected: 1 or 2

- Glyph name: seven	Contours detected: 61	Expected: 1

- Glyph name: eight	Contours detected: 66	Expected: 3

- 228 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>


> 
> Some rasterizers encounter difficulties when rendering glyphs with
> overlapping path segments.
> 
> A path segment is a section of a path defined by two on-curve points.
> When two segments share the same coordinates, they are considered
> overlapping.
> 




> Original proposal: https://github.com/google/fonts/issues/7594#issuecomment-2401909084





* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* B (U+0042): B&lt;&lt;1999.0,1736.0&gt;-&lt;1992.0,1712.0&gt;-&lt;1967.0,1712.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E9E (U+1E9E): B&lt;&lt;1999.0,1736.0&gt;-&lt;1992.0,1712.0&gt;-&lt;1967.0,1712.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E9E (U+1E9E): B&lt;&lt;2884.0,1607.0&gt;-&lt;2880.0,1613.0&gt;-&lt;2879.0,1617.0&gt;&gt; has the same coordinates as a previous segment.

* Y (U+0059): B&lt;&lt;1788.0,269.0&gt;-&lt;1788.0,270.0&gt;-&lt;1787.0,270.0&gt;&gt; has the same coordinates as a previous segment.

* Yacute (U+00DD): B&lt;&lt;1788.0,269.0&gt;-&lt;1788.0,270.0&gt;-&lt;1787.0,270.0&gt;&gt; has the same coordinates as a previous segment.

* Ycircumflex (U+0176): B&lt;&lt;1788.0,269.0&gt;-&lt;1788.0,270.0&gt;-&lt;1787.0,270.0&gt;&gt; has the same coordinates as a previous segment.

* Ydieresis (U+0178): B&lt;&lt;1788.0,269.0&gt;-&lt;1788.0,270.0&gt;-&lt;1787.0,270.0&gt;&gt; has the same coordinates as a previous segment.

* Ygrave (U+1EF2): B&lt;&lt;1788.0,269.0&gt;-&lt;1788.0,270.0&gt;-&lt;1787.0,270.0&gt;&gt; has the same coordinates as a previous segment.

* b (U+0062): B&lt;&lt;1999.0,1736.0&gt;-&lt;1992.0,1712.0&gt;-&lt;1967.0,1712.0&gt;&gt; has the same coordinates as a previous segment.

* germandbls (U+00DF): B&lt;&lt;1999.0,1736.0&gt;-&lt;1992.0,1712.0&gt;-&lt;1967.0,1712.0&gt;&gt; has the same coordinates as a previous segment.

* 15 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if category on METADATA.pb matches what can be inferred from the family name. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-category-hints">googlefonts/metadata/category_hints</a></summary>
    <div>


> 
> Sometimes the font familyname contains words that hint at which is the most
> likely correct category to be declared on METADATA.pb
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3624





* ⚠️ **WARN** <p>Familyname seems to hint at &quot;SANS_SERIF&quot; but METADATA.pb declares it as &quot;['DISPLAY']&quot;.</p>
 [code: inferred-category]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> METADATA.pb: Designers are listed correctly on the Google Fonts catalog? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-designer-profiles">googlefonts/metadata/designer_profiles</a></summary>
    <div>


> 
> Google Fonts has a catalog of designers.
> 
> This check ensures that the online entries of the catalog can be found based
> on the designer names listed on the METADATA.pb file.
> 
> It also validates the URLs and file formats are all correctly set.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3083





* ⚠️ **WARN** <p>It seems that KENT MORI is still not listed on the designers catalog. Please submit a photo and a link to a webpage where people can learn more about the work of this designer/typefoundry.</p>
 [code: profile-not-found]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unreachable-subsetting">googlefonts/metadata/unreachable_subsetting</a></summary>
    <div>


> 
> This check ensures that all encoded glyphs in the font are covered by a
> subset declared in the METADATA.pb. Google Fonts splits the font into
> a set of subset fonts based on the contents of the `subsets` field and
> the subset definitions in the `glyphsets` repository.
> 
> Any encoded glyphs which are not by any of these subset definitions
> will not be served in the subsetted fonts, and so will be unreachable to
> the end user.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4097
> See also: https://github.com/fonttools/fontbakery/pull/4273





* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: cherokee, coptic, tifinagh, math</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: coptic, hebrew, old-permic, math, malayalam, tai-le, canadian-aboriginal, syriac, tifinagh, todhri, duployan</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math
5 more.</li>
</ul>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>latin</code>, <code>latin-ext</code>, <code>menu</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>


> 
> This check uses a heuristic to determine which GF glyphsets a font supports.
> Then it checks the font for correct shaping behaviour for all languages in
> those glyphsets.
> 




> Original proposal: https://github.com/googlefonts/fontbakery/issues/4147





* ⚠️ **WARN** <p>GF_TransLatin_Arabic glyphset:</p>
<table>
<thead>
<tr>
<th align="left">WARN messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ĕ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ĭ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ŀ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ŏ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ō</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ŭ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ĕ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ĭ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ŀ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ŏ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ō</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ŭ</td>
<td align="left">ca_Latn (Catalan)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ĕ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ĭ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ŏ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ō</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ŭ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ĕ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ĭ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ŏ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ō</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ŭ</td>
<td align="left">cs_Latn (Czech), cy_Latn (Welsh), es_Latn (Spanish), hu_Latn (Hungarian), pt_Latn (Portuguese), sk_Latn (Slovak) and tr_Latn (Turkish)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ǿ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ǿ</td>
<td align="left">da_Latn (Danish)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ĕ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ĭ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ŏ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ō</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ŭ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ĕ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ĭ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ŏ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ō</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ſ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ŭ</td>
<td align="left">de_Latn (German)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ĕ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ĭ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ŏ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ō</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ŭ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ĕ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ĭ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ŏ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ō</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ŭ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ʻ</td>
<td align="left">en_Latn (English)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ǧ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ǥ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ȟ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ǩ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ŋ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ŝ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ţ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ŧ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ʒ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ǯ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ǧ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ǥ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ȟ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ǩ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ŋ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ŝ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ţ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ŧ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ʒ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ǯ</td>
<td align="left">fi_Latn (Finnish)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ǔ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ſ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ǔ</td>
<td align="left">fr_Latn (French)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ẽ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ĩ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ũ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ẽ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ĩ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ũ</td>
<td align="left">lt_Latn (Lithuanian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ō</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ŗ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ō</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ŗ</td>
<td align="left">lv_Latn (Latvian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ǎ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ŋ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ŧ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ǎ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ŋ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ŧ</td>
<td align="left">nb_Latn (Norwegian Bokmål)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ĳ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ĳ</td>
<td align="left">nl_Latn (Dutch)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ţ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ţ</td>
<td align="left">ro_Latn (Romanian)</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-jaggy-segments">outline_jaggy_segments</a></summary>
    <div>


> 
> This check heuristically detects outline segments which form a particularly
> small angle, indicative of an outline error. This may cause false positives
> in cases such as extreme ink traps, so should be regarded as advisory and
> backed up by manual inspection.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3064





* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* B (U+0042): B&lt;&lt;2009.0,1391.0&gt;-&lt;2009.0,1375.0&gt;-&lt;1997.0,1363.0&gt;&gt;/B&lt;&lt;1997.0,1363.0&gt;-&lt;2010.0,1374.0&gt;-&lt;2027.0,1374.0&gt;&gt; = 4.763641690726144

* B (U+0042): B&lt;&lt;2027.0,1374.0&gt;-&lt;2041.0,1374.0&gt;-&lt;2054.0,1364.0&gt;&gt;/B&lt;&lt;2054.0,1364.0&gt;-&lt;2044.0,1376.0&gt;-&lt;2044.0,1391.0&gt;&gt; = 12.625836878907332

* B (U+0042): B&lt;&lt;2085.0,1350.0&gt;-&lt;2070.0,1350.0&gt;-&lt;2059.0,1359.0&gt;&gt;/B&lt;&lt;2059.0,1359.0&gt;-&lt;2069.0,1347.0&gt;-&lt;2069.0,1332.0&gt;&gt; = 10.905022045234425

* B (U+0042): B&lt;&lt;2113.0,1805.0&gt;-&lt;2113.0,1819.0&gt;-&lt;2124.0,1828.0&gt;&gt;/L&lt;&lt;2124.0,1828.0&gt;--&lt;2069.0,1786.0&gt;&gt; = 1.9227374497316982

* B (U+0042): B&lt;&lt;2145.0,1374.0&gt;-&lt;2160.0,1374.0&gt;-&lt;2172.0,1365.0&gt;&gt;/B&lt;&lt;2172.0,1365.0&gt;-&lt;2162.0,1377.0&gt;-&lt;2162.0,1391.0&gt;&gt; = 13.324531261890755

* B (U+0042): B&lt;&lt;2189.0,1352.0&gt;-&lt;2183.0,1354.0&gt;-&lt;2177.0,1359.0&gt;&gt;/B&lt;&lt;2177.0,1359.0&gt;-&lt;2187.0,1347.0&gt;-&lt;2187.0,1332.0&gt;&gt; = 10.388857815469583

* B (U+0042): B&lt;&lt;2220.0,1313.0&gt;-&lt;2227.0,1310.0&gt;-&lt;2229.0,1308.0&gt;&gt;/B&lt;&lt;2229.0,1308.0&gt;-&lt;2221.0,1319.0&gt;-&lt;2221.0,1332.0&gt;&gt; = 8.972626614896358

* B (U+0042): B&lt;&lt;2221.0,1332.0&gt;-&lt;2221.0,1347.0&gt;-&lt;2231.0,1359.0&gt;&gt;/B&lt;&lt;2231.0,1359.0&gt;-&lt;2221.0,1350.0&gt;-&lt;2205.0,1350.0&gt;&gt; = 8.207216411918077

* B (U+0042): B&lt;&lt;2246.0,1391.0&gt;-&lt;2246.0,1376.0&gt;-&lt;2237.0,1365.0&gt;&gt;/B&lt;&lt;2237.0,1365.0&gt;-&lt;2248.0,1374.0&gt;-&lt;2263.0,1374.0&gt;&gt; = 11.42118627499929

* B (U+0042): B&lt;&lt;2340.0,1332.0&gt;-&lt;2340.0,1349.0&gt;-&lt;2350.0,1359.0&gt;&gt;/B&lt;&lt;2350.0,1359.0&gt;-&lt;2338.0,1350.0&gt;-&lt;2323.0,1350.0&gt;&gt; = 8.13010235415596

* 854 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: found-jaggy-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any semi-vertical or semi-horizontal lines? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-semi-vertical">outline_semi_vertical</a></summary>
    <div>


> 
> This check detects line segments which are nearly, but not quite, exactly
> horizontal or vertical. Sometimes such lines are created by design, but often
> they are indicative of a design error.
> 
> This check is disabled for italic styles, which often contain nearly-upright
> lines.
> 




> Original proposal: https://github.com/fonttools/fontbakery/pull/3088





* ⚠️ **WARN** <p>The following glyphs have semi-vertical/semi-horizontal lines:</p>
<pre><code>* W (U+0057): L&lt;&lt;4733.0,1476.0&gt;--&lt;3561.0,1477.0&gt;&gt;

* Wacute (U+1E82): L&lt;&lt;4733.0,1476.0&gt;--&lt;3561.0,1477.0&gt;&gt;

* Wcircumflex (U+0174): L&lt;&lt;4733.0,1476.0&gt;--&lt;3561.0,1477.0&gt;&gt;

* Wdieresis (U+1E84): L&lt;&lt;4733.0,1476.0&gt;--&lt;3561.0,1477.0&gt;&gt;

* Wgrave (U+1E80): L&lt;&lt;4733.0,1476.0&gt;--&lt;3561.0,1477.0&gt;&gt;

* seven (U+0037): L&lt;&lt;1539.0,-2.0&gt;--&lt;451.0,1.0&gt;&gt;

* w (U+0077): L&lt;&lt;4733.0,1476.0&gt;--&lt;3561.0,1477.0&gt;&gt;

* wacute (U+1E83): L&lt;&lt;4733.0,1476.0&gt;--&lt;3561.0,1477.0&gt;&gt;

* wcircumflex (U+0175): L&lt;&lt;4733.0,1476.0&gt;--&lt;3561.0,1477.0&gt;&gt;

* wdieresis (U+1E85): L&lt;&lt;4733.0,1476.0&gt;--&lt;3561.0,1477.0&gt;&gt;

* wgrave (U+1E81): L&lt;&lt;4733.0,1476.0&gt;--&lt;3561.0,1477.0&gt;&gt;
</code></pre>
 [code: found-semi-vertical]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-meta-script-lang-tags">googlefonts/meta/script_lang_tags</a></summary>
    <div>


> 
> The OpenType 'meta' table originated at Apple. Microsoft added it to OT with
> just two DataMap records:
> 
> - dlng: comma-separated ScriptLangTags that indicate which scripts,
> or languages and scripts, with possible variants, the font is designed for.
> 
> - slng: comma-separated ScriptLangTags that indicate which scripts,
> or languages and scripts, with possible variants, the font supports.
> 
> 
> The slng structure is intended to describe which languages and scripts the
> font overall supports. For example, a Traditional Chinese font that also
> contains Latin characters, can indicate Hant,Latn, showing that it supports
> Hant, the Traditional Chinese variant of the Hani script, and it also
> supports the Latn script.
> 
> The dlng structure is far more interesting. A font may contain various glyphs,
> but only a particular subset of the glyphs may be truly "leading" in the design,
> while other glyphs may have been included for technical reasons. Such a
> Traditional Chinese font could only list Hant there, showing that it’s designed
> for Traditional Chinese, but the font would omit Latn, because the developers
> don’t think the font is really recommended for purely Latin-script use.
> 
> The tags used in the structures can comprise just script, or also language
> and script. For example, if a font has Bulgarian Cyrillic alternates in the
> locl feature for the cyrl BGR OT languagesystem, it could also indicate in
> dlng explicitly that it supports bul-Cyrl. (Note that the scripts and languages
> in meta use the ISO language and script codes, not the OpenType ones).
> 
> This check ensures that the font has the meta table containing the
> slng and dlng structures.
> 
> All families in the Google Fonts collection should contain the 'meta' table.
> Windows 10 already uses it when deciding on which fonts to fall back to.
> The Google Fonts API and also other environments could use the data for
> smarter filtering. Most importantly, those entries should be added
> to the Noto fonts.
> 
> In the font making process, some environments store this data in external
> files already. But the meta table provides a convenient way to store this
> inside the font file, so some tools may add the data, and unrelated tools
> may read this data. This makes the solution much more portable and universal.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3349





* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-vendor-id">googlefonts/vendor_id</a></summary>
    <div>


> 
> Microsoft keeps a list of font vendors and their respective contact info. This
> list is updated regularly and is indexed by a 4-char "Vendor ID" which is
> stored in the achVendID field of the OS/2 table.
> 
> Registering your ID is not mandatory, but it is a good practice since some
> applications may display the type designer / type foundry contact info on some
> dialog and also because that info will be visible on Microsoft's website:
> 
> https://docs.microsoft.com/en-us/typography/vendors/
> 
> This check verifies whether or not a given font's vendor ID is registered in
> that list or if it has some of the default values used by the most common
> font editors.
> 
> Each new FontBakery release includes a cached copy of that list of vendor IDs.
> If you registered recently, you're safe to ignore warnings emitted by this
> check, since your ID will soon be included in one of our upcoming releases.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3943
> See also: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>OS/2 VendorID value 'MRYT' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: unknown]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 11 | 66 | 7 | 152 | 0 | 
| 0% | 0% | 0% | 5% | 28% | 3% | 64% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
