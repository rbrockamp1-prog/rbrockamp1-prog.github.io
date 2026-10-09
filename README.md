# Ricky Brockamp — Product Design portfolio

Four complete, accessible versions of the portfolio. Each folder is a self-contained static site.

| Folder | Direction |
| --- | --- |
| `gravity/` | Candy-pastel, drag-and-fling physics hero |
| `swiss/` | International Typographic Style with a generative tile grid |
| `canvas/` | A design file you can pan and zoom (plus `overview.html` list view) |
| `fluid/` | Warm paper with a live ink simulation |

The root `index.html` is a switcher for comparing them. Once this is pushed, the sites are live at
`https://rbrockamp1-prog.github.io/gravity/` (and `/swiss/`, `/canvas/`, `/fluid/`).

**Making one the main site:** move the contents of that folder (not the folder itself) to the repo root,
replacing the switcher `index.html`.

## Pages in each site
Home · About · Process · Photo · Resume · four case studies in `work/`.

## Accessibility
- Skip link, landmarks, one `h1` per page, logical headings, `aria-current` navigation
- Visible focus rings; 44px touch targets; color contrast checked with axe-core (WCAG 2.2 AA)
- `prefers-reduced-motion` respected; continuous animation has a Pause control (WCAG 2.2.2)
- Decorative canvases are hidden from screen readers; all their text exists as real HTML
- Canvas keyboard shortcuts only work while the canvas has focus (WCAG 2.1.4), the view follows Tab focus, and `overview.html` offers a linear list view
- Descriptive alt text on every photo and project image; print stylesheet for the resume
