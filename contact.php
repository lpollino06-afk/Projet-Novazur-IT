<?php
// Novazur IT — envoi du formulaire de contact par e-mail (hébergement OVH, fonction mail()).

const DESTINATAIRE = 'contact@novazur-it.com';
const EXPEDITEUR   = 'contact@novazur-it.com'; // doit être une adresse du domaine, sinon OVH refuse l'envoi
const PAGE_CONTACT = '/contact';

$ajax = isset($_SERVER['HTTP_ACCEPT']) && strpos($_SERVER['HTTP_ACCEPT'], 'application/json') !== false;

function repondre($ok, $message, $ajax) {
    if ($ajax) {
        http_response_code($ok ? 200 : 400);
        header('Content-Type: application/json; charset=utf-8');
        echo json_encode(['ok' => $ok, 'message' => $message]);
    } else {
        header('Location: ' . PAGE_CONTACT . ($ok ? '?envoye=1' : '?erreur=1'), true, 303);
    }
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: ' . PAGE_CONTACT, true, 303);
    exit;
}

// Anti-spam : champ piège rempli = robot (on fait semblant que tout va bien)
if (!empty($_POST['_gotcha'])) {
    repondre(true, 'ok', $ajax);
}

function champ($nom, $max) {
    $v = isset($_POST[$nom]) ? trim((string) $_POST[$nom]) : '';
    return mb_substr($v, 0, $max, 'UTF-8');
}
// Retire les retours à la ligne des champs courts (empêche l'injection d'en-têtes e-mail)
function ligne($v) {
    return preg_replace('/[\r\n\t]+/', ' ', $v);
}

$nom       = ligne(champ('nom', 120));
$telephone = ligne(champ('telephone', 40));
$email     = ligne(champ('email', 160));
$ville     = ligne(champ('ville', 120));
$profil    = ligne(champ('profil', 80));
$message   = champ('message', 5000);

if ($nom === '' || $telephone === '' || $ville === '' || $message === ''
    || !filter_var($email, FILTER_VALIDATE_EMAIL) || empty($_POST['consentement'])) {
    repondre(false, 'Merci de remplir tous les champs obligatoires.', $ajax);
}

$sujet = 'Demande de contact – ' . $nom . ' (' . $ville . ')';
$corps = "Nouvelle demande depuis le site novazur-it.com\n\n"
       . "Nom : $nom\n"
       . "Téléphone : $telephone\n"
       . "E-mail : $email\n"
       . "Ville : $ville\n"
       . "Profil : $profil\n\n"
       . "Message :\n$message\n\n"
       . "---\nEnvoyé le " . date('d/m/Y à H:i') . "\n";

$entetes = implode("\r\n", [
    'From: Site Novazur IT <' . EXPEDITEUR . '>',
    'Reply-To: ' . mb_encode_mimeheader($nom, 'UTF-8') . ' <' . $email . '>',
    'MIME-Version: 1.0',
    'Content-Type: text/plain; charset=UTF-8',
    'Content-Transfer-Encoding: 8bit',
]);

$ok = mail(DESTINATAIRE, mb_encode_mimeheader($sujet, 'UTF-8'), $corps, $entetes, '-f' . EXPEDITEUR);

repondre($ok, $ok ? 'ok' : "L'envoi a échoué.", $ajax);
