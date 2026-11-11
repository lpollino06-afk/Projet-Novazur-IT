"""Boîte à outils commune pour générer les pages du site Novazur IT.

Chaque script de page (outils/gen_*.py) fait :  from blocks import *
puis assemble des blocs et appelle write_page().
L'en-tête (menu) et le pied de page sont repris de depannage-informatique-nice.html,
pour rester identiques au reste du site.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://www.novazur-it.com"
TEL = "04 22 13 26 73"
TEL_HREF = "tel:+33422132673"

_tpl = (ROOT / "depannage-informatique-nice.html").read_text()
HEADER = _tpl[_tpl.index("<body>"):_tpl.index('<main id="contenu">')]
FOOTER = _tpl[_tpl.index("</main>") + len("</main>"):]

HERO_SZ = "(min-width: 1160px) 520px, (min-width: 900px) 45vw, 100vw"
SPLIT = "(min-width: 900px) 540px, 100vw"
TALL = "(min-width: 900px) 440px, 100vw"
FULL = "(min-width: 1160px) 1128px, 100vw"
KIND = {"hero": (1200, 900, 600), "tall": (800, 1000, 400), "card": (1200, 675, 600),
        "banner": (1600, 600, 800), "zone": (1400, 620, 900)}

ICONS = {
    "pc": '<rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/>',
    "print": '<path d="M6 9V2h12v7"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/>',
    "wifi": '<path d="M5 12.55a11 11 0 0 1 14.08 0M1.42 9a16 16 0 0 1 21.16 0M8.53 16.11a6 6 0 0 1 6.95 0M12 20h.01"/>',
    "drop": '<path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/>',
    "file": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/>',
    "scan": '<path d="M3 7V5a2 2 0 0 1 2-2h2M17 3h2a2 2 0 0 1 2 2v2M21 17v2a2 2 0 0 1-2 2h-2M7 21H5a2 2 0 0 1-2-2v-2M7 12h10"/>',
    "smartphone": '<rect x="5" y="2" width="14" height="20" rx="2"/><path d="M12 18h.01"/>',
    "alert": '<path d="M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><path d="M12 9v4M12 17h.01"/>',
    "refresh": '<path d="M23 4v6h-6M1 20v-6h6"/><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/>',
    "box": '<path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><path d="M3.27 6.96 12 12.01l8.73-5.05M12 22.08V12"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
    "photo": '<rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="m21 15-5-5L5 21"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
    "trash": '<path d="M3 6h18M19 6l-1 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2L5 6M10 11v6M14 11v6M9 6V4a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2"/>',
    "key": '<circle cx="7.5" cy="15.5" r="5.5"/><path d="m21 2-9.6 9.6M15.5 7.5l3 3L22 7l-3-3"/>',
    "check": '<circle cx="12" cy="12" r="10"/><path d="m8 12 3 3 5-6"/>',
    "users": '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
    "home": '<path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V12h6v10"/>',
    "server": '<rect x="2" y="2" width="20" height="8" rx="2"/><rect x="2" y="14" width="20" height="8" rx="2"/><path d="M6 6h.01M6 18h.01"/>',
    "lock": '<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    "globe": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
    "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>',
    "headset": '<path d="M3 18v-6a9 9 0 0 1 18 0v6"/><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z"/>',
    "map": '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
    "settings": '<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.6 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.6a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/>',
}


def icon(name):
    return ('<div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg></div>')


def photo(name, kind, alt, sizes, lazy=True, style=""):
    w, h, sw = KIND[kind]
    load = 'loading="lazy"' if lazy else 'fetchpriority="high"'
    st = f' style="{style}"' if style else ""
    return (f'<img src="assets/img/{name}.webp" srcset="assets/img/{name}-sm.webp {sw}w, assets/img/{name}.webp {w}w" '
            f'sizes="{sizes}" width="{w}" height="{h}" {load} alt="{alt}"{st}>')


def cta_bg(name):
    return (f'<img class="cta-band__bg" src="assets/img/{name}.webp" srcset="assets/img/{name}-sm.webp 800w, '
            f'assets/img/{name}.webp 1600w" sizes="100vw" width="1600" height="600" loading="lazy" alt="">')


def sec(inner, soft=False, label=None):
    cls = "section section--soft" if soft else "section"
    lab = f' aria-labelledby="{label}"' if label else ""
    return f'\n    <section class="{cls}"{lab}>\n      <div class="container">\n{inner}\n      </div>\n    </section>'


def head_block(hid, title, intro=None, eyebrow=None):
    eb = f'\n          <span class="eyebrow">{eyebrow}</span>' if eyebrow else ""
    p = f"\n          <p>{intro}</p>" if intro else ""
    return f'        <div class="section__head">{eb}\n          <h2 id="{hid}">{title}</h2>{p}\n        </div>'


def lis(items, indent=14):
    return "\n".join(" " * indent + f"<li>{i}</li>" for i in items)


def hero(crumbs, eyebrow, h1, lead, img, buttons=None):
    """crumbs : liste de (lien, texte) ; le dernier est la page courante (lien ignoré)."""
    c = '<li><a href="/">Accueil</a></li>' + "".join(f'<li><a href="{l}">{t}</a></li>' for l, t in crumbs[:-1])
    c += f'<li aria-current="page">{crumbs[-1][1]}</li>'
    buttons = buttons or [(TEL_HREF, "Appeler un technicien", "primary"), ("contact", "Demander un devis", "ghost")]
    btns = "\n          ".join(f'<a class="btn btn--{k}" href="{h}">{t}</a>' for h, t, k in buttons)
    return f'''    <section class="hero hero--page">
      <div class="container hero__grid">
        <div class="hero__intro">
        <nav class="breadcrumb" aria-label="Fil d'Ariane">
          <ol>{c}</ol>
        </nav>
        <span class="eyebrow">{eyebrow}</span>
        <h1>{h1}</h1>
        <p class="hero__lead">{lead}</p>
        <div class="btn-row">
          {btns}
        </div>
        </div>
        <div class="photo-wrap">
          <div class="photo photo--page">
            {img}
          </div>
        </div>
      </div>
    </section>'''


def cards(items, cols=3, with_icons=True):
    out = []
    for it in items:
        t, d = it[0], it[1]
        ic = ("\n            " + icon(it[2])) if with_icons and len(it) > 2 else ""
        out.append(f'          <article class="card">{ic}\n            <h3>{t}</h3>\n            <p>{d}</p>\n          </article>')
    return f'        <div class="grid grid--{cols}">\n' + "\n".join(out) + "\n        </div>"


def service_items(items):
    out = [f'          <div class="service-item">\n            {icon(ic)}\n            <div><h3>{t}</h3><p>{d}</p></div>\n          </div>'
           for t, d, ic in items]
    return '        <div class="grid grid--2">\n' + "\n".join(out) + "\n        </div>"


def feature(eyebrow, hid, title, body, img, reverse=False):
    rev = " feature--reverse" if reverse else ""
    eb = f'\n            <span class="eyebrow">{eyebrow}</span>' if eyebrow else ""
    return f'''        <div class="feature{rev}">
          <div class="feature__media photo">
            {img}
          </div>
          <div class="feature__text">{eb}
            <h2 id="{hid}">{title}</h2>
{body}
          </div>
        </div>'''


def steps_layout(steps, img):
    items = "\n".join(f"          <li><h3>{t}</h3><p>{d}</p></li>" for t, d in steps)
    return f'''        <div class="steps-layout">
          <div class="steps-layout__media photo">
            {img}
          </div>
        <ol class="steps">
{items}
        </ol>
        </div>'''


def steps_row(steps):
    items = "\n".join(f"          <li><h3>{t}</h3><p>{d}</p></li>" for t, d in steps)
    return f'        <ol class="steps">\n{items}\n        </ol>'


def faq_section(title, faq, soft=True, media=None, hid="faq-titre"):
    items = "\n".join(f"          <details>\n            <summary>{q}</summary>\n            <p>{a}</p>\n          </details>" for q, a in faq)
    if media:
        body = f'''        <div class="faq-layout">
          <div class="faq-layout__media photo">
            {media}
          </div>
          <div class="faq">
{items}
          </div>
        </div>'''
    else:
        body = f'        <div class="faq">\n{items}\n        </div>'
    return sec(f'        <div class="section__head"><h2 id="{hid}">{title}</h2></div>\n' + body, soft, hid)


def cta(title, text, bg, buttons=None):
    buttons = buttons or [(TEL_HREF, TEL, "primary"), ("contact", "Écrire un message", "light")]
    btns = "\n            ".join(f'<a class="btn btn--{k}" href="{h}">{t}</a>' for h, t, k in buttons)
    return f'''
    <section class="section">
      <div class="container">
        <div class="cta-band cta-band--photo">
          {cta_bg(bg)}
          <h2>{title}</h2>
          <p>{text}</p>
          <div class="btn-row">
            {btns}
          </div>
        </div>
      </div>
    </section>'''


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s).replace("&nbsp;", " ")


def breadcrumb_ld(crumbs, slug):
    items = [{"@type": "ListItem", "position": 1, "name": "Accueil" if not slug.startswith("it-") else "Home", "item": f"{SITE}/"}]
    for i, (l, t) in enumerate(crumbs, start=2):
        items.append({"@type": "ListItem", "position": i, "name": t, "item": f"{SITE}/{l or slug}"})
    return {"@type": "BreadcrumbList", "itemListElement": items}


def head(meta, graph, faq=None, lang="fr", extra_head=""):
    url = f"{SITE}/{meta['slug']}"
    ld = {"@context": "https://schema.org", "@graph": graph}
    ind = lambda o: "\n".join("  " + l for l in json.dumps(o, ensure_ascii=False, indent=2).splitlines())
    faq_block = ""
    if faq:
        fq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in faq]}
        faq_block = f'\n  <script type="application/ld+json">\n{ind(fq)}\n  </script>'
    locale = "fr_FR" if lang == "fr" else "en_GB"
    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{meta["title"]}</title>
  <meta name="description" content="{meta["desc"]}">
  <link rel="canonical" href="{url}">{extra_head}
  <meta name="theme-color" content="#0a5bd3">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="{locale}">
  <meta property="og:site_name" content="Novazur IT">
  <meta property="og:title" content="{meta["ogTitle"]}">
  <meta property="og:description" content="{meta["ogDesc"]}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{SITE}/assets/img/og-image.jpg?v=2">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Novazur IT – assistance informatique sur la Côte d'Azur">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="assets/img/logo.svg?v=2" type="image/svg+xml">
  <link rel="stylesheet" href="assets/css/style.css?v=3">
  <script type="application/ld+json">
{ind(ld)}
  </script>{faq_block}
</head>
"""


def write_page(slug, head_html, sections, header=None, footer=None):
    body = "\n".join(sections).replace("« ", "«&nbsp;").replace(" »", "&nbsp;»")
    html = head_html + (header or HEADER) + '<main id="contenu">\n' + body + "\n  </main>\n" + (footer or FOOTER)
    (ROOT / f"{slug}.html").write_text(html)
    m = html[html.index("<main"):html.index("</main>")]
    words = len(re.sub(r"<[^>]+>", " ", m).split())
    print(f"écrit {slug}.html — {words} mots")
    return html
