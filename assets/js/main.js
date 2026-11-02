// Novazur IT — scripts légers (menu mobile, année, formulaire)
(function () {
  'use strict';

  // Menu mobile
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.setAttribute('aria-label', open ? 'Fermer le menu' : 'Ouvrir le menu');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.focus();
      }
    });
  }

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // En-tête qui s'ombre au défilement
  var header = document.querySelector('.site-header');
  if (header) {
    var onScroll = function () { header.classList.toggle('is-scrolled', window.scrollY > 10); };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  // Phrase rotative du hero
  var rotator = document.querySelector('.rotator');
  if (rotator && !reduceMotion) {
    var words = rotator.getAttribute('data-words').split('|');
    var w = 0;
    setInterval(function () {
      rotator.classList.add('is-out');
      setTimeout(function () {
        w = (w + 1) % words.length;
        rotator.textContent = words[w];
        rotator.classList.remove('is-out');
      }, 350);
    }, 2600);
  }

  // Compteurs animés (la valeur finale est déjà dans le HTML pour le SEO et sans JS)
  function animateCount(el) {
    var target = parseInt(el.getAttribute('data-count'), 10);
    var prefix = el.getAttribute('data-prefix') || '';
    var suffix = el.getAttribute('data-suffix') || '';
    var start = null;
    var step = function (t) {
      if (!start) start = t;
      var p = Math.min((t - start) / 1400, 1);
      el.textContent = prefix + Math.round(target * (1 - Math.pow(1 - p, 3))) + suffix;
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  }

  // Apparition des blocs au défilement
  if ('IntersectionObserver' in window && !reduceMotion) {
    var selectors = [
      '.section__head', '.card', '.service-item', '.steps li', '.faq details', '.cta-band',
      '.zone-banner', '.panel', '.stats li', '.split > div', '.prose', '.form', '.contact-list li',
      '.highlight', '.city-list li', '.feature__media', '.feature__text',
      '.section-banner', '.faq-layout__media', '.steps-layout__media'
    ];
    var items = [];
    document.querySelectorAll(selectors.join(',')).forEach(function (el) {
      if (el.closest('.hero') || items.indexOf(el) !== -1) return;
      var cls = 'reveal';
      if (el.classList.contains('feature__media')) {
        cls += el.closest('.feature--reverse') ? ' reveal--right' : ' reveal--left';
      } else if (el.classList.contains('feature__text')) {
        cls += el.closest('.feature--reverse') ? ' reveal--left' : ' reveal--right';
      } else if (el.classList.contains('faq-layout__media') || el.classList.contains('steps-layout__media')) {
        cls += ' reveal--left';
      } else if (el.classList.contains('cta-band') || el.classList.contains('zone-banner') || el.classList.contains('section-banner')) {
        cls += ' reveal--zoom';
      }
      // Décalage en cascade entre éléments frères
      var siblings = Array.prototype.filter.call(el.parentNode.children, function (s) { return s.matches(selectors.join(',')); });
      var delay = Math.min(siblings.indexOf(el), 5) * 0.09;
      el.className += ' ' + cls;
      el.style.setProperty('--reveal-delay', delay + 's');
      items.push(el);
    });

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        observer.unobserve(el);
        el.classList.add('is-visible');
        // Nettoyage : rend la main aux transitions de survol une fois l'apparition terminée
        var d = parseFloat(el.style.getPropertyValue('--reveal-delay')) || 0;
        setTimeout(function () {
          el.classList.remove('reveal', 'reveal--left', 'reveal--right', 'reveal--zoom', 'is-visible');
          el.style.removeProperty('--reveal-delay');
        }, 800 + d * 1000);
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
    items.forEach(function (el) { observer.observe(el); });

    // Les compteurs ne s'animent que si on défile jusqu'à eux : déjà visibles au chargement,
    // ils gardent leur valeur finale (les robots d'indexation ne voient jamais « 0 »)
    var observeStart = Date.now();
    var counterObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        counterObserver.unobserve(entry.target);
        if (Date.now() - observeStart > 300) animateCount(entry.target);
      });
    }, { threshold: 0.6 });
    document.querySelectorAll('[data-count]').forEach(function (el) { counterObserver.observe(el); });
  }

  // Année du copyright
  var year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();

  // Formulaire de contact (envoi AJAX vers contact.php)
  var form = document.getElementById('contact-form');
  if (form) {
    var status = document.getElementById('form-status');
    var button = form.querySelector('button[type="submit"]');
    var buttonLabel = button.textContent;
    var errorText = "Oups, l'envoi a échoué. Appelez-nous au 04 22 13 26 73 ou écrivez à contact@novazur-it.com.";

    var showError = function () {
      status.textContent = errorText;
      status.style.color = '#b42318';
      form.classList.remove('is-shaking');
      void form.offsetWidth; // relance l'animation
      form.classList.add('is-shaking');
    };

    // Remplace le formulaire par un message de confirmation avec une coche animée
    var showSuccess = function () {
      var box = document.createElement('div');
      box.className = 'form-success';
      box.setAttribute('role', 'status');
      box.setAttribute('tabindex', '-1');
      box.innerHTML =
        '<svg class="form-success__check" viewBox="0 0 56 56" aria-hidden="true">' +
          '<circle cx="28" cy="28" r="26"/><path d="M16 29l8 8 16-17"/></svg>' +
        '<h3>Message envoyé !</h3>' +
        '<p>Merci, votre demande est bien arrivée. Nous vous recontactons rapidement, en général dans la journée.</p>' +
        '<button type="button" class="btn btn--ghost">Envoyer un autre message</button>';
      form.hidden = true;
      form.parentNode.insertBefore(box, form);
      box.focus();
      box.querySelector('button').addEventListener('click', function () {
        box.remove();
        form.hidden = false;
        form.querySelector('input').focus();
      });
    };

    // Retour du formulaire quand JavaScript était désactivé (contact.php redirige avec ?envoye=1 ou ?erreur=1)
    if (/[?&]envoye=1/.test(location.search)) showSuccess();
    else if (/[?&]erreur=1/.test(location.search)) showError();

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (form.querySelector('.hp input').value) return; // anti-spam (pot de miel)
      status.textContent = '';
      form.classList.remove('is-shaking');
      button.disabled = true;
      button.classList.add('is-loading');
      button.textContent = 'Envoi en cours…';
      fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: { Accept: 'application/json' }
      }).then(function (res) {
        if (!res.ok) throw new Error(res.status);
        form.reset();
        showSuccess();
      }).catch(showError).then(function () {
        button.disabled = false;
        button.classList.remove('is-loading');
        button.textContent = buttonLabel;
      });
    });
  }
})();
