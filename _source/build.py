#!/usr/bin/env python3
"""Generate four multi-page portfolio sites (gravity, swiss, canvas, fluid) into dist/."""
import html, os, shutil, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import *

SRC = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.dirname(SRC)  # repo root
e = html.escape

THEMES = {
    "gravity": dict(
        label="Gravity",
        fonts="family=Gabarito:wght@400..900&family=DM+Sans:opsz,wght@9..40,400..700",
        theme_color="#d6f2e4",
        brand='<span class="mono" aria-hidden="true">RB</span><span>Ricky Brockamp</span>',
    ),
    "swiss": dict(
        label="Swiss",
        fonts="family=Archivo:ital,wdth,wght@0,62..125,100..900;1,62..125,100..900",
        theme_color="#f2ede4",
        pre='<div class="guides" aria-hidden="true">'+'<i></i>'*12+'</div>',
        brand='<svg viewBox="0 0 22 22" width="22" height="22" aria-hidden="true"><rect width="22" height="22" fill="#18223f"/><path d="M0 22A22 22 0 0 1 22 0V22Z" fill="#e3321f"/><circle cx="16" cy="16" r="4" fill="#f4b223"/></svg><span>Ricky Brockamp</span>',
    ),
    "canvas": dict(
        label="Canvas",
        fonts="family=Anybody:ital,wdth,wght@0,50..150,100..900&family=Inter+Tight:wght@400;500;600;700",
        theme_color="#e9edf3",
        brand='<span class="mono" aria-hidden="true">RB</span><span class="file"><b>Ricky Brockamp</b><span>Portfolio — Product Designer</span></span>',
    ),
    "fluid": dict(
        label="Fluid",
        fonts="family=Big+Shoulders+Display:wght@500..900&family=Familjen+Grotesk:wght@400..700",
        theme_color="#f8eddc",
        brand='<i class="dot" aria-hidden="true"></i><span>Ricky Brockamp</span>',
    ),
}

NAV = [("work", "Work", "index.html#work"), ("about", "About", "about.html"), ("process", "Process", "process.html"),
       ("photo", "Photo", "photo.html"), ("resume", "Resume", "resume.html")]


def head(t, title, desc, root, extra=""):
    T = THEMES[t]
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="theme-color" content="{T['theme_color']}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{root}assets/ricky.jpg">
<link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?{T['fonts']}&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}base.css">
<link rel="stylesheet" href="{root}theme.css">
{extra}</head>"""


def header(t, root, current, home=False):
    T = THEMES[t]
    items = []
    for key, label, href in NAV:
        h = ("#work" if home and key == "work" else root + href)
        cur = ' aria-current="page"' if key == current else ""
        items.append(f'<li><a href="{h}"{cur}>{label}</a></li>')
    return T.get("pre", "") + f"""<a class="skip" href="#main">Skip to main content</a>
<header class="site-header">
 <div class="wrap">
  <a class="brand" href="{root}index.html"{' aria-current="page"' if home else ''}>{T['brand']}<span class="sr-only">, home</span></a>
  <nav class="site-nav" aria-label="Primary"><ul>{''.join(items)}</ul></nav>
  <a class="btn btn-sm header-cta" href="mailto:{EMAIL}">Get in touch</a>
 </div>
</header>"""


def footer(t, root):
    return f"""<footer class="site-footer">
 <div class="wrap">
  <div class="foot-id"><p class="foot-name">{NAME}</p><p>{ROLE} · {LOCATION}</p></div>
  <nav aria-label="Footer"><ul>
   <li><a href="{root}index.html#work">Work</a></li><li><a href="{root}about.html">About</a></li><li><a href="{root}process.html">Process</a></li><li><a href="{root}photo.html">Photo</a></li><li><a href="{root}resume.html">Resume</a></li>
  </ul></nav>
  <ul aria-label="Contact">
   <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
   <li><a href="{LINKEDIN}" rel="me">LinkedIn<span class="sr-only"> (opens LinkedIn)</span></a></li>
  </ul>
  <p class="foot-small">© 2026 {NAME}</p>
 </div>
</footer>"""


def frame(t, label, inner, cls=""):
    """Canvas wraps sections in labelled 'frames'; other themes pass through."""
    if t == "canvas":
        return f'<div class="frame {cls}"><span class="frame-label" aria-hidden="true">{e(label)}</span>{inner}</div>'
    return inner


# ---------------- shared sections ----------------
def work_section(t, root, h="h2"):
    cards = []
    for c in CASES:
        cards.append(f"""<li class="card case-card" data-case="{c['slug']}">
  <div class="card-media"><img src="{root}assets/{c['img']}" alt="" width="1232" height="818" loading="lazy"></div>
  <div class="card-body">
   <p class="card-kicker"><span class="num">{c['n']}</span> <span>{e(c['kicker'])}</span></p>
   <h3 class="card-title"><a class="stretch" href="{root}work/{c['slug']}.html">{e(c['title'])}</a></h3>
   <p class="card-text">{e(c['summary'])}</p>
  </div>
 </li>""")
    inner = f"""<div class="section-head"><{h} class="section-title" id="work-title">Selected work</{h}><p class="section-note">Four projects, 2020–2026</p></div>
 <ul class="cards" role="list">{''.join(cards)}</ul>"""
    return f'<section class="section work-section" id="work" aria-labelledby="work-title"><div class="wrap">{frame(t, "Selected work · 01—04", inner)}</div></section>'


def quotes_section(t):
    qs = []
    for i, q in enumerate(TESTIMONIALS):
        body = "".join(f"<p>{e(p)}</p>" for p in q["quote"])
        qs.append(f'<figure class="quote{" wide" if i == 0 else ""}"><blockquote>{body}</blockquote><figcaption><b>{e(q["name"])}</b>{e(q["role"])}</figcaption></figure>')
    inner = f'<div class="section-head"><h2 class="section-title" id="kind-words">Kind words</h2></div><div class="quotes">{"".join(qs)}</div>'
    return f'<section class="section quotes-section" aria-labelledby="kind-words"><div class="wrap">{frame(t, "Testimonials", inner)}</div></section>'


def process_teaser(t, root):
    steps = "".join(f'<li><span class="num">{p["n"]}</span> {e(p["title"])}</li>' for p in PROCESS)
    inner = f"""<div class="teaser">
  <div><h2 class="section-title" id="how">How I work</h2><p class="lede">Active listening first, then research, collaboration, iteration and measurement, with accessibility built in from the start.</p>
  <p class="btn-row" style="margin-top:24px"><a class="btn btn-primary" href="{root}process.html">See the full process</a></p></div>
  <ol class="steps" role="list">{steps}</ol>
 </div>"""
    return f'<section class="section process-teaser" aria-labelledby="how"><div class="wrap">{frame(t, "Process — overview", inner)}</div></section>'


def contact_section(t, root):
    inner = f"""<div class="contact">
  <h2 class="section-title" id="contact-title">Let’s talk</h2>
  <p class="lede">I’m always happy to talk about design systems, accessibility, AI in design, or a role where I can help.</p>
  <p class="btn-row"><a class="btn btn-primary" href="mailto:{EMAIL}">Email {EMAIL}</a><a class="btn btn-ghost" href="{root}resume.html">View resume</a></p>
 </div>"""
    return f'<section class="section contact-section" id="contact" aria-labelledby="contact-title"><div class="wrap">{frame(t, "Contact", inner)}</div></section>'


def page(t, root, current, title, desc, main_html, body_cls=""):
    return f"""{head(t, title, desc, root)}
<body class="{body_cls}">
{header(t, root, current)}
<main id="main" tabindex="-1">
{main_html}
</main>
{footer(t, root)}
</body>
</html>
"""


def page_head(t, eyebrow, h1, lede=None):
    l = f'<p class="lede">{lede}</p>' if lede else ""
    inner = f'<p class="eyebrow">{eyebrow}</p><h1 class="page-title">{h1}</h1>{l}'
    return f'<section class="page-head"><div class="wrap">{frame(t, "Header", inner, "head-frame")}</div></section>'


# ---------------- pages ----------------
def about(t):
    r = ""
    bio = "".join(f"<p>{e(p)}</p>" for p in BIO)
    strip = "".join(f'<li><img src="{r}assets/photo/{f}" alt="{e(a)}" loading="lazy"></li>' for f, a, _ in [PHOTOS[0], PHOTOS[1], PHOTOS[6]])
    inner = f"""<div class="about-grid">
  <figure class="portrait"><img src="assets/ricky.jpg" alt="Ricky Brockamp standing on a gravel garden path in a rain jacket and cap, smiling, beside a shingled cottage." width="760" height="866"></figure>
  <div class="prose">{bio}
   <h2 class="sub-title">Outside of work</h2><p>{e(OUTSIDE)}</p>
   <h2 class="sub-title">Focus</h2>
   <ul class="tags" role="list">{''.join(f'<li class="chip">{e(f)}</li>' for f in FOCUS)}</ul>
   <p class="btn-row" style="margin-top:32px"><a class="btn btn-primary" href="mailto:{EMAIL}">Get in touch</a><a class="btn btn-ghost" href="resume.html">Resume</a></p>
  </div>
 </div>"""
    main = page_head(t, "About", NAME, e(TAGLINE)) + f'<section class="section about-section" aria-label="Biography"><div class="wrap">{frame(t, "About / Bio", inner)}</div></section>' \
        + f'<section class="section strip-section" aria-labelledby="strip-title"><div class="wrap">{frame(t, "Photo — selects", f"<div class=section-head><h2 class=section-title id=strip-title>Through the lens</h2><a class=more-link href=photo.html>All photos</a></div><ul class=strip role=list>{strip}</ul>")}</div></section>'
    return page(t, "", "about", f"About — {NAME}", f"About {NAME}, a product designer and design lead in Los Angeles.", main)


def process(t):
    items = []
    for p in PROCESS:
        txt = "".join(f"<p>{e(x)}</p>" for x in p["text"])
        meth = "".join(f'<li class="chip">{e(m)}</li>' for m in p["methods"])
        items.append(f"""<li class="phase">
  <div class="phase-head"><span class="phase-num" aria-hidden="true">{p['n']}</span><h2 class="phase-title"><span class="sr-only">Step {int(p['n'])}: </span>{e(p['title'])}</h2></div>
  <div class="phase-body prose">{txt}<h3 class="sr-only">Methods</h3><ul class="tags" role="list" aria-label="Methods">{meth}</ul></div>
 </li>""")
    inner = f'<ol class="phases" role="list">{"".join(items)}</ol>'
    main = page_head(t, "Process", "My UX/UI design process", "Five phases, from active listening to measuring success. Each one is iterative, collaborative and grounded in what users actually need.") \
        + f'<section class="section" aria-label="Process phases"><div class="wrap">{frame(t, "Process — 5 phases", inner)}</div></section>'
    return page(t, "", "process", f"Process — {NAME}", "Ricky Brockamp’s UX and UI design process, from discovery to measuring success.", main)


def photo(t):
    figs = "".join(f'<figure class="shot {o}"><img src="assets/photo/{f}" alt="{e(a)}" loading="lazy"></figure>' for f, a, o in PHOTOS)
    inner = f'<div class="gallery">{figs}</div>'
    main = page_head(t, "Photo", "Photography", e(PHOTO_INTRO)) + f'<section class="section gallery-section" aria-label="Photo gallery"><div class="wrap">{frame(t, "Photo — film + digital", inner)}</div></section>'
    return page(t, "", "photo", f"Photography — {NAME}", "Film and digital photography by Ricky Brockamp.", main)


def resume(t):
    jobs = "".join(f"""<article class="job"><header><h3 class="job-title">{e(j['title'])}, <span>{e(j['org'])}</span></h3><p class="job-dates">{e(j['dates'])}</p></header><ul>{''.join(f'<li>{e(b)}</li>' for b in j['bullets'])}</ul></article>""" for j in JOBS)
    edu = "".join(f'<li><b>{e(a)}</b><br>{e(b)} · {c}</li>' for a, b, c in EDUCATION)
    inner = f"""<div class="resume-grid">
  <div><h2 class="sub-title" id="exp">Experience</h2>{jobs}</div>
  <div class="resume-side">
   <h2 class="sub-title">Contact</h2><ul class="plain" role="list"><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="{LINKEDIN}">linkedin.com/in/rickybrockamp</a></li><li>{LOCATION}</li></ul>
   <h2 class="sub-title">Education</h2><ul class="plain" role="list">{edu}</ul>
   <h2 class="sub-title">Skills</h2><ul class="tags" role="list">{''.join(f'<li class="chip">{e(s)}</li>' for s in SKILLS)}</ul>
   <h2 class="sub-title">Tools</h2><ul class="tags" role="list">{''.join(f'<li class="chip">{e(s)}</li>' for s in TOOLS)}</ul>
  </div>
 </div>
 <p class="btn-row no-print" style="margin-top:40px"><button class="btn btn-primary" type="button" onclick="window.print()">Print or save as PDF</button><a class="btn btn-ghost" href="mailto:{EMAIL}">Email me</a></p>"""
    main = page_head(t, "Resume", NAME, e(RESUME_SUMMARY)) + f'<section class="section" aria-label="Resume details"><div class="wrap">{frame(t, "Resume — 2026", inner)}</div></section>'
    return page(t, "", "resume", f"Resume — {NAME}", "Resume for Ricky Brockamp, product designer and design lead.", main)


def case(t, i):
    c = CASES[i]
    root = "../"
    prev, nxt = CASES[i - 1], CASES[(i + 1) % len(CASES)]
    ov = "".join(f"<p>{e(p)}</p>" for p in c["overview"])
    did = "".join(f'<li class="did-item"><h3>{e(a)}</h3><p>{e(b)}</p></li>' for a, b in c["did"])
    svc = "".join(f'<li class="chip">{e(s)}</li>' for s in c["services"])
    head_inner = f"""<p class="eyebrow"><span class="num">{c['n']}</span> {e(c['kicker'])}</p><h1 class="page-title">{e(c['title'])}</h1><p class="lede">{e(c['summary'])}</p>"""
    main = f"""<section class="page-head case-head"><div class="wrap">{frame(t, f"Case {c['n']} / Header", head_inner, "head-frame")}</div></section>
<section class="case-hero-section"><div class="wrap">{frame(t, f"{c['short']} / Hero image", f'<figure class="case-hero"><img src="{root}assets/{c["img"]}" alt="{e(c["alt"])}" width="1232" height="818"></figure>')}</div></section>
<section class="section" aria-labelledby="ov"><div class="wrap">{frame(t, "Overview", f'''<div class="case-cols">
  <div class="prose"><h2 class="section-title" id="ov">Overview</h2>{ov}</div>
  <dl class="case-meta">
   <div><dt>Client</dt><dd>{e(c['client'])}</dd></div>
   <div><dt>Role</dt><dd>Product designer, design lead</dd></div>
   <div><dt>Focus</dt><dd><ul class="tags" role="list">{svc}</ul></dd></div>
  </dl>
 </div>''')}</div></section>
<section class="section did-section" aria-labelledby="did"><div class="wrap">{frame(t, "What I did", f'<h2 class="section-title" id="did">What I did</h2><ul class="did" role="list">{did}</ul>')}</div></section>
<section class="section nda-section" aria-labelledby="nda"><div class="wrap">{frame(t, "Note", f'''<div class="nda"><h2 class="sub-title" id="nda">Want the full story?</h2><p>The detailed case study includes client work I can’t publish openly. I’m glad to walk you through it, including the research, flows and outcomes.</p><p class="btn-row"><a class="btn btn-primary" href="mailto:{EMAIL}?subject={e(c['title'])}%20case%20study">Request a walkthrough</a></p></div>''')}</div></section>
<nav class="section pager-section" aria-label="More case studies"><div class="wrap"><div class="pager">
 <a href="{prev['slug']}.html" rel="prev"><span class="pager-label">Previous case</span><span class="pager-title">{e(prev['title'])}</span></a>
 <a href="{nxt['slug']}.html" rel="next"><span class="pager-label">Next case</span><span class="pager-title">{e(nxt['title'])}</span></a>
</div></div></nav>"""
    return page(t, root, "work", f"{c['title']} — {NAME}", f"{c['title']}: {c['summary']}", main, "case-page")


def home(t):
    tpl = open(os.path.join(SRC, "themes", t, "home.html"), encoding="utf-8").read()
    rep = {
        "{{HEAD}}": head(t, f"{NAME} — Product Designer", f"{NAME} is a product designer and design lead in Los Angeles. {TAGLINE}", "",
                         '<link rel="stylesheet" href="home.css">\n'),
        "{{HEADER}}": header(t, "", None, home=True),
        "{{FOOTER}}": footer(t, ""),
        "{{WORK}}": work_section(t, ""),
        "{{QUOTES}}": quotes_section(t),
        "{{PROCESS}}": process_teaser(t, ""),
        "{{CONTACT}}": contact_section(t, ""),
        "{{EMAIL}}": EMAIL, "{{TAGLINE}}": TAGLINE, "{{ROLE}}": ROLE, "{{LOCATION}}": LOCATION,
    }
    for k, v in rep.items():
        tpl = tpl.replace(k, v)
    return tpl


FAVICON = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#1a2030"/><text x="32" y="42" font-family="Arial,sans-serif" font-size="26" font-weight="800" fill="#fff" text-anchor="middle">RB</text></svg>'


def build(t):
    out = os.path.join(DIST, t)
    if os.path.exists(out):
        shutil.rmtree(out)
    os.makedirs(os.path.join(out, "work"))
    shutil.copytree(os.path.join(SRC, "assets"), os.path.join(out, "assets"))
    open(os.path.join(out, "assets", "favicon.svg"), "w").write(FAVICON)
    shutil.copy(os.path.join(SRC, "base.css"), out)
    for f in os.listdir(os.path.join(SRC, "themes", t)):
        if f != "home.html":
            shutil.copy(os.path.join(SRC, "themes", t, f), out)
    pages = {"index.html": home(t), "about.html": about(t), "process.html": process(t), "photo.html": photo(t), "resume.html": resume(t)}
    for i, c in enumerate(CASES):
        pages[f"work/{c['slug']}.html"] = case(t, i)
    if t == "canvas":
        pages["overview.html"] = canvas_overview()
    for p, s in pages.items():
        open(os.path.join(out, p), "w", encoding="utf-8").write(s)
    return sorted(pages)


def canvas_overview():
    """Accessible, linear 'list view' of the canvas home page."""
    t = "canvas"
    inner = f'<p class="eyebrow">{ROLE} · {LOCATION}</p><h1 class="page-title">{NAME}</h1><p class="lede">{e(TAGLINE)}</p><ul class="tags" role="list" style="margin-top:20px">{"".join(f"<li class=chip>{e(f)}</li>" for f in FOCUS)}</ul><p class="btn-row" style="margin-top:28px"><a class="btn btn-primary" href="mailto:{EMAIL}">Get in touch</a><a class="btn btn-ghost" href="index.html">Open the interactive canvas</a></p>'
    main = f'<section class="page-head"><div class="wrap">{frame(t, "Hero / List view", inner, "head-frame")}</div></section>' + work_section(t, "") + quotes_section(t) + process_teaser(t, "") + contact_section(t, "")
    return page(t, "", None, f"{NAME} — Product Designer (list view)", f"{NAME}, product designer. A linear, screen-reader-friendly view of the portfolio home.", main)


if __name__ == "__main__":
    for t in (sys.argv[1:] or THEMES):
        print(t, build(t))
