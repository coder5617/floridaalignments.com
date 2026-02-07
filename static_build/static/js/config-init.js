(function () {
  const config = window.SITE_CONFIG || {};

  function setText(el, key) {
    if (config[key]) {
      el.textContent = config[key];
    }
  }

  function setHref(el, href) {
    if (href) {
      el.setAttribute('href', href);
    }
  }

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('[data-config-text]').forEach(function (el) {
      const key = el.getAttribute('data-config-text');
      setText(el, key);
    });

    document.querySelectorAll('[data-config-year]').forEach(function (el) {
      el.textContent = config.currentYear || new Date().getFullYear().toString();
    });

    document.querySelectorAll('[data-config-href]').forEach(function (el) {
      const hrefType = el.getAttribute('data-config-href');
      if (hrefType === 'tel' && config.businessPhoneLink) {
        setHref(el, `tel:${config.businessPhoneLink}`);
      }
      if (hrefType === 'mailto' && config.businessEmail) {
        setHref(el, `mailto:${config.businessEmail}`);
      }
    });

    document.querySelectorAll('[data-config-map-link]').forEach(function (el) {
      if (!config.mapsQueryEncoded) {
        return;
      }
      const linkType = el.getAttribute('data-config-map-link');
      if (linkType === 'q') {
        setHref(el, `https://maps.google.com?q=${config.mapsQueryEncoded}`);
      }
      if (linkType === 'directions') {
        setHref(el, `https://maps.google.com/directions/?api=1&destination=${config.mapsQueryEncoded}`);
      }
    });

    document.querySelectorAll('[data-config-mailto]').forEach(function (el) {
      if (config.businessEmail) {
        el.setAttribute('data-mailto', config.businessEmail);
        el.setAttribute('action', `mailto:${config.businessEmail}`);
      }
    });

    if (config.businessName) {
      document.title = document.title.replace(/Florida Alignment & Suspension/g, config.businessName);
    }
  });
})();
