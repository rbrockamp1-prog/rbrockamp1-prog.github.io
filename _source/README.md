# Source for the four portfolio sites

Jekyll ignores folders that start with `_`, so nothing in this folder is published.

- `content.py`: all copy (bio, case studies, testimonials, process, resume). Edit text here.
- `base.css`: shared structure and accessibility layer used by every site.
- `themes/<site>/theme.css`: that site's look for inner pages.
- `themes/<site>/home.html` + `home.css`: that site's interactive home page.
- `assets/`: portrait, project images, photography.
- `build.py`: regenerates `gravity/`, `swiss/`, `canvas/`, `fluid/` at the repo root.

## Rebuild
```
cd _source
python3 build.py            # all four
python3 build.py swiss      # just one
```
Then commit the changed site folders.

`axe.js` / `shot.js` are the Playwright helpers used for accessibility audits and screenshots (need `npm i axe-core` and Playwright).
