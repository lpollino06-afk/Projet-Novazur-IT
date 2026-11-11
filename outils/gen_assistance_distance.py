#!/usr/bin/env python3
"""Page « Assistance à distance » (téléchargement du module de prise en main).
Usage : python3 outils/gen_assistance_distance.py  (écrit assistance-a-distance.html à la racine du site)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent          # dossier du site
SITE = "https://www.novazur-it.com"
_tpl = (ROOT / "depannage-informatique-nice.html").read_text()
HEADER = _tpl[_tpl.index("<body>"):_tpl.index('<main id="contenu">')]
FOOTER = _tpl[_tpl.index("</main>") + len("</main>"):]
TALL = "(min-width: 900px) 440px, 100vw"
KIND = {"hero": (1200, 900, 600), "tall": (800, 1000, 400), "card": (1200, 675, 600)}
ICONS = {}


def icon(name):
    return ('<div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg></div>')


def photo(name, kind, alt, sizes, lazy=True):
    w, h, sw = KIND[kind]
    load = 'loading="lazy"' if lazy else 'fetchpriority="high"'
    return (f'<img src="assets/img/{name}.webp" srcset="assets/img/{name}-sm.webp {sw}w, assets/img/{name}.webp {w}w" '
            f'sizes="{sizes}" width="{w}" height="{h}" {load} alt="{alt}">')


def cta_bg(name):
    return (f'<img class="cta-band__bg" src="assets/img/{name}.webp" srcset="assets/img/{name}-sm.webp 800w, '
            f'assets/img/{name}.webp 1600w" sizes="100vw" width="1600" height="600" loading="lazy" alt="">')


def sec(inner, soft=False, label=None):
    cls = "section section--soft" if soft else "section"
    lab = f' aria-labelledby="{label}"' if label else ""
    return f"\n    <section class=\"{cls}\"{lab}>\n      <div class=\"container\">\n{inner}\n      </div>\n    </section>"


def head_block(hid, title, intro=None):
    p = f"\n          <p>{intro}</p>" if intro else ""
    return f'        <div class="section__head">\n          <h2 id="{hid}">{title}</h2>{p}\n        </div>'


def strip_tags(s):
    import re
    return re.sub(r"<[^>]+>", "", s).replace("&nbsp;", " ")


def b_faq(p, soft=True):
    items = "\n".join(f"          <details>\n            <summary>{q}</summary>\n            <p>{a}</p>\n          </details>" for q, a in p["faq"])
    return sec(f'        <div class="section__head"><h2 id="faq-titre">{p["faqTitle"]}</h2></div>\n        <div class="faq">\n{items}\n        </div>', soft, "faq-titre")


def head(p, ld):
    url = f"{SITE}/{p['slug']}"
    fq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in p["faq"]]}
    ind = lambda o: "\n".join("  " + l for l in json.dumps(o, ensure_ascii=False, indent=2).splitlines())
    return f"""<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{p["title"]}</title>
  <meta name="description" content="{p["desc"]}">
  <link rel="canonical" href="{url}">
  <meta name="theme-color" content="#0a5bd3">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="fr_FR">
  <meta property="og:site_name" content="Novazur IT">
  <meta property="og:title" content="{p["ogTitle"]}">
  <meta property="og:description" content="{p["ogDesc"]}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{SITE}/assets/img/og-image.jpg?v=2">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Novazur IT – assistance informatique sur la Côte d'Azur">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="assets/img/logo.svg?v=2" type="image/svg+xml">
  <link rel="stylesheet" href="assets/css/style.css?v=2">
  <script type="application/ld+json">
{ind(ld)}
  </script>
  <script type="application/ld+json">
{ind(fq)}
  </script>
</head>
"""


ICONS.update({
    "win": '<rect x="3" y="3" width="8" height="8" rx="1"/><rect x="13" y="3" width="8" height="8" rx="1"/><rect x="3" y="13" width="8" height="8" rx="1"/><rect x="13" y="13" width="8" height="8" rx="1"/>',
    "apple": '<path d="M16 3c0 2-1.5 3.5-3.3 3.6C12.5 4.7 14 3.2 16 3z"/><path d="M19 16.5c-.8 2-2.2 4.5-4 4.5-1.3 0-1.7-.8-3-.8s-1.8.8-3 .8C6.9 21 4 16.6 4 12.8 4 9.6 6 8 8 8c1.3 0 2.2.8 3.2.8S13 8 14.6 8c1.4 0 2.8.7 3.6 2-1.6 1-2.4 2.3-2.4 3.7 0 1.6 1 2.8 3.2 2.8z"/>',
    "lock": '<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    "eye": '<path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/>',
    "power": '<path d="M18.36 6.64a9 9 0 1 1-12.73 0M12 2v10"/>',
    "key": '<circle cx="7.5" cy="15.5" r="5.5"/><path d="m21 2-9.6 9.6M15.5 7.5l3 3L22 7l-3-3"/>',
})

SLUG = "assistance-a-distance"
URL = f"{SITE}/{SLUG}"
p = {
    "slug": SLUG,
    "title": "Assistance informatique à distance | Novazur IT",
    "desc": "Prise en main à distance sécurisée : téléchargez le module Novazur IT, donnez le code à votre technicien et suivez la réparation en direct.",
    "ogTitle": "Assistance informatique à distance | Novazur IT",
    "ogDesc": "Téléchargez le module de prise en main à distance Novazur IT et faites-vous dépanner sans attendre, en toute sécurité.",
    "serviceType": "Assistance informatique à distance",
    "service": "Assistance informatique à distance",
    "faqTitle": "Assistance à distance : vos questions",
    "faq": [
        ("Est-ce sécurisé ?", "Oui. La connexion est chiffrée et ne peut s'ouvrir qu'avec le code que vous nous communiquez. Vous voyez tout ce que nous faisons, et vous pouvez couper la connexion à tout moment en fermant le module."),
        ("Pouvez-vous accéder à mon ordinateur sans moi ?", "Non. Chaque session d'assistance démarre uniquement à votre demande, avec un nouveau code. Une fois la session terminée, nous n'avons plus aucun accès. Seuls les clients entreprises sous contrat de supervision peuvent, s'ils le souhaitent, autoriser un accès permanent encadré."),
        ("Je n'arrive pas à installer le module, que faire ?", "Appelez-nous au 04 22 13 26 73 : nous vous guidons pas à pas par téléphone. Si l'ordinateur ne démarre plus ou n'a pas accès à internet, nous venons chez vous."),
        ("Le module fonctionne-t-il sur Mac ?", "Oui, une version est prévue pour Windows et une pour Mac. Pour les tablettes et smartphones, nous vous guidons par téléphone selon votre appareil."),
        ("Que peut-on régler à distance ?", "La plupart des problèmes logiciels : lenteurs, virus et logiciels indésirables, mises à jour, messagerie, réglages, installation de logiciels, paramétrage d'imprimante. Les pannes matérielles et les installations (box, Wi-Fi) se font sur place."),
        ("Un inconnu m'appelle pour me faire installer un logiciel de prise en main : est-ce vous ?", "Non. Novazur IT ne vous demandera jamais d'installer un logiciel sans que vous nous ayez contactés vous-même. Raccrochez, et en cas de doute, rappelez-nous au 04 22 13 26 73 : c'est très probablement une arnaque."),
    ],
}

ld = {"@context": "https://schema.org", "@graph": [
    {"@type": "Service", "name": p["service"], "serviceType": p["serviceType"], "provider": {"@id": f"{SITE}/#entreprise"},
     "areaServed": {"@type": "Country", "name": "France"}, "availableChannel": {"@type": "ServiceChannel", "name": "Prise en main à distance"}, "url": URL},
    {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Accueil", "item": f"{SITE}/"},
        {"@type": "ListItem", "position": 2, "name": "Assistance à distance", "item": URL}]},
]}
html_head = head(p, ld)

hero = f'''    <section class="hero hero--page">
      <div class="container hero__grid">
        <div class="hero__intro">
        <nav class="breadcrumb" aria-label="Fil d'Ariane">
          <ol><li><a href="/">Accueil</a></li><li aria-current="page">Assistance à distance</li></ol>
        </nav>
        <span class="eyebrow">Télé-assistance</span>
        <h1>Assistance informatique à distance</h1>
        <p class="hero__lead">Pas besoin d'attendre un rendez-vous : avec votre accord, un technicien Novazur IT se connecte à votre ordinateur de façon sécurisée et règle le problème sous vos yeux. Vous suivez tout en direct, et vous gardez la main à chaque instant.</p>
        <div class="btn-row">
          <a class="btn btn--primary" href="#telechargement">Télécharger le module</a>
          <a class="btn btn--ghost" href="tel:+33422132673">04 22 13 26 73</a>
        </div>
        </div>
        <div class="photo-wrap">
          <div class="photo photo--page">
            {photo("assistance-a-distance-domicile-card", "card", "Femme utilisant son ordinateur portable dans son salon", "(min-width: 1160px) 520px, (min-width: 900px) 45vw, 100vw", lazy=False)}
          </div>
        </div>
      </div>
    </section>'''

DISABLED = 'style="opacity:.55;pointer-events:none;cursor:not-allowed" aria-disabled="true"'
download = sec('''        <div class="section__head">
          <span class="eyebrow">Téléchargement</span>
          <h2 id="telechargement">Téléchargez le module de prise en main</h2>
          <p>Téléchargez-le <strong>uniquement si un technicien Novazur IT vous l'a demandé</strong>, puis lancez-le : un code s'affiche, communiquez-le-nous par téléphone.</p>
        </div>
        <div class="grid grid--2">
          <article class="card" style="text-align:center">
            ''' + icon("win") + '''
            <h3>Pour Windows</h3>
            <p>Windows 10 et 11. Aucune installation complexe : il suffit de lancer le fichier téléchargé.</p>
            <!-- Mettre ici le lien de téléchargement Windows de l'outil (AnyDesk, RustDesk, TeamViewer QuickSupport…) et retirer le style « désactivé » -->
            <a class="btn btn--primary" href="#" ''' + DISABLED + '''>Bientôt disponible</a>
          </article>
          <article class="card" style="text-align:center">
            ''' + icon("apple") + '''
            <h3>Pour Mac</h3>
            <p>macOS récent. À la première ouverture, nous vous guidons pour autoriser le partage d'écran.</p>
            <!-- Mettre ici le lien de téléchargement Mac de l'outil et retirer le style « désactivé » -->
            <a class="btn btn--primary" href="#" ''' + DISABLED + '''>Bientôt disponible</a>
          </article>
        </div>
        <div class="highlight mt-lg">
          <strong>Le module n'est pas encore en ligne.</strong> En attendant, appelez-nous au <a href="tel:+33422132673">04 22 13 26 73</a> : nous vous indiquons par téléphone comment ouvrir la session d'assistance.
        </div>''', soft=True, label="telechargement")

steps = sec(head_block("etapes-titre", "Comment se déroule une session", "Quelques minutes suffisent pour démarrer.") + '''
        <div class="steps-layout">
          <div class="steps-layout__media photo">
            ''' + photo("support-informatique-telephone-tall", "tall", "Technicien du support informatique souriant avec son casque", TALL) + '''
          </div>
        <ol class="steps">
          <li><h3>Vous nous appelez</h3><p>Vous nous décrivez le problème au 04 22 13 26 73 ou via le formulaire de contact.</p></li>
          <li><h3>Vous lancez le module</h3><p>Vous téléchargez le module sur cette page et l'ouvrez. Un code à usage unique s'affiche.</p></li>
          <li><h3>Vous nous donnez le code</h3><p>Vous nous le lisez au téléphone et acceptez la connexion : nous voyons alors votre écran.</p></li>
          <li><h3>Nous réglons le problème</h3><p>Vous suivez tout en direct et pouvez poser vos questions. À la fin, vous fermez le module : la connexion est coupée.</p></li>
        </ol>
        </div>''', soft=False, label="etapes-titre")

items = "\n".join('          <div class="service-item">\n            ' + icon(ic) + '\n            <div><h3>' + t + '</h3><p>' + d + '</p></div>\n          </div>' for t, d, ic in [
    ("Connexion chiffrée", "Les échanges entre votre ordinateur et le nôtre sont chiffrés de bout en bout.", "lock"),
    ("Uniquement à votre demande", "La session ne peut démarrer qu'avec le code que vous nous donnez. Aucun accès permanent.", "key"),
    ("Vous voyez tout", "Chaque action s'affiche sur votre écran. Nous vous expliquons ce que nous faisons.", "eye"),
    ("Vous pouvez couper à tout moment", "Il suffit de fermer le module pour mettre fin à la connexion immédiatement.", "power"),
])
securite = sec(head_block("securite-titre", "Votre sécurité avant tout", "La prise en main à distance repose sur la confiance : voici nos garanties.") + '\n        <div class="grid grid--2">\n' + items + '''
        </div>
        <div class="highlight mt-lg">
          <strong>Attention aux arnaques.</strong> Novazur IT ne vous appellera jamais pour vous demander d'installer un logiciel si vous ne nous avez pas contactés. Vérifiez toujours que vous êtes bien sur <strong>novazur-it.com</strong> avant de télécharger quoi que ce soit. <a href="suppression-virus-arnaque">En savoir plus sur les arnaques au faux support</a>.
        </div>''', soft=True, label="securite-titre")

quoi = sec('''        <div class="split">
          <div class="panel">
            <h3>Ce que nous réglons à distance</h3>
            <ul class="check-list">
              <li>Ordinateur lent, logiciels qui plantent</li>
              <li>Virus, pop-ups et logiciels indésirables</li>
              <li>Mises à jour, Windows 11</li>
              <li>Messagerie, Microsoft 365, comptes</li>
              <li>Installation et réglage de logiciels</li>
              <li>Paramétrage d'imprimante</li>
            </ul>
          </div>
          <div class="panel">
            <h3>Ce qui demande un déplacement</h3>
            <ul class="check-list">
              <li>Ordinateur qui ne démarre plus du tout</li>
              <li>Pas d'accès à internet</li>
              <li>Installation de box et de Wi-Fi</li>
              <li>Remplacement de pièces (SSD, mémoire)</li>
              <li>Récupération de données sur un disque abîmé</li>
            </ul>
            <a class="btn btn--secondary" href="zone-intervention">Voir notre zone d'intervention</a>
          </div>
        </div>''', soft=False, label=None)

cta = f'''
    <section class="section">
      <div class="container">
        <div class="cta-band cta-band--photo">
          {cta_bg("helpdesk-entreprise-equipe-banner")}
          <h2>Besoin d'une assistance maintenant&nbsp;?</h2>
          <p>Appelez-nous : nous ouvrons une session à distance dès qu'un technicien est disponible.</p>
          <div class="btn-row">
            <a class="btn btn--primary" href="tel:+33422132673">04 22 13 26 73</a>
            <a class="btn btn--light" href="contact">Écrire un message</a>
          </div>
        </div>
      </div>
    </section>'''

body = "\n".join([hero, download, steps, securite, quoi, b_faq(p, soft=True), cta]).replace("« ", "«&nbsp;").replace(" »", "&nbsp;»")
(ROOT / f"{SLUG}.html").write_text(html_head + HEADER + '<main id="contenu">\n' + body + "\n  </main>\n" + FOOTER)
print("écrit", SLUG, len(p["title"]), len(p["desc"]))
