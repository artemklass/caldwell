# Caldwell Private Health — Website

## Behavior Rules — Absolute

- **Never ask clarifying questions before doing the work.** Pick the best interpretation, execute it, then briefly state what you did.
- **No confirmation prompts.** Do not ask "want me to do X?" or "should I proceed?" — just do it.
- **Only pause** for actions that are truly destructive and irreversible (e.g. dropping a database, force-pushing to a shared branch against user intent).
- When making a design choice, make the best call and mention it in one sentence after the fact. The user will say "revert" if they don't like it.

## Project Overview
Single-page marketing website for **Caldwell Private Health** — a private personal training business serving high-net-worth men in Fort Lauderdale, FL. Domain: caldwellreserve.com

## Tech Stack
- **Pure HTML/CSS/JS** — everything lives in `index.html`, no build step, no framework
- Fonts: Cormorant (headings, serif) + DM Sans (body, modern)
- Calendly widget for booking
- Vimeo player API for video
- Favicon: `favicon.svg`
- Logo: `LOGOCALDWELL.png`

## Brand Colors
```
--navy:        #07101e   (primary background — deep, authoritative)
--navy-mid:    #0d1a2e   (cards/secondary bg)
--parchment:   #F0EBE0   (section breaks — light sections)
--parchment-d: #E6DFCF   (slightly darker parchment)
--gold:        #C9A84C   (primary accent — authoritative)
--gold-lt:     #D6BC5E   (lighter gold)
--gold-deep:   #8B6A35   (dark gold for gradients)
--gold-mid:    #A8894A   (mid-tone gold)
```

## Design Rules — Never Break These
- Dark navy background with gold accents is the core aesthetic — do not introduce new colors
- Cormorant for all display/heading text, DM Sans for body/UI
- Everything is in `index.html` — do not split into multiple files unless explicitly asked
- Mobile responsive — always verify changes don't break mobile layout
- Luxury, understated tone — no flashy animations, no aggressive CTAs

## How to Work
- All edits happen inside `index.html`
- To preview: open `index.html` in a browser, or use Live Server in VS Code
- Screenshot tool available via `node screenshot.mjs http://localhost:PORT`
- No npm, no build process — just edit and refresh

## Business Context
- Owner: Artem (personal trainer)
- Clientele: High-net-worth men, Fort Lauderdale
- Goal of site: Drive Calendly bookings for discovery calls
- Tone: Private, premium, results-driven — like a members-only club, not a gym
