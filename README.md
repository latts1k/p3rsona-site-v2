# P3RSONA site

The Jack of All Trades Content Deck: home page plus one page per card.

- **Change copy or prices:** edit `CARDS` in `tools/build.py`, then run `python3 tools/build.py` (it rewrites `index.html` and `card/*/index.html`).
- **Plug in the Tally forms:** paste the form IDs into `assets/forms.js`. Empty values fall back to Instagram / built-in unlock fields.
- **Card art:** `assets/cards/*.svg` (fonts embedded).
- **Hosting:** Vercel, no build step. Every push to `main` goes live.

Before launch: confirm the P3RSONA Amplified and Next Gen prices (both show "being finalised" in the FAQ).
