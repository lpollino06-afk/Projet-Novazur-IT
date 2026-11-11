#!/usr/bin/env python3
"""Page en anglais : IT support on the French Riviera & Monaco.  Usage : python3 outils/gen_english.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from blocks import *  # noqa

SLUG = "it-support-french-riviera-monaco"
URL = f"{SITE}/{SLUG}"
TEL_INT = "+33 4 22 13 26 73"

PHONE_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
             + ICONS["phone"] + '</svg>')

HEADER_EN = f'''<body>
  <a class="skip-link" href="#contenu">Skip to content</a>

  <header class="site-header">
    <div class="container site-header__inner">
      <a class="logo" href="{SLUG}" aria-label="Novazur IT – English page">
        <img src="assets/img/logo.svg?v=2" alt="" width="36" height="36">
        <span>Novazur <b>IT</b></span>
      </a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="main-nav" aria-label="Open menu">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
      </button>
      <nav id="main-nav" class="main-nav" aria-label="Main navigation">
        <ul>
          <li><a href="#services">Services</a></li>
          <li><a href="#second-homes">Second homes</a></li>
          <li><a href="#businesses">Businesses</a></li>
          <li><a href="#area">Area</a></li>
          <li><a href="#faq-titre">FAQ</a></li>
          <li><a href="/" lang="fr" hreflang="fr">Français</a></li>
        </ul>
        <a class="btn btn--primary" href="{TEL_HREF}">
          {PHONE_SVG}
          {TEL_INT}
        </a>
      </nav>
    </div>
  </header>

'''

FOOTER_EN = f'''  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid" style="grid-template-columns:repeat(auto-fit,minmax(200px,1fr))">
        <div>
          <a class="logo" href="{SLUG}"><img src="assets/img/logo.svg?v=2" alt="" width="36" height="36"><span>Novazur <b>IT</b></span></a>
          <p>IT support for homes and businesses on the French Riviera and in Monaco. English &amp; French spoken.</p>
          <address style="font-style:normal">
            Novazur IT<br>
            219 boulevard du Mont Boron<br>
            06300 Nice, France
          </address>
        </div>
        <div>
          <h2>Services</h2>
          <ul>
            <li><a href="#services">Home IT support</a></li>
            <li><a href="#second-homes">Second-home care</a></li>
            <li><a href="#businesses">Business IT</a></li>
            <li><a href="assistance-a-distance" lang="fr">Remote support (in French)</a></li>
          </ul>
        </div>
        <div>
          <h2>Contact</h2>
          <ul>
            <li><a href="{TEL_HREF}">{TEL_INT}</a></li>
            <li><a href="mailto:contact@novazur-it.com">contact@novazur-it.com</a></li>
            <li>Mon – Fri: 8:30am – 7pm</li>
            <li>Saturday: 9am – 1pm</li>
          </ul>
        </div>
        <div>
          <h2>Français</h2>
          <ul>
            <li><a href="/" lang="fr" hreflang="fr">Site en français</a></li>
            <li><a href="depannage-informatique-monaco" lang="fr">Informatique Monaco</a></li>
            <li><a href="zone-intervention" lang="fr">Zone d'intervention</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>© <span id="year">2026</span> Novazur IT – All rights reserved</span>
        <a href="mentions-legales" lang="fr">Legal notice &amp; privacy (in French)</a>
      </div>
    </div>
  </footer>

  <div class="mobile-cta">
    <a class="btn btn--primary" href="{TEL_HREF}">Call</a>
    <a class="btn btn--secondary" href="mailto:contact@novazur-it.com">Email us</a>
  </div>

  <script src="assets/js/main.js?v=2" defer></script>
  <script src="assets/js/stats.js?v=1" defer></script>
</body>
</html>
'''

faq = [
    ("Do you really speak English?", "Yes. You can call us, write to us and be helped on site entirely in English, from the first call to the end of the visit. We also speak French, which helps when dealing with local providers."),
    ("Do you work in Monaco?", "Yes. Monaco is part of our main service area, together with Menton, Cap-d'Ail, Beaulieu, Villefranche, Nice, Antibes and Cannes. We regularly visit homes and offices from Monte-Carlo to Fontvieille."),
    ("Can you help while I'm abroad?", "Yes. Most software issues can be solved remotely, wherever you are. For your Riviera home, we can check the internet box, Wi-Fi, TV and cameras before you arrive, and coordinate with your caretaker or concierge."),
    ("Can you deal with French internet providers for me?", "We can help you understand your contract, report a fault to your internet provider and set up the equipment they send, so you don't have to struggle with French helplines."),
    ("Do you support businesses?", "Yes: IT maintenance and helpdesk, cybersecurity, Microsoft 365, backups and VoIP phone systems for small and medium-sized companies, including Monaco-based businesses and international teams in Sophia Antipolis."),
    ("Is my data kept confidential?", "Absolutely. We only access what is needed to fix the issue, always with your consent, and we never keep copies of your data."),
]
meta = {"slug": SLUG, "title": "IT Support on the French Riviera & Monaco | Novazur IT",
        "desc": "English-speaking IT support in Nice, Monaco, Cannes and Antibes: computer repair, Wi-Fi, cybersecurity and IT maintenance for homes and businesses.",
        "ogTitle": "English-speaking IT support on the French Riviera & Monaco | Novazur IT",
        "ogDesc": "Computer repair, Wi-Fi, second-home care and business IT, in English, from Menton to Cannes and across Monaco."}
graph = [
    {"@type": "Service", "name": "English-speaking IT support on the French Riviera and in Monaco", "serviceType": "IT support",
     "provider": {"@id": f"{SITE}/#entreprise"}, "availableLanguage": ["en", "fr"], "inLanguage": "en",
     "areaServed": [{"@type": "Country", "name": "Monaco"}, {"@type": "AdministrativeArea", "name": "Alpes-Maritimes"}], "url": URL},
    {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
        {"@type": "ListItem", "position": 2, "name": "IT support in English", "item": URL}]},
]
extra = f'\n  <link rel="alternate" hreflang="en" href="{URL}">\n  <link rel="alternate" hreflang="fr" href="{SITE}/">'
h = head(meta, graph, faq, lang="en", extra_head=extra)

hero_html = f'''    <section class="hero hero--page">
      <div class="container hero__grid">
        <div class="hero__intro">
        <span class="eyebrow">English &amp; French spoken</span>
        <h1>English-speaking IT support on the French Riviera &amp; Monaco</h1>
        <p class="hero__lead">Based in Nice, Novazur IT helps residents, second-home owners and businesses from Menton to Cannes and across Monaco, in English or in French. Home and office visits, or remote support, usually the same day.</p>
        <div class="btn-row">
          <a class="btn btn--primary" href="{TEL_HREF}">Call {TEL_INT}</a>
          <a class="btn btn--ghost" href="mailto:contact@novazur-it.com">Email us</a>
        </div>
        </div>
        <div class="photo-wrap">
          <div class="photo photo--page">
            {photo("riviera-monaco-aerial-hero", "hero", "View over the harbour of Monaco and the Riviera coastline", HERO_SZ, lazy=False)}
          </div>
        </div>
      </div>
    </section>'''

stats = '''
    <section class="stats" aria-label="Our commitments">
      <div class="container">
        <ul>
          <li><strong class="stat__num">EN · FR</strong><span class="stat__label">English and French spoken</span></li>
          <li><strong class="stat__num">5 min</strong><span class="stat__label">to start a remote session</span></li>
          <li><strong class="stat__num">6 days</strong><span class="stat__label">a week, Monday to Saturday</span></li>
          <li><strong class="stat__num">Monaco</strong><span class="stat__label">and the whole Riviera coast</span></li>
        </ul>
      </div>
    </section>'''

services = sec(head_block("services", "IT help at home", "PC or Mac, phone, tablet or printer: we fix it, set it up and explain it, in plain English.", "For residents") + "\n" + cards([
    ("Computer repair", "Slow or crashing PC or Mac, failed updates, Windows 11 upgrade, SSD upgrade.", "pc"),
    ("Wi-Fi &amp; internet", "Internet box set-up (Monaco Telecom and French providers), Wi-Fi in every room and on the terrace.", "wifi"),
    ("Viruses &amp; scams", "Virus removal, fake tech-support scams, hacked email or social media accounts.", "shield"),
    ("Data recovery &amp; backups", "Lost photos and files recovered when possible, automatic backups set up.", "photo"),
    ("New computer set-up", "Buying advice, set-up and transfer of your files, emails and accounts.", "box"),
    ("Printers &amp; devices", "Printers, scanners, smart TVs and connected devices installed and working together.", "print"),
], cols=3), soft=False, label="services")

second = feature("Second homes", "second-homes", "Your Riviera home, ready when you arrive",
                 f'''            <p>Many of our clients spend only part of the year on the Côte d'Azur. Between two stays, an internet box that updates itself, a Wi-Fi network that drops or a TV that loses its channels is enough to spoil an arrival.</p>
            <p>We take care of it: we check your installation before you come, help you remotely wherever you are, and visit on site when needed, in coordination with your caretaker, concierge or property manager.</p>
            <ul class="check-list">
{lis(["Pre-arrival check of internet, Wi-Fi, TV and cameras", "Remote help from anywhere in the world", "Help with French internet providers", "Guest Wi-Fi for family, friends and tenants"])}
            </ul>''',
                 photo("second-home-laptop-sideboard-hero", "hero", "Laptop on a wooden sideboard in a bright living room", SPLIT))

business = sec(head_block("businesses", "IT for businesses", "Your outsourced IT department, for Monaco-based companies, Riviera SMEs and international teams.", "For companies") + '''
        <div class="split">
          <div class="panel">
            <h3>Day-to-day IT</h3>
            <ul class="check-list">
''' + lis(["IT maintenance and monitoring", "Helpdesk for your staff, in English or French", "Microsoft 365, email and file sharing", "VoIP phone systems"]) + '''
            </ul>
          </div>
          <div class="panel">
            <h3>Security &amp; continuity</h3>
            <ul class="check-list">
''' + lis(["Managed antivirus (EDR) and firewall", "Multi-factor authentication", "Automatic, off-site backups", "Staff awareness of phishing"]) + '''
            </ul>
            <a class="btn btn--secondary" href="mailto:contact@novazur-it.com">Ask for an IT audit</a>
          </div>
        </div>''', soft=True, label="businesses")

towns = ["Monaco", "Menton", "Roquebrune-Cap-Martin", "Cap-d'Ail", "Èze", "Beaulieu-sur-Mer", "Saint-Jean-Cap-Ferrat", "Villefranche-sur-Mer",
         "Nice", "Saint-Laurent-du-Var", "Cagnes-sur-Mer", "Vence", "Saint-Paul-de-Vence", "Antibes", "Juan-les-Pins", "Valbonne / Sophia Antipolis",
         "Mougins", "Cannes", "Grasse", "Fréjus / Saint-Raphaël"]
area = sec(head_block("area", "Where we work", "Our main service area covers the coast and its nearby hills, from the Italian border to the Estérel. Further up the valleys, visits are by appointment.") + '''
        <div class="steps-layout">
          <div class="steps-layout__media photo">
            ''' + photo("monaco-fontvieille-cliff-tall", "tall", "The Rock of Monaco above the Fontvieille marina", TALL) + '''
          </div>
          <div>
            <ul class="city-list">
''' + "\n".join(f"              <li><span>{t}</span></li>" for t in towns) + '''
            </ul>
            <h3 class="mt-lg">How it works</h3>
            <ol class="check-list">
              <li><strong>Call or email us</strong>: we assess the problem with you, in English.</li>
              <li><strong>Remote session</strong> when possible: you watch everything on your screen.</li>
              <li><strong>Or a visit</strong> at your home or office, at an agreed time.</li>
              <li><strong>Follow-up</strong>: we stay reachable, and businesses get a written report.</li>
            </ol>
          </div>
        </div>''', soft=False, label="area")

cta_html = f'''
    <section class="section">
      <div class="container">
        <div class="cta-band cta-band--photo">
          {cta_bg("nice-promenade-des-anglais-banner")}
          <h2>Need IT help on the Riviera?</h2>
          <p>Call or email us: we reply quickly, in English.</p>
          <div class="btn-row">
            <a class="btn btn--primary" href="{TEL_HREF}">{TEL_INT}</a>
            <a class="btn btn--light" href="mailto:contact@novazur-it.com">contact@novazur-it.com</a>
          </div>
        </div>
      </div>
    </section>'''

write_page(SLUG, h, [hero_html, stats, services, sec(second, soft=True, label="second-homes"), business.replace('section section--soft', 'section'),
                     area.replace('<section class="section"', '<section class="section section--soft"', 1),
                     faq_section("Frequently asked questions", faq, soft=False), cta_html],
           header=HEADER_EN, footer=FOOTER_EN)
