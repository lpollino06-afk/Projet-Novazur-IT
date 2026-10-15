# Site Novazur IT

Site vitrine statique (HTML/CSS/JS, sans framework). S'héberge sur n'importe quel hébergeur web
(OVH, o2switch, IONOS, Netlify…). Pour le prévisualiser : double-cliquer sur `index.html`.

## Structure

| Fichier | Rôle | Mot-clé visé |
|---|---|---|
| `index.html` | Accueil | dépannage / assistance informatique Côte d'Azur |
| `assistance-informatique-particuliers.html` | Offre particuliers | assistance informatique à domicile |
| `infogerance-informatique-pme.html` | Offre entreprises | infogérance / maintenance informatique PME |
| `formation-informatique.html` | Formations particuliers & entreprises | formation informatique Nice / cours informatique seniors |
| `tarifs.html` | Tarifs | tarif dépannage informatique |
| `zone-intervention.html` | Communes desservies | informatique Alpes-Maritimes |
| `depannage-informatique-nice.html` / `-cannes` / `-antibes` | Pages locales | dépannage informatique + ville |
| `contact.html` | Formulaire + coordonnées | — |
| `mentions-legales.html` | Obligations légales + RGPD | (noindex) |
| `404.html`, `sitemap.xml`, `robots.txt`, `.htaccess` | Technique | — |
| `assets/` | CSS, JS, logo | — |

## À compléter avant la mise en ligne

Faire un « rechercher / remplacer dans tous les fichiers » (Ctrl+Maj+H dans VS Code) :

- [ ] `07 61 44 65 38` et `+33761446538` → votre numéro
- [ ] `219 boulevard du Mont Boron` → votre adresse (et vérifier `06300 Nice` + coordonnées `geo` dans `index.html`)
- [ ] `novazur-it.fr` → votre vrai nom de domaine (canonical, sitemap, Open Graph, .htaccess, e-mail)
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
- Données structurées Schema.org : `LocalBusiness` (NAP, horaires, zone desservie), `Service`, `BreadcrumbList`
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
   « Wi-Fi qui coupe : 5 solutions »…) et de nouvelles pages villes (Cagnes-sur-Mer, Grasse, Menton…)
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

Toutes les autres photos (suffixes `-banner`, `-tall`, `-hero`, `-card` ; versions mobiles en `-sm`) proviennent également
d'Unsplash, sous la même licence. Chaque section du site comporte au moins une image.

Pour mettre vos propres photos : garder les **mêmes noms de fichiers** et un format proche (4:3 ; 5:4 pour la photo d'accueil),
compresser en WebP (ex. sur squoosh.app) et adapter le texte `alt` dans `index.html`.

## Ajouter une page ville

Dupliquer `depannage-informatique-nice.html`, puis modifier : `<title>`, meta description, canonical,
`og:url`, JSON-LD, `<h1>`, textes et quartiers. Ajouter la page dans `sitemap.xml`,
`zone-intervention.html` et le pied de page.
