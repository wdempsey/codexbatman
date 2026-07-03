# UI Direction — Warm Editorial ("soft-ui"), July 2026

Why the site should feel different, what it now feels like, and where the tokens came from.

## References

1. **[wdempsey/digitalrandomforest](https://github.com/wdempsey/digitalrandomforest)** — the maintainer's Quartz digital garden. Its `QUARTZ_DESIGN_TARGET.md` defines the target mood ("a quiet study, a research notebook — warm, calm, minimal, editorial") and an explicit avoid-list: developer documentation, dashboards, SaaS UI, heavy styling. Its `quartz.config.ts` supplies the concrete palette adopted here.
2. **[pi.dev](https://pi.dev/)** — calm one-column page, quiet nav, copy-first, with terminal recordings as the single visual flourish. The lesson taken: on a soft page, one dark element reads as intentional; five read as a dashboard.

## Decisions (scoped per maintainer, 2026-07-02)

- **Warm restyle, not redesign** — palette/typography/softness across the site; homepage structure, dark sections, and amber CTAs unchanged.
- **Terminals stay dark** — the pi.dev pattern; only their shadow/border soften in light mode.
- **Serif headers (Fraunces, already in place, extended to h3) + DM Sans body** — the full garden stack (Newsreader body) was considered and deferred.

## Token map (light scheme only; slate unchanged)

| Role | Was (Material indigo defaults) | Now | Source |
|------|-------------------------------|-----|--------|
| Page background | `#ffffff` | `#f8f4ec` parchment | garden `light` |
| Ink | near-black | `#2f2b27` charcoal | garden `dark` |
| Secondary text | cool gray | `#5f584f` / `#8f8577` | garden `darkgray`/`gray` |
| Borders / hairlines | cool gray | `#e6dfd3` | garden `lightgray` |
| Links | indigo | `#776657` | garden `secondary` |
| Accent / hover | indigo | `#6f5b46` | derived (deeper `secondary` for contrast) |
| Header / primary buttons | indigo | `#3d362e` warm dark brown | derived from ink |
| Inline code bg | cool gray | `#f0e8db` | garden `highlight` |
| Terminal widgets | navy `#0d1b2e` | unchanged; softer warm shadow on paper | pi.dev pattern |

Implementation: single "Warm Editorial Restyle" block appended to `docs/stylesheets/extra.css` — pure CSS-variable overrides plus four small softening rules. Fully reversible by deleting the block.

## Contrast notes

`#776657` and `#6f5b46` on `#f8f4ec` both clear WCAG AA for body text (≈5.0:1 and ≈5.9:1). `#5f584f` secondary text ≈6.9:1. `#8f8577` is reserved for large/quiet text only (≈3.4:1 — passes AA large-text, fails body).

## Not done here (future passes)

- Homepage editorial rework (dark SaaS sections → quieter single-column) — deferred by scope decision; revisit after the restyle has lived for a while
- Home SVGs still carry the cool navy/indigo palette — regenerate via Asset Prompt Pack with the warm tokens
- Dark scheme warming toward the garden's dark palette (`#1e1b18` / `#f0e9dc`)
- Newsreader body text experiment on one long-form page before committing site-wide
