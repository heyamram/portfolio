# heyamram.com — Portfolio Site

Built with FastAPI + Jinja2 templates + plain CSS. No frontend framework —
on purpose, so you're getting more reps with the stack you're already
learning instead of adding a new one just for this.

## Run it locally

```
pip install -r requirements.txt --break-system-packages
uvicorn main:app --reload
```

Then open http://127.0.0.1:8000

## What's built vs. what's yours to build

**Done for you (as a pattern to learn from):**
- Home (`/`)
- About (`/about`)
- The nav, shared layout, and CSS — reuse this for every page

**Left for you — same steps each time:**
- `/skills`, `/projects`, `/blog`, `/contact`, `/resume`
- For each one: copy `templates/about.html`, rename it, change the
  content, add a matching route in `main.py` (the pattern is commented
  at the bottom of that file), run it locally, then deploy.

That's five more reps of the same loop: skim what you need, build the
page, deploy it, move to the next one.

## CSS quick reference

Every color and the max content width live in the `:root { }` block at
the very top of `static/style.css` as CSS variables (`--accent-1`,
`--bg`, etc.). Change a value there and it updates everywhere it's
used — that's the one concept worth understanding first. Everything
else in the file is flexbox layout, which is easiest to pick up by
reading the CSS next to the rendered page and changing one value at a
time to see what moves.

## Deploying

Render or Railway both have a free tier that works well with FastAPI —
connect your GitHub repo and they detect `requirements.txt` and
`main.py` automatically. Point your existing heyamram.com domain at
whichever one you pick once it's live. If your current site is on
something else entirely (a static host, a no-code builder), let me
know what it's on and I'll adjust this.
