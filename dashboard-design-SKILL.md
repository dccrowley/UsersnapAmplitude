---
name: dashboard-design
description: Create stunning, envy-inducing dashboards using Swiss grid principles, sophisticated colour palettes, and refined data visualisation. Use when the user asks to build dashboards, data visualisations, analytics interfaces, KPI displays, or any data-dense interface. Produces React/HTML dashboards with donut charts, Sankey diagrams, area charts, bar charts, and subtle animations. Follows International Typographic Style with WCAG AA accessibility.
---

# Dashboard Design Skill

Create dashboards that inspire genuine admiration through disciplined Swiss design, sophisticated colour theory, and obsessive attention to detail.

## Design Philosophy

Exceptional dashboards share three qualities:

1. **Restraint** - Show only what matters, eliminate visual noise
2. **Intentionality** - Every element serves a clear purpose
3. **Craft** - Obsessive micro-detail attention (shadows, borders, transitions)

## Workflow

1. Clarify the data story (3-5 key metrics maximum per view)
2. Select colour palette from references/palettes.md
3. Apply 8-point grid system and typography scale
4. Choose appropriate chart types for each metric
5. Add subtle animations that illuminate, not decorate
6. Verify WCAG AA compliance

## Swiss Grid Foundation

Use the **8-point spacing system** for all measurements:

```css
--space-xs: 4px;   /* Tight internal spacing */
--space-sm: 8px;   /* Icon gaps */
--space-md: 16px;  /* Default padding */
--space-lg: 24px;  /* Widget gaps */
--space-xl: 32px;  /* Section breaks */
--space-2xl: 48px; /* Major divisions */
--space-3xl: 64px; /* Page margins */
```

**Typography scale** (all text left-aligned, numbers right-aligned in tables):

| Element | Size | Weight |
|---------|------|--------|
| Dashboard title | 28-32px | Bold (700) |
| Section header | 18-20px | Semibold (600) |
| Widget title | 14-16px | Medium (500) |
| Body/labels | 12-14px | Regular (400) |
| Data values (hero) | 36-48px | Bold (700) |

**Font choices**: Inter, SF Pro, or similar high-quality sans-serif with clear distinction between 1/I and 0/O. Maximum 2 typefaces per dashboard.

## Colour Selection

See **references/palettes.md** for complete palette definitions with hex codes.

Quick selection guide:

- **Alef Brand**: Use Alef primary colours with yellow (#F5C542), lilac (#B8A9C9), red (#E85A4F) accents in matching tones
- **Sequential data**: Single hue, vary lightness 60+ percentage points
- **Diverging data**: Light neutral centre, contrasting dark extremes
- **Categorical**: Maximum 5-7 colours, vary lightness alongside hue

**Critical rules**:

- Never use rainbow palettes on numeric data
- Desaturate slightly for sophistication (avoid pure saturated colours)
- Maintain 3:1 contrast minimum for graphics, 4.5:1 for text
- Test with colourblind simulation tools

## Chart Implementation

See **references/charts.md** for detailed implementation patterns.

**Selection guide**:

| Data Relationship | Chart Type |
|-------------------|------------|
| Part-to-whole | Donut (max 5 segments) |
| Flow/conversion | Sankey |
| Trend over time | Area or line |
| Comparison | Horizontal bar |
| Distribution | Histogram or violin |
| Correlation | Scatter |

**Universal rules**:

- Direct label charts, avoid legends when possible
- Start bar chart Y-axes at zero (non-negotiable)
- Use rounded corners (4-8px) for modern aesthetic
- Never use 3D effects

## Animation Patterns

Use animation to illuminate data changes, not to impress:

```css
/* Entrance animation */
@keyframes fade-up {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}

.widget {
  animation: fade-up 0.4s ease-out forwards;
  animation-delay: calc(var(--index) * 80ms);
}

/* Value transitions */
.data-value {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Respect motion preferences */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

**Effective animation types**:

- Staggered entrance reveals
- Smooth data value transitions
- Subtle hover state changes
- Chart draw-on effects

## Technical Implementation

**React charting libraries** (in order of design control):

1. **Visx** (Airbnb) - Maximum control, steeper learning curve
2. **Recharts** - Best balance of ease and customisation
3. **Victory** - Accessibility-focused, works with React Native

**Dashboard grid structure**:

```css
.dashboard {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: var(--space-lg);
  padding: var(--space-2xl);
}

.widget-full { grid-column: span 12; }
.widget-half { grid-column: span 6; }
.widget-third { grid-column: span 4; }
.widget-quarter { grid-column: span 3; }

@media (max-width: 768px) {
  .widget-half, .widget-third, .widget-quarter {
    grid-column: span 12;
  }
}
```

## Anti-Patterns to Avoid

**Never do these**:

- Exceed single-screen boundaries (breaks simultaneous vision)
- Display excessive precision ($3.8M not $3,848,305.93)
- Use different chart types just for variety
- Apply 3D effects or fake gauges/meters
- Use chartjunk (decorative elements that add no data meaning)
- Place vendor logos in prime data real estate

**Typography crimes**:

- Missing axis labels
- Confusing or distant legends
- Text too small to read
- Multiple disparate fonts

**Colour crimes**:

- Rainbow palettes on numeric variables
- Different colours per bar with no meaning
- More than 5-7 total colours
- Insufficient contrast for accessibility

## Quality Checklist

Before delivering, verify:

- [ ] Maximum 3-5 key metrics visible without scrolling
- [ ] 8-point grid spacing applied consistently
- [ ] Typography scale followed (max 2 fonts)
- [ ] Colours pass WCAG AA contrast requirements
- [ ] Charts directly labelled (minimal legend use)
- [ ] Animations respect prefers-reduced-motion
- [ ] Bar charts start Y-axis at zero
- [ ] Numbers display appropriate precision
- [ ] Mobile responsive breakpoints work
- [ ] No chartjunk or decorative clutter

## Reference Files

- **references/palettes.md** - Complete colour palette definitions with hex codes
- **references/charts.md** - Detailed chart implementation patterns and code examples
