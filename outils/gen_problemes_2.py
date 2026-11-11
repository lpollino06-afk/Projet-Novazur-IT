#!/usr/bin/env python3
"""Pages problèmes : imprimante et nouvel ordinateur.  Usage : python3 outils/gen_problemes_2.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from blocks import *  # noqa

PROBLEMS = [("ordinateur-lent", "Ordinateur lent"), ("suppression-virus-arnaque", "Virus et arnaques"),
            ("installation-wifi-box-internet", "Box internet et Wi-Fi"), ("recuperation-donnees", "Récupération de données"),
            ("installation-imprimante", "Imprimante"), ("nouvel-ordinateur-transfert-donnees", "Nouvel ordinateur"),
            ("installation-antivirus", "Antivirus")]
CITIES = [("depannage-informatique-nice", "Nice"), ("depannage-informatique-monaco", "Monaco"),
          ("depannage-informatique-villefranche-sur-mer", "Villefranche · Beaulieu · Cap-Ferrat"), ("depannage-informatique-menton", "Menton"),
          ("depannage-informatique-saint-laurent-du-var", "Saint-Laurent-du-Var"), ("depannage-informatique-cagnes-sur-mer", "Cagnes-sur-Mer"),
          ("depannage-informatique-vence", "Vence"), ("depannage-informatique-arriere-pays-nicois", "Arrière-pays niçois"),
          ("depannage-informatique-antibes", "Antibes"), ("depannage-informatique-cannes", "Cannes"),
          ("depannage-informatique-mougins-le-cannet", "Mougins · Le Cannet"), ("depannage-informatique-grasse", "Grasse"),
          ("depannage-informatique-frejus-saint-raphael", "Fréjus · Saint-Raphaël")]


def links(slug, soft=False):
    o = "\n".join(f'          <li><a href="{s}">{n}</a></li>' for s, n in PROBLEMS if s != slug)
    c = "\n".join(f'          <li><a href="{s}">{n}</a></li>' for s, n in CITIES)
    return sec(f'''        <div class="section__head">
          <h2 id="liens-titre">Autres problèmes fréquents</h2>
          <p>Retrouvez tous nos services sur la page <a href="assistance-informatique-particuliers">assistance aux particuliers</a>.</p>
        </div>
        <ul class="city-list" style="justify-content:center">
{o}
        </ul>
        <div class="section__head mt-lg">
          <h3>Nous intervenons partout sur la Côte d’Azur et à Monaco</h3>
        </div>
        <ul class="city-list" style="justify-content:center">
{c}
          <li><a href="zone-intervention">Toutes les communes</a></li>
        </ul>''', soft, "liens-titre")


def service_ld(name, stype, slug):
    return {"@type": "Service", "name": name, "serviceType": stype, "provider": {"@id": f"{SITE}/#entreprise"},
            "areaServed": {"@type": "AdministrativeArea", "name": "Alpes-Maritimes"},
            "audience": {"@type": "PeopleAudience", "audienceType": "Particuliers"}, "url": f"{SITE}/{slug}"}


# =====================================================================
# IMPRIMANTE
# =====================================================================
slug = "installation-imprimante"
crumbs = [("assistance-informatique-particuliers", "Particuliers"), (None, "Imprimante")]
faq = [
    ("Mon imprimante est « hors ligne », que faire ?", "Commencez par éteindre l'imprimante et la box, puis rallumez-les. Si le message persiste, l'imprimante a souvent perdu le Wi-Fi ou changé d'adresse sur le réseau : nous la reconnectons et la configurons pour que cela ne se reproduise pas."),
    ("Pouvez-vous installer n'importe quelle marque ?", "Oui : HP, Canon, Epson, Brother et les autres, à jet d'encre ou laser, en USB, en Wi-Fi ou en réseau. Nous installons aussi les scanners et les imprimantes multifonctions."),
    ("Peut-on imprimer depuis un smartphone ou une tablette ?", "Oui, la plupart des imprimantes récentes le permettent. Nous configurons l'impression depuis votre iPhone, votre iPad ou votre téléphone Android, et vous montrons comment faire."),
    ("Mes cartouches sont neuves mais l'imprimante refuse de les reconnaître.", "C'est fréquent avec certaines cartouches compatibles ou après une mise à jour du logiciel de l'imprimante. Nous identifions la cause et vous indiquons la solution la plus adaptée."),
    ("Mon imprimante imprime des traits ou des pages pâles.", "Les têtes d'impression sont probablement encrassées, surtout si l'imprimante sert rarement. Un nettoyage suffit souvent ; nous vous montrons aussi comment l'éviter."),
]
meta = {"slug": slug, "title": "Dépannage et installation d'imprimante à Nice | Novazur IT",
        "desc": "Imprimante hors ligne, qui n'imprime plus ou à installer en Wi-Fi ? Dépannage et installation d'imprimante et de scanner à domicile à Nice et dans le 06.",
        "ogTitle": "Dépannage et installation d'imprimante | Novazur IT",
        "ogDesc": "Imprimante hors ligne, bourrage, Wi-Fi, scanner : nous réglons vos soucis d'impression à domicile ou à distance."}
pannes = service_items([
    ("Imprimante « hors ligne »", "Elle ne répond plus alors qu'elle est allumée : souvent une perte de connexion Wi-Fi ou un changement d'adresse réseau.", "wifi"),
    ("Rien ne sort", "Documents bloqués dans la file d'attente, mauvais pilote, mauvaise imprimante choisie par défaut : nous remettons tout en ordre.", "file"),
    ("Cartouches non reconnues", "Message d'erreur malgré des cartouches neuves, niveau d'encre faux : nous identifions la cause.", "drop"),
    ("Traits, taches, pages pâles", "Têtes d'impression encrassées ou réglages de qualité : un nettoyage et quelques réglages suffisent souvent.", "alert"),
    ("Scanner qui ne fonctionne pas", "Numérisation impossible, fichiers introuvables : nous configurons le scanner et l'envoi vers votre ordinateur ou par e-mail.", "scan"),
    ("Impression depuis le téléphone", "Imprimer une photo ou un billet depuis votre smartphone ou votre tablette, sans passer par l'ordinateur.", "smartphone"),
])
cartouches = f'''            <p>Les cartouches sont la première source de soucis : encre qui sèche quand l'imprimante sert peu, cartouche refusée après une mise à jour, niveau d'encre affiché incorrect…</p>
            <p>Nous vous conseillons sur le type d'imprimante et de cartouches adapté à votre usage, et nous réglons l'imprimante pour limiter la consommation d'encre au quotidien.</p>
            <ul class="check-list">
{lis(["Nettoyage des têtes d'impression", "Réglage du mode brouillon et du noir seul pour les documents courants", "Conseils pour éviter que l'encre ne sèche"])}
            </ul>'''
install = [
    ("Déballage et mise en route", "Retrait des protections, installation des cartouches ou du toner, premiers réglages de l'imprimante."),
    ("Connexion Wi-Fi ou USB", "Connexion à votre box en Wi-Fi, ou en USB si vous préférez, avec une adresse stable pour éviter les « hors ligne »."),
    ("Ordinateurs, tablettes et téléphones", "Installation sur chaque appareil de la maison, impression et numérisation testées partout."),
    ("Vous repartez autonome", "Nous vous montrons comment imprimer, scanner, changer une cartouche et vérifier les niveaux d'encre."),
]
choix = sec(head_block("choix-titre", "Jet d'encre ou laser : laquelle choisir&nbsp;?", "Avant d'acheter, posez-vous la bonne question : qu'allez-vous imprimer, et à quelle fréquence ?", "Conseil d'achat") + '''
        <div class="split">
          <div class="panel">
            <h3>Jet d'encre</h3>
            <ul class="check-list">
''' + lis(["Idéale pour les photos et les documents en couleur", "Compacte, souvent multifonction (scanner, copie)", "À utiliser régulièrement pour éviter que l'encre ne sèche"]) + '''
            </ul>
          </div>
          <div class="panel">
            <h3>Laser</h3>
            <ul class="check-list">
''' + lis(["Parfaite pour les documents en noir et blanc", "Rapide, et le toner ne sèche pas", "Idéale si vous imprimez peu souvent ou beaucoup d'un coup"]) + '''
            </ul>
          </div>
        </div>
        <p class="text-center mt-lg">Vous hésitez&nbsp;? Appelez-nous avant d'acheter : nous vous orientons vers le modèle adapté, en toute indépendance.</p>''', soft=True, label="choix-titre")

h = head(meta, [service_ld("Dépannage et installation d'imprimante", "Dépannage d'imprimante et de scanner", slug), breadcrumb_ld(crumbs, slug)], faq)
write_page(slug, h, [
    hero(crumbs, "Imprimante et scanner", "Dépannage et installation d'imprimante à domicile",
         "Imprimante « hors ligne », pages blanches, cartouches refusées, scanner muet ou nouvelle imprimante à installer en Wi-Fi : nous réglons vos soucis d'impression chez vous ou à distance, et vous montrons comment éviter qu'ils reviennent.",
         photo("imprimante-maison-parquet-hero", "hero", "Imprimante multifonction posée sur un parquet, à côté d'une plante", HERO_SZ, lazy=False)),
    sec(head_block("pannes-titre", "Les pannes d'imprimante les plus courantes", "Toutes marques, jet d'encre ou laser, en USB comme en Wi-Fi.") + "\n" + pannes, soft=False, label="pannes-titre"),
    sec(feature("Cartouches et encre", "cartouches-titre", "Les cartouches, source n°1 des soucis", cartouches,
                photo("imprimante-cartouches-encre", "hero", "Gros plan sur les cartouches d'encre de couleur d'une imprimante", SPLIT)), soft=True, label="cartouches-titre"),
    sec(head_block("install-titre", "Installer une nouvelle imprimante", "Une visite suffit pour que tout fonctionne, sur tous vos appareils.") + "\n" +
        steps_layout(install, photo("imprimante-panneau-commande-tall", "tall", "Main appuyant sur le panneau de commande d'une imprimante", TALL)), soft=False, label="install-titre"),
    choix,
    faq_section("Imprimante : vos questions", faq, soft=False),
    links(slug, soft=True),
    cta("Votre imprimante vous fait des misères&nbsp;?", "Appelez-nous : un premier diagnostic par téléphone règle parfois le problème en quelques minutes.", "toits-vieux-nice-banner"),
])

# =====================================================================
# NOUVEL ORDINATEUR / TRANSFERT DE DONNÉES
# =====================================================================
slug = "nouvel-ordinateur-transfert-donnees"
crumbs = [("assistance-informatique-particuliers", "Particuliers"), (None, "Nouvel ordinateur")]
faq = [
    ("Pouvez-vous m'aider à choisir mon nouvel ordinateur ?", "Oui. Nous partons de votre usage (internet, photos, bureautique, jeux, télétravail) pour vous conseiller un modèle adapté, en toute indépendance, sans lien avec une marque ou un magasin."),
    ("Mes fichiers, e-mails et mots de passe seront-ils transférés ?", "Oui : documents, photos, musique, favoris, comptes e-mail, contacts et, lorsque c'est possible, les mots de passe enregistrés. Nous vérifions tout avec vous avant de terminer."),
    ("Puis-je passer de Windows à Mac, ou l'inverse ?", "Oui. Nous transférons vos fichiers et vos comptes, puis nous vous montrons les différences pour que vous preniez vite vos repères."),
    ("Que faire de mon ancien ordinateur ?", "Nous effaçons vos données de façon sécurisée, puis vous pouvez le donner, le revendre ou le recycler. Nous vous indiquons où le déposer pour qu'il soit recyclé correctement."),
    ("Vous occupez-vous aussi des smartphones et tablettes ?", "Oui : mise en service, transfert des contacts, photos et applications depuis votre ancien appareil, et synchronisation avec votre ordinateur."),
]
meta = {"slug": slug, "title": "Nouvel ordinateur : installation et transfert | Novazur IT",
        "desc": "Nouvel ordinateur, smartphone ou tablette ? Conseil d'achat, mise en service, transfert de vos fichiers, e-mails et photos, à domicile à Nice et dans le 06.",
        "ogTitle": "Nouvel ordinateur : installation et transfert de données | Novazur IT",
        "ogDesc": "Conseil d'achat, mise en service et transfert de toutes vos données vers votre nouvel ordinateur, smartphone ou tablette."}
aide = cards([
    ("Conseil d'achat", "Le bon modèle pour votre usage, en toute indépendance, sans vous suréquiper.", "check"),
    ("Mise en service", "Installation, mises à jour, comptes, sécurité : votre ordinateur prêt à l'emploi dès le premier jour.", "settings"),
    ("Transfert de vos données", "Documents, photos, musique et favoris copiés depuis l'ancien ordinateur, rien n'est oublié.", "box"),
    ("E-mails et comptes", "Messagerie, contacts, calendriers et comptes en ligne reconfigurés à l'identique.", "mail"),
    ("Logiciels et imprimante", "Vos logiciels habituels réinstallés, l'imprimante et le Wi-Fi reconnectés.", "print"),
    ("Ancien ordinateur effacé", "Effacement sécurisé de vos données avant de le donner, le revendre ou le recycler.", "trash"),
], cols=3)
transfere = f'''        <figure class="section-banner photo">
          {photo("cable-usb-transfert-banner", "banner", "Main tenant un câble USB prêt à être branché", FULL)}
        </figure>
        <div class="split">
          <div>
            <h3>Ce que nous transférons</h3>
            <ul class="check-list">
{lis(["Documents, photos, vidéos et musique", "Favoris et mots de passe du navigateur (si possible)", "Comptes e-mail, contacts et calendriers", "Bureau, fond d'écran et dossiers habituels"])}
            </ul>
          </div>
          <div>
            <h3>Ce que nous vérifions avec vous</h3>
            <ul class="check-list">
{lis(["Que vos fichiers importants sont tous là", "Que vos e-mails arrivent et partent", "Que l'imprimante et le Wi-Fi fonctionnent", "Qu'une sauvegarde automatique est en place"])}
            </ul>
          </div>
        </div>'''
tel = f'''            <p>Nouveau smartphone ou nouvelle tablette&nbsp;? Contacts, photos, messages, applications : nous transférons tout depuis l'ancien appareil, puis synchronisons vos photos et vos contacts avec votre ordinateur.</p>
            <ul class="check-list">
{lis(["iPhone, Android et tablettes", "Photos sauvegardées sur l'ordinateur ou dans le cloud", "Applications et comptes reconfigurés"])}
            </ul>'''
etapes = [
    ("Avant l'achat", "Un échange rapide pour cerner vos besoins, et une recommandation claire."),
    ("Le jour J", "Mise en service, transfert de vos données et de vos comptes, chez vous ou sur votre lieu de travail."),
    ("Les jours suivants", "Nous restons joignables : une question sur votre nouvel ordinateur, un appel suffit."),
]
h = head(meta, [service_ld("Installation de nouvel ordinateur et transfert de données", "Mise en service et transfert de données", slug), breadcrumb_ld(crumbs, slug)], faq)
write_page(slug, h, [
    hero(crumbs, "Nouvel ordinateur", "Nouvel ordinateur&nbsp;: installation et transfert de vos données",
         "Vous venez d'acheter un ordinateur, un smartphone ou une tablette, ou vous hésitez encore ? Nous vous conseillons, le mettons en service et transférons toutes vos données, pour que vous retrouviez vos habitudes dès le premier jour.",
         photo("nouvel-ordinateur-carton-hero", "hero", "Carton d'un ordinateur neuf posé sur une table en bois", HERO_SZ, lazy=False)),
    sec(head_block("aide-titre", "Nous nous occupons de tout", "Du choix du modèle jusqu'au recyclage de l'ancien.") + "\n" + aide, soft=False, label="aide-titre"),
    sec(head_block("transfert-titre", "Rien ne se perd pendant le transfert", "Nous travaillons sur une copie de vos données, et l'ancien ordinateur n'est effacé qu'une fois tout vérifié.", "Transfert de données") + "\n" + transfere, soft=True, label="transfert-titre"),
    sec(feature("Smartphone et tablette", "mobile-titre", "Votre nouveau téléphone, prêt en un après-midi", tel,
                photo("smartphone-ordinateur-transfert-card", "card", "Smartphone posé à côté du clavier d'un ordinateur portable", SPLIT), reverse=True), soft=False, label="mobile-titre"),
    sec(head_block("etapes-titre", "Comment ça se passe", None) + "\n" + steps_row(etapes), soft=True, label="etapes-titre"),
    sec(feature("Windows 11", "w11-titre", "Votre ordinateur est encore sous Windows 10&nbsp;?",
                "            <p>Windows 10 ne reçoit plus de mises à jour de sécurité gratuites depuis le 14 octobre 2025. Avant d'en racheter un, nous vérifions si votre ordinateur peut passer à Windows 11. Sinon, nous vous accompagnons dans le choix d'un nouveau modèle et transférons tout.</p>\n            <a class=\"btn btn--secondary\" href=\"ordinateur-lent\">Faire vérifier mon ordinateur</a>",
                photo("installation-windows-portable-hero", "hero", "Main posée sur un ordinateur portable affichant le bureau Windows", SPLIT)), soft=False, label="w11-titre"),
    faq_section("Nouvel ordinateur : vos questions", faq, soft=True, media=photo("ordinateur-portable-bureau-bois-tall", "tall", "Ordinateur portable ouvert sur un bureau en bois", TALL)),
    links(slug, soft=False),
    cta("Un nouvel ordinateur en vue&nbsp;?", "Appelez-nous avant ou après l'achat : nous nous occupons de la mise en service et du transfert.", "services-depannage-informatique-banner"),
])
