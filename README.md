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
| `infogerance-informatique-pme.html` | Offre entreprises | infogérance / maintenance informatique PME |
| `formation-informatique.html` | Formations particuliers & entreprises | formation informatique Nice / cours informatique seniors |
| `tarifs.html` | Tarifs | tarif dépannage informatique |
| `zone-intervention.html` | Communes desservies | informatique Alpes-Maritimes |
| `depannage-informatique-nice.html` / `-cannes` / `-antibes` / `-cagnes-sur-mer` / `-saint-laurent-du-var` / `-menton` / `-grasse` | Pages locales | dépannage informatique + ville |
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
- [ ] Lien du module de télé-assistance dans `contact.html` (AnyDesk, RustDesk…)
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

Toutes les autres photos (suffixes `-banner`, `-tall`, `-hero`, `-card` ; versions mobiles en `-sm`) proviennent également
d'Unsplash, sous la même licence. Chaque section du site comporte au moins une image.

Pour mettre vos propres photos : garder les **mêmes noms de fichiers** et un format proche (4:3 ; 5:4 pour la photo d'accueil),
compresser en WebP (ex. sur squoosh.app) et adapter le texte `alt` dans `index.html`.

## Ajouter une page ville

Dupliquer `depannage-informatique-nice.html`, puis modifier : `<title>`, meta description, canonical,
`og:url`, JSON-LD, `<h1>`, textes et quartiers. Ajouter la page dans `sitemap.xml`,
`zone-intervention.html` et le pied de page.
