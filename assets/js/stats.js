// Novazur IT — statistiques de visite SANS cookies (pas de bandeau RGPD nécessaire).
// Désactivé tant que PROVIDER est vide. Pour activer, renseigner UNE des deux configurations :
//   GoatCounter : PROVIDER = 'goatcounter' ; CODE = 'le-code-du-compte' (ex. 'novazur' pour novazur.goatcounter.com)
//   Plausible   : PROVIDER = 'plausible'   ; CODE = 'novazur-it.com' (le domaine déclaré dans Plausible)
// Puis augmenter le numéro de version (?v=) dans les pages, ou simplement renvoyer ce fichier sur le serveur.
(function () {
  'use strict';
  var PROVIDER = '';
  var CODE = '';
  if (!PROVIDER || !CODE) return;
  if (location.hostname !== 'www.novazur-it.com') return; // pas de mesure en local
  var s = document.createElement('script');
  s.async = true;
  if (PROVIDER === 'goatcounter') {
    s.src = 'https://gc.zgo.at/count.js';
    s.setAttribute('data-goatcounter', 'https://' + CODE + '.goatcounter.com/count');
  } else if (PROVIDER === 'plausible') {
    s.defer = true;
    s.src = 'https://plausible.io/js/script.js';
    s.setAttribute('data-domain', CODE);
  } else {
    return;
  }
  document.head.appendChild(s);
})();
