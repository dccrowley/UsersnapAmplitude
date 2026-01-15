# Colour Palettes Reference

## Alef Brand Extended

Primary Alef colours with complementary accent tones.

### Core Brand

```css
--alef-primary: #00A3E0;
--alef-secondary: #003C71;
--alef-accent: #7AB800;
```

### Extended Accent Palette

Yellow, lilac, and red tones that harmonise with Alef brand:

```css
/* Yellow spectrum */
--accent-yellow-light: #FEF3C7;
--accent-yellow: #F5C542;
--accent-yellow-dark: #D4A012;

/* Lilac spectrum */
--accent-lilac-light: #E8E0F0;
--accent-lilac: #B8A9C9;
--accent-lilac-dark: #8B7BA3;

/* Red spectrum */
--accent-red-light: #FEE2E2;
--accent-red: #E85A4F;
--accent-red-dark: #C53030;
```

### Neutral Scale

```css
--neutral-50: #FAFAFA;
--neutral-100: #F5F5F5;
--neutral-200: #E5E5E5;
--neutral-300: #D4D4D4;
--neutral-400: #A3A3A3;
--neutral-500: #737373;
--neutral-600: #525252;
--neutral-700: #404040;
--neutral-800: #262626;
--neutral-900: #171717;
```

---

## Chic Contemporary Palettes

### Pastel Sophistication

Soft, muted tones for approachable data stories:

```css
--pastel-coral: #FD7F6F;
--pastel-blue: #7EB0D5;
--pastel-sage: #B2E061;
--pastel-lilac: #BD7EBE;
--pastel-amber: #FFB55A;
--pastel-lavender: #BEB9DB;
--pastel-mint: #8BD3C7;
```

### Premium Earth

Sophisticated, grounded palette:

```css
--earth-plum: #7C1158;
--earth-purple: #4421AF;
--earth-azure: #0D88E6;
--earth-teal: #00B7C7;
--earth-wheat: #EBDC78;
--earth-moss: #5C7C5C;
```

### Sage-Coral-Lilac

Balanced contemporary combination:

```css
--scl-sage: #9CAE9B;
--scl-coral: #FD7F6F;
--scl-lilac: #BD7EBE;
--scl-seafoam: #8DDCDC;
--scl-slate: #6D8196;
```

### Midnight Professional

Dark theme with vibrant accents:

```css
--midnight-bg: #0F0F1A;
--midnight-surface: #1A1A2E;
--midnight-border: #2D2D44;
--midnight-cyan: #00D4FF;
--midnight-magenta: #FF00E5;
--midnight-lime: #CCFF00;
--midnight-text: #E8E8F0;
--midnight-muted: #8888A0;
```

---

## Sequential Scales

For continuous numeric data. Light values = low, dark values = high.

### Blue Sequential

```css
--seq-blue-1: #EFF6FF;
--seq-blue-2: #BFDBFE;
--seq-blue-3: #60A5FA;
--seq-blue-4: #2563EB;
--seq-blue-5: #1E40AF;
```

### Teal Sequential

```css
--seq-teal-1: #F0FDFA;
--seq-teal-2: #99F6E4;
--seq-teal-3: #2DD4BF;
--seq-teal-4: #0D9488;
--seq-teal-5: #115E59;
```

### Purple Sequential

```css
--seq-purple-1: #FAF5FF;
--seq-purple-2: #DDD6FE;
--seq-purple-3: #A78BFA;
--seq-purple-4: #7C3AED;
--seq-purple-5: #5B21B6;
```

### Warm Sequential (Yellow to Red)

```css
--seq-warm-1: #FEF9C3;
--seq-warm-2: #FDE047;
--seq-warm-3: #FB923C;
--seq-warm-4: #EF4444;
--seq-warm-5: #991B1B;
```

---

## Diverging Scales

For data with meaningful midpoint. Centre should be neutral/light.

### Brown-Teal Diverging

```css
--div-brown-5: #8C510A;
--div-brown-4: #BF812D;
--div-brown-3: #DFC27D;
--div-neutral: #F5F5F5;
--div-teal-3: #80CDC1;
--div-teal-4: #35978F;
--div-teal-5: #01665E;
```

### Red-Blue Diverging

```css
--div-red-5: #B91C1C;
--div-red-4: #EF4444;
--div-red-3: #FCA5A5;
--div-neutral: #F9FAFB;
--div-blue-3: #93C5FD;
--div-blue-4: #3B82F6;
--div-blue-5: #1D4ED8;
```

### Purple-Green Diverging

```css
--div-purple-5: #6B21A8;
--div-purple-4: #A855F7;
--div-purple-3: #D8B4FE;
--div-neutral: #FAFAFA;
--div-green-3: #86EFAC;
--div-green-4: #22C55E;
--div-green-5: #15803D;
```

---

## Categorical Palettes

For discrete categories. Maximum 7 colours recommended.

### Vibrant Categorical (5 colours)

```css
--cat-1: #3B82F6; /* Blue */
--cat-2: #10B981; /* Emerald */
--cat-3: #F59E0B; /* Amber */
--cat-4: #EF4444; /* Red */
--cat-5: #8B5CF6; /* Violet */
```

### Muted Categorical (7 colours)

```css
--cat-muted-1: #6B7280; /* Gray */
--cat-muted-2: #3B82F6; /* Blue */
--cat-muted-3: #10B981; /* Green */
--cat-muted-4: #F59E0B; /* Amber */
--cat-muted-5: #EF4444; /* Red */
--cat-muted-6: #8B5CF6; /* Purple */
--cat-muted-7: #EC4899; /* Pink */
```

### Soft Categorical (5 colours)

```css
--cat-soft-1: #93C5FD; /* Light blue */
--cat-soft-2: #86EFAC; /* Light green */
--cat-soft-3: #FCD34D; /* Light yellow */
--cat-soft-4: #FCA5A5; /* Light red */
--cat-soft-5: #C4B5FD; /* Light purple */
```

---

## Semantic Colours

Consistent meaning across dashboards:

```css
/* Status */
--semantic-success: #10B981;
--semantic-warning: #F59E0B;
--semantic-error: #EF4444;
--semantic-info: #3B82F6;

/* Trends */
--semantic-positive: #10B981;
--semantic-negative: #EF4444;
--semantic-neutral: #6B7280;

/* Comparison */
--semantic-current: #3B82F6;
--semantic-previous: #9CA3AF;
--semantic-target: #8B5CF6;
```

---

## Accessibility Notes

### Contrast Requirements

- **Text on backgrounds**: 4.5:1 minimum (WCAG AA)
- **Large text (18px+ bold or 24px+)**: 3:1 minimum
- **Graphic elements**: 3:1 minimum against adjacent colours

### Colourblind-Safe Combinations

These pairs work for most colour vision deficiencies:

```css
/* Blue + Orange (deuteranopia/protanopia safe) */
--cb-safe-1: #3B82F6;
--cb-safe-2: #F97316;

/* Blue + Yellow */
--cb-safe-3: #2563EB;
--cb-safe-4: #EAB308;

/* Purple + Green (with lightness difference) */
--cb-safe-5: #7C3AED;
--cb-safe-6: #22C55E;
```

### Testing Tools

- Viz Palette ([vizpalette.com](https://vizpalette.com))
- ColorBrewer ([colorbrewer2.org](https://colorbrewer2.org))
- Stark plugin for Figma
- Chrome DevTools colour vision simulation
