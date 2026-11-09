# Warm Editorial — Style Reference

Warm, steady, textured. Inspired by high-quality print publications: off-white paper, brown-ochre ink, generous margins. Suited to research reports, brand white papers and annual retrospectives.

---

## Colors

```css
:root {
  --primary:      #92400E;   /* deep amber brown: heading rules, links, emphasis */
  --primary-light:#FEF3C7;   /* pale amber: KPI card background */
  --accent:       #B45309;   /* warm orange: highlighted numbers */
  --bg:           #FDFAF6;   /* warm off-white: page background */
  --surface:      #FFFFFF;   /* pure white: card background */
  --text:         #1C1917;   /* warm near-black: body text */
  --text-muted:   #78716C;   /* warm mid-gray: secondary text, metadata */
  --border:       #E7E5E4;   /* warm light gray: borders and dividers */
  --success:      #065F46;
  --warning:      #92400E;
  --danger:       #991B1B;
}
```

**Avoid:** cool gray (#888), pure blue (#2563EB), neon colors, dark backgrounds

---

## Typography

Headings use an elegant serif face; body text uses a highly readable sans-serif.

```html
<!-- Google Fonts -->
<link href="https://fonts.googleapis.com/css2?family=Lora:wght@600;700&family=Source+Sans+3:wght@400;600&display=swap" rel="stylesheet">
```

```css
--font-sans: 'Source Sans 3', system-ui, sans-serif;
--font-serif: 'Lora', Georgia, serif;
/* h1/h2 use font-family: var(--font-serif) */
```

---

## Layout

Generous whitespace, easy to read.

```css
--radius: 4px;   /* sharp corners for data elements */
/* cards use border-radius: 8px */
/* max report width 900px, ample left/right padding */
```

---

## Best For

Research reports · brand white papers · annual retrospectives · internal insight documents · any report that needs a "professional but not cold" tone
