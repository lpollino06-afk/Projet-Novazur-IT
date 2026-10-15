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

  // Formulaire de contact (envoi AJAX vers le service configuré dans l'attribut action)
  var form = document.getElementById('contact-form');
  if (form) {
    var status = document.getElementById('form-status');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (form.querySelector('.hp input').value) return; // anti-spam (pot de miel)
      status.textContent = 'Envoi en cours…';
      status.style.color = '';
      fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: { Accept: 'application/json' }
      }).then(function (res) {
        if (!res.ok) throw new Error(res.status);
        form.reset();
        status.textContent = 'Merci ! Votre demande a bien été envoyée, nous vous recontactons rapidement.';
        status.style.color = 'var(--c-success)';
      }).catch(function () {
        status.textContent = "Oups, l'envoi a échoué. Appelez-nous directement ou écrivez-nous par e-mail.";
        status.style.color = '#b42318';
      });
    });
  }
})();
