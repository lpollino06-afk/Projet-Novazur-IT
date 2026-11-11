#!/usr/bin/env python3
"""Pied de page commun du site (5 colonnes).

Usage : python3 outils/footer.py
Remplace le bloc <footer class="site-footer">…</footer> de toutes les pages qui en ont un
(sauf mentions-legales.html et 404.html, qui ont un pied de page volontairement réduit).
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FOOTER = """  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <a class="logo" href="/"><img src="assets/img/logo.svg?v=2" alt="" width="36" height="36"><span>Novazur <b>IT</b></span></a>
          <p>Dépannage, assistance et maintenance informatique pour particuliers et PME sur la Côte d'Azur et à Monaco.</p>
          <address style="font-style:normal">
            Novazur IT<br>
            219 boulevard du Mont Boron<br>
            06300 Nice
          </address>
        </div>
        <div>
          <h2>Particuliers</h2>
          <ul>
            <li><a href="assistance-informatique-particuliers">Assistance particuliers</a></li>
            <li><a href="ordinateur-lent">Ordinateur lent</a></li>
            <li><a href="suppression-virus-arnaque">Virus et arnaques</a></li>
            <li><a href="installation-wifi-box-internet">Box internet et Wi-Fi</a></li>
            <li><a href="recuperation-donnees">Récupération de données</a></li>
            <li><a href="installation-imprimante">Imprimante</a></li>
            <li><a href="nouvel-ordinateur-transfert-donnees">Nouvel ordinateur</a></li>
            <li><a href="installation-antivirus">Gestion antivirus</a></li>
            <li><a href="assistance-a-distance">Assistance à distance</a></li>
            <li><a href="formation-informatique">Formations</a></li>
          </ul>
        </div>
        <div>
          <h2>Entreprises</h2>
          <ul>
            <li><a href="infogerance-informatique-pme">Infogérance PME</a></li>
            <li><a href="maintenance-informatique-entreprise">Maintenance informatique</a></li>
            <li><a href="cybersecurite-entreprise">Cybersécurité</a></li>
            <li><a href="microsoft-365-entreprise">Microsoft 365</a></li>
            <li><a href="sauvegarde-informatique-entreprise">Sauvegarde</a></li>
            <li><a href="telephonie-voip-entreprise">Téléphonie VoIP</a></li>
            <li><a href="formation-informatique#entreprises">Formations en entreprise</a></li>
          </ul>
        </div>
        <div>
          <h2>Zones</h2>
          <ul>
            <li><a href="depannage-informatique-nice">Informatique Nice</a></li>
            <li><a href="depannage-informatique-monaco">Informatique Monaco</a></li>
            <li><a href="depannage-informatique-cannes">Informatique Cannes</a></li>
            <li><a href="depannage-informatique-antibes">Informatique Antibes</a></li>
            <li><a href="depannage-informatique-cagnes-sur-mer">Informatique Cagnes-sur-Mer</a></li>
            <li><a href="depannage-informatique-saint-laurent-du-var">Informatique Saint-Laurent</a></li>
            <li><a href="depannage-informatique-menton">Informatique Menton</a></li>
            <li><a href="depannage-informatique-grasse">Informatique Grasse</a></li>
            <li><a href="depannage-informatique-frejus-saint-raphael">Fréjus / Saint-Raphaël</a></li>
            <li><a href="zone-intervention">Toutes les zones</a></li>
          </ul>
        </div>
        <div>
          <h2>Contact</h2>
          <ul>
            <li><a href="tel:+33422132673">04 22 13 26 73</a></li>
            <li><a href="mailto:contact@novazur-it.com">contact@novazur-it.com</a></li>
            <li>Lun – ven : 8h30 – 19h</li>
            <li>Samedi : 9h – 13h</li>
            <li>Français · <a href="it-support-french-riviera-monaco" lang="en" hreflang="en">English</a></li>
            <li><a href="tarifs">Tarifs</a></li>
            <li><a href="contact">Devis gratuit</a></li>
            <li><a href="a-propos">Qui sommes-nous&nbsp;?</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>© <span id="year">2026</span> Novazur IT – Tous droits réservés</span>
        <a href="mentions-legales">Mentions légales &amp; confidentialité</a>
      </div>
    </div>
  </footer>"""

PATTERN = re.compile(r'  <footer class="site-footer">\s*<div class="container">\s*<div class="footer-grid">.*?</footer>', re.S)


def apply(paths=None):
    n = 0
    for f in paths or sorted(ROOT.glob("*.html")):
        if f.name in ("mentions-legales.html", "404.html") or " 2." in f.name:
            continue
        t = f.read_text()
        u, k = PATTERN.subn(FOOTER, t)
        if k == 1 and u != t:
            f.write_text(u)
            n += 1
    return n


if __name__ == "__main__":
    print(apply(), "pages mises à jour")
