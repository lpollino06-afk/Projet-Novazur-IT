# Site Novazur IT

Site vitrine statique (HTML/CSS/JS, sans framework). S'héberge sur n'importe quel hébergeur web
(OVH, o2switch, IONOS, Netlify…). Les adresses sont « propres » (`/contact` au lieu de `/contact.html`) grâce au `.htaccess` : en local (double-clic sur `index.html`), les liens entre pages ne fonctionnent donc pas, c'est normal — tout marche une fois en ligne sur OVH.

## Structure

| Fichier | Rôle | Mot-clé visé |
|---|---|---|
| `index.html` | Accueil | dépannage / assistance informatique Côte d'Azur |
| `assistance-informatique-particuliers.html` | Offre particuliers | assistance informatique à domicile |
| `ordinateur-lent.html` / `suppression-virus-arnaque.html` / `installation-wifi-box-internet.html` / `recuperation-donnees.html` | Pages par problème (particuliers) | ordinateur lent, suppression virus, installation wifi, récupération de données |
| `installation-antivirus.html` | Gestion antivirus (particuliers + PME) : licences, installation, suivi | installation antivirus, antivirus entreprise |
| `maintenance-informatique-entreprise.html` / `telephonie-voip-entreprise.html` / `microsoft-365-entreprise.html` / `sauvegarde-informatique-entreprise.html` / `cybersecurite-entreprise.html` | Pages services entreprises | maintenance informatique entreprise, téléphonie VoIP, Microsoft 365, sauvegarde, cybersécurité PME |
| `infogerance-informatique-pme.html` | Offre entreprises | infogérance / maintenance informatique PME |
| `formation-informatique.html` | Formations particuliers & entreprises | formation informatique Nice / cours informatique seniors |
| `tarifs.html` | Tarifs | tarif dépannage informatique |
| `zone-intervention.html` | Communes desservies | informatique Alpes-Maritimes |
| `depannage-informatique-nice.html` / `-cannes` / `-antibes` / `-cagnes-sur-mer` / `-saint-laurent-du-var` / `-menton` / `-grasse` | Pages locales | dépannage informatique + ville |
| `depannage-informatique-monaco.html` (renforcée) / `-villefranche-sur-mer` / `-arriere-pays-nicois` / `-vence` / `-mougins-le-cannet` / `-frejus-saint-raphael` | Nouvelles pages locales | dépannage informatique + ville |
| `a-propos.html` | Qui sommes-nous : histoire (supervision IT à Monaco, création 2026), convictions, engagements | Novazur IT |
| `installation-imprimante.html` / `nouvel-ordinateur-transfert-donnees.html` | Pages problèmes (particuliers) | dépannage imprimante, installation nouvel ordinateur |
| `it-support-french-riviera-monaco.html` | Page en anglais (Riviera, Monaco, résidences secondaires) | IT support French Riviera / Monaco |
| `assistance-a-distance.html` | Télé-assistance : téléchargement du module, sécurité, FAQ | assistance informatique à distance |
| `contact.html` | Formulaire + coordonnées | — |
| `mentions-legales.html` | Obligations légales + RGPD | (noindex) |
| `404.html`, `sitemap.xml`, `robots.txt`, `.htaccess` | Technique | — |
| `assets/` | CSS, JS, logo | — |

## À compléter avant la mise en ligne

Faire un « rechercher / remplacer dans tous les fichiers » (Ctrl+Maj+H dans VS Code) :

- [x] Numéro officiel : `04 22 13 26 73` (`+33422132673`)
- [ ] `219 boulevard du Mont Boron` → votre adresse (et vérifier `06300 Nice` + coordonnées `geo` dans `index.html`)
- [ ] `novazur-it.com` → votre vrai nom de domaine (canonical, sitemap, Open Graph, .htaccess, e-mail)
- [ ] Horaires d'ouverture (pied de page, contact, JSON-LD dans `index.html`)
- [ ] **Tarifs** dans `tarifs.html` : ce sont des prix indicatifs du marché, à ajuster
- [ ] Formulaire : créer un compte sur [Formspree](https://formspree.io) (gratuit) et remplacer `VOTRE_ID` dans `contact.html`
- [ ] Liens de téléchargement du module de télé-assistance dans `assistance-a-distance.html` : 2 boutons « Bientôt disponible » (Windows, Mac) à activer. Pour régénérer la page : `python3 outils/gen_assistance_distance.py`
- [ ] Mentions légales : SIRET, forme juridique, hébergeur, directeur de publication
- [ ] (Optionnel) Remplacer `assets/img/og-image.jpg` (1200×630 px, aperçu lors des partages) par un visuel avec votre logo
- [ ] Crédit d'impôt 50 % : bloc commenté dans `assistance-informatique-particuliers.html`, à activer **uniquement** si vous êtes déclaré « Services à la personne » (SAP)
- [ ] Ajouter vos profils (Google, LinkedIn, Facebook) dans `"sameAs": []` de `index.html`

## SEO déjà en place

- Une balise `<title>` et une meta description uniques par page, avec ville + service
- Un seul `<h1>` par page, hiérarchie de titres propre, HTML sémantique
- Données structurées Schema.org : `LocalBusiness` (NAP, horaires, zone desservie), `Service`, `BreadcrumbList`, `FAQPage` (pages avec FAQ), `OfferCatalog` (tarifs)
- Titres ≤ ~60 caractères et descriptions ≤ ~160 caractères (pas de troncature dans Google)
- Balises Open Graph + Twitter Card complètes sur toutes les pages
- Pages locales avec contenu **différent** pour chaque ville (pas de copier-coller)
- Maillage interne (pied de page, liens entre offres et villes, fil d'Ariane)
- URLs explicites avec mots-clés, `canonical` sur chaque page, `sitemap.xml`, `robots.txt`
- Performance : aucune police externe, aucune librairie, icônes SVG en ligne, CSS < 15 Ko
- Responsive mobile-first + barre d'appel fixe sur mobile (conversion)
- Accessibilité : lien d'évitement, navigation clavier, contrastes, `aria-*`

## Actions SEO hors site (les plus importantes pour du local !)

1. **Fiche Google Business Profile** : c'est le levier n°1 pour apparaître dans Google Maps
   (« dépannage informatique Nice »). Catégorie principale : *Service de réparation d'ordinateurs*,
   secondaire : *Service d'assistance informatique*. Mêmes nom, adresse et téléphone que sur le site.
2. **Avis clients** : demander systématiquement un avis Google après chaque intervention.
   N'affichez sur le site que de vrais avis (les faux avis sont sanctionnés par la DGCCRF).
3. **Google Search Console** : déclarer le site et soumettre `sitemap.xml`.
4. **Annuaires locaux** avec NAP identique : PagesJaunes, Bing Places, Apple Plans, CCI Nice Côte d'Azur.
5. **Contenu** : ajouter progressivement un blog/guides (« Comment reconnaître un faux support Microsoft »,
   « Wi-Fi qui coupe : 5 solutions »…) et de nouvelles pages villes (Vence, Mougins, Villefranche-sur-Mer…)
   en gardant un contenu unique à chaque fois.
6. **Photos réelles** (vous, votre véhicule, interventions) : bien plus efficaces que des photos de banque d'images.
   Les compresser en WebP et renseigner l'attribut `alt`.

## Photos

Photos libres de droits issues d'[Unsplash](https://unsplash.com/license) (usage commercial gratuit, sans attribution obligatoire),
recadrées et converties en WebP, chacune en deux tailles (`srcset`) pour le mobile et l'ordinateur :

| Fichier | Source Unsplash |
|---|---|
| `support-informatique-nice*.jpg`, `og-image.jpg` | Image fournie par Novazur IT |
| `a-propos-riviera-monaco-hero*.webp` | unsplash.com/photos/8tQC3gTopgI |
| `a-propos-numerique-visio*.webp` | unsplash.com/photos/HJgaV1qjHS0 |
| `imprimante-maison-parquet-hero*.webp` | unsplash.com/photos/QbOnQQebbjU |
| `imprimante-panneau-commande-tall*.webp` | unsplash.com/photos/j7cOdWrbKUI |
| `imprimante-cartouches-encre*.webp` | unsplash.com/photos/Da9qsu-0a00 |
| `nouvel-ordinateur-carton-hero*.webp` | unsplash.com/photos/BsuO0vUX8BY |
| `ordinateur-portable-bureau-bois-tall*.webp` | unsplash.com/photos/RSCirJ70NDM |
| `installation-windows-portable-hero*.webp` | unsplash.com/photos/XITGKg5gRyw |
| `cable-usb-transfert-banner*.webp` | unsplash.com/photos/uzPq35Ahq20 |
| `smartphone-ordinateur-transfert-card*.webp` | unsplash.com/photos/xsGxhtAsfSA |
| `riviera-monaco-aerial-hero*.webp` | unsplash.com/photos/LpUZX53hBqc |
| `monaco-fontvieille-cliff-tall*.webp` | unsplash.com/photos/boBaMH39P6Y |
| `second-home-laptop-sideboard-hero*.webp` | unsplash.com/photos/1SAnrIxw5OY |
| `assistance-informatique-domicile-particulier*.webp` | photo-1758612897035-f75eb62f9f57 |
| `maintenance-informatique-entreprise-pme*.webp` | photo-1551434678-e076c223a692 |
| `cybersecurite-serveur-entreprise*.webp` | photo-1573164713988-8665fc963095 |
| `nice-baie-des-anges-cote-azur*.webp` | photo-1643914729809-4aa59fdc4c17 |
| `ordinateur-lent-utilisateur-agace-hero*.webp` (pages problème / antivirus) | unsplash.com/photos/xQ93cUceb74 |
| `passage-ssd-ordinateur-portable*.webp` (pages problème / antivirus) | unsplash.com/photos/SMHx_spBYx0 |
| `reparation-ordinateur-portable-atelier*.webp` (pages problème / antivirus) | unsplash.com/photos/7x0dGJqbfgk |
| `arnaque-telephone-senior-hero*.webp` (pages problème / antivirus) | unsplash.com/photos/4M7HLn1r6ss |
| `email-suspect-ordinateur-tall*.webp` (pages problème / antivirus) | unsplash.com/photos/5_aNqrJeMIY |
| `wifi-smartphone-canape-hero*.webp` (pages problème / antivirus) | unsplash.com/photos/h2FIDYqL_SA |
| `box-internet-routeur-wifi*.webp` (pages problème / antivirus) | unsplash.com/photos/43ak6tfF4Ss |
| `salon-tv-connectee-wifi-banner*.webp` (pages problème / antivirus) | unsplash.com/photos/N90LM3A5AZQ |
| `wifi-maille-repeteur*.webp` (pages problème / antivirus) | unsplash.com/photos/6ZXP-5-jJts |
| `recuperation-donnees-disque-dur-hero*.webp` (pages problème / antivirus) | unsplash.com/photos/T6u10VL2kjo |
| `carte-sd-disque-externe-card*.webp` (pages problème / antivirus) | unsplash.com/photos/LFUxLeaGsCI |
| `sauvegarde-ssd-externe-tall*.webp` (pages problème / antivirus) | unsplash.com/photos/wTU92z82H4s |
| `disque-dur-interne-tall*.webp` (pages problème / antivirus) | unsplash.com/photos/NZY3eCGZZEU |
| `antivirus-cadenas-clavier-hero*.webp` (pages problème / antivirus) | unsplash.com/photos/QP7RBa5r8HM |
| `antivirus-particulier-canape-card*.webp` (pages problème / antivirus) | unsplash.com/photos/t2HJh7OsnVs |
| `antivirus-entreprise-equipe-card*.webp` (pages problème / antivirus) | unsplash.com/photos/N3Bf0ArT5J0 |
| `antivirus-bureau-open-space-tall*.webp` (pages problème / antivirus) | unsplash.com/photos/CXxH2EiX760 |
| `maintenance-technicien-baie-serveur-hero*.webp` (pages entreprises) | unsplash.com/photos/ufT32_VFS-I |
| `maintenance-bureaux-open-space-tall*.webp` (pages entreprises) | unsplash.com/photos/kN_kViDchA0 |
| `maintenance-point-client-tall*.webp` (pages entreprises) | unsplash.com/photos/uQM4Vk6F_7o |
| `telephonie-ip-salarie-appel-hero*.webp` (pages entreprises) | unsplash.com/photos/WEDDt-u3q3o |
| `poste-telephone-ip-bureau*.webp` (pages entreprises) | unsplash.com/photos/Dkn8-zPIbwo |
| `telephonie-mobile-softphone*.webp` (pages entreprises) | unsplash.com/photos/lDEPHBi7QK4 |
| `telephone-ip-salle-reunion-banner*.webp` (pages entreprises) | unsplash.com/photos/V6GChIKrriU |
| `microsoft-365-ordinateur-bureau-hero*.webp` (pages entreprises) | unsplash.com/photos/pPpUCaudT5Q |
| `visioconference-teams-banner*.webp` (pages entreprises) | unsplash.com/photos/smgTvepind4 |
| `agenda-outlook-partage*.webp` (pages entreprises) | unsplash.com/photos/4BnNnEtAGP0 |
| `visio-equipe-ordinateur-tall*.webp` (pages entreprises) | unsplash.com/photos/s8KDEUHJErQ |
| `sauvegarde-disque-entreprise-hero*.webp` (pages entreprises) | unsplash.com/photos/hL8slYnc-bM |
| `sauvegarde-baie-serveurs*.webp` (pages entreprises) | unsplash.com/photos/2JJ3wBHu4_0 |
| `sauvegarde-externalisee-datacenter-tall*.webp` (pages entreprises) | unsplash.com/photos/fImCPTZ026U |
| `cybersecurite-supervision-ecrans-hero*.webp` (pages entreprises) | unsplash.com/photos/3WW_8chGubQ |
| `cybersecurite-pare-feu-reseau-banner*.webp` (pages entreprises) | unsplash.com/photos/eVWWr6nmDf8 |
| `sensibilisation-cybersecurite-equipe*.webp` (pages entreprises) | unsplash.com/photos/gMsnXqILjp4 |
| `cybersecurite-baie-reseau-tall*.webp` (pages entreprises) | unsplash.com/photos/c-lSQecD9oI |
| `monaco-port-hercule-hero*.webp` (pages villes) | unsplash.com/photos/bVXvntN75zY |
| `monaco-yachts-port-banner*.webp` (pages villes) | unsplash.com/photos/1CkSNmbT7J0 |
| `monaco-monte-carlo-tours-tall*.webp` (pages villes) | unsplash.com/photos/_0hTRmpkT5s |
| `monaco-rocher-fontvieille-tall*.webp` (pages villes) | unsplash.com/photos/otl--SqrefI |
| `monaco-rue-vue-mer-card*.webp` (pages villes) | unsplash.com/photos/mFpXE-oyVoo |
| `villefranche-sur-mer-rade-hero*.webp` (pages villes) | unsplash.com/photos/3OpfLXmfuYY |
| `saint-jean-cap-ferrat-vue-aerienne-banner*.webp` (pages villes) | unsplash.com/photos/5uKbBBkoQco |
| `eze-vue-cap-ferrat-tall*.webp` (pages villes) | unsplash.com/photos/qWYfwwGwMt0 |
| `arriere-pays-nicois-gorges-hero*.webp` (pages villes) | unsplash.com/photos/pzKQC0B5RaU |
| `village-perche-arriere-pays-tall*.webp` (pages villes) | unsplash.com/photos/pUhcWVhekcw |
| `village-perche-mediterranee-card*.webp` (pages villes) | unsplash.com/photos/I18z3r0raS4 |
| `vence-ruelle-pavee-hero*.webp` (pages villes) | unsplash.com/photos/pTaKfl-yNoA |
| `village-provencal-rue-tall*.webp` (pages villes) | unsplash.com/photos/guASyf2km7c |
| `ruelle-escaliers-pierre-card*.webp` (pages villes) | unsplash.com/photos/MDl4txrOudQ |
| `cannes-suquet-vue-mougins-hero*.webp` (pages villes) | unsplash.com/photos/mc1YUnKr2WU |
| `collines-mougins-coucher-soleil-banner*.webp` (pages villes) | unsplash.com/photos/-xXwe3-Ttww |
| `bougainvillier-provence-tall*.webp` (pages villes) | unsplash.com/photos/rPGcXFxyBdI |
| `saint-raphael-port-palmiers-hero*.webp` (pages villes) | unsplash.com/photos/W3CjnuOcgTw |
| `frejus-plage-coucher-soleil-banner*.webp` (pages villes) | unsplash.com/photos/qh3B7kqEm70 |
| `frejus-vieille-ville-rue-tall*.webp` (pages villes) | unsplash.com/photos/1xR5iVnXMMU |

Toutes les autres photos (suffixes `-banner`, `-tall`, `-hero`, `-card` ; versions mobiles en `-sm`) proviennent également
d'Unsplash, sous la même licence. Chaque section du site comporte au moins une image.

Pour mettre vos propres photos : garder les **mêmes noms de fichiers** et un format proche (4:3 ; 5:4 pour la photo d'accueil),
compresser en WebP (ex. sur squoosh.app) et adapter le texte `alt` dans `index.html`.

## Carte de la zone d'intervention (accueil)

Carte interactive en SVG, sans librairie ni service externe : `assets/js/carte-zone.js` (données + code) et `assets/css/carte.css`,
chargés uniquement sur l'accueil, et seulement à l'approche de la section. Cadrage : littoral et arrière-pays proche (≈ 30 min de la côte) ; la recherche reconnaît toutes les communes du 06 (hors cadre = « sur rendez-vous »). Monaco inclus. Var : 11 communes à environ 1 h de Nice
(Saint-Raphaël, Fréjus, Puget-sur-Argens, Les Adrets-de-l'Estérel, Bagnols-en-Forêt, Montauroux, Callian, Tanneron, Fayence, Tourrettes,
Saint-Paul-en-Forêt). Contours des communes : projet [france-geojson](https://github.com/gregoiredavid/france-geojson) (données IGN / INSEE,
Licence Ouverte Etalab), simplifiés. Les temps de trajet affichés sont indicatifs. Pour ajouter une commune du Var ou un repère,
il faut régénérer `carte-zone.js` (script de génération conservé hors du site).

## Ajouter une page ville

Dupliquer `depannage-informatique-nice.html`, puis modifier : `<title>`, meta description, canonical,
`og:url`, JSON-LD, `<h1>`, textes et quartiers. Ajouter la page dans `sitemap.xml`,
`zone-intervention.html` et le pied de page.

## Signatures e-mail

`assets/img/email/` contient le logo et le bandeau utilisés par les signatures e-mail (dossier `Signatures-mail` hors du site). **Ne pas supprimer** : les signatures chargent ces images depuis le site.

## Supports de communication

Le dossier `communication/` (flyers, autocollants, réseaux sociaux, signatures e-mail) est versionné avec le site mais **ne doit pas être envoyé sur l'hébergement**.

## Outils

`outils/` contient les scripts qui génèrent certaines pages (`blocks.py` = boîte à outils commune, `footer.py` = pied de page de tout le site). Comme `communication/`, ce dossier n'est **jamais mis en ligne**.

## Statistiques de visite (sans cookies)

Toutes les pages chargent `assets/js/stats.js`, **désactivé par défaut**. Pour l'activer :
1. créer un compte GoatCounter (goatcounter.com) ou Plausible (plausible.io), deux outils sans cookies ;
2. renseigner `PROVIDER` et `CODE` en haut de `assets/js/stats.js`, puis envoyer ce fichier sur le serveur ;
3. compléter le paragraphe « Cookies » des mentions légales avec le nom de l'outil.

En attendant, OVH fournit des statistiques de fréquentation basées sur les journaux du serveur
(espace client OVH › Hébergements › Statistiques et logs), sans rien installer sur le site.

## Google Search Console

`googleb3dea0bd61837eda.html` (à la racine) prouve à Google que le site vous appartient. **Ne pas le supprimer ni le renommer**, sinon la propriété Search Console est dévalidée. Une règle du `.htaccess` le sert sans redirection.
