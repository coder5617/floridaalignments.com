Florida Alignments Static Site
==============================

Overview
--------
This repository contains a fully static site for Florida Alignment & Suspension.
It is designed for low-cost hosting (Cloudflare Pages) and uses a mailto: flow
to open the visitor's local email client when the contact form is submitted.

Project Structure
-----------------
static_build/
  404.html
  500.html
  about/
    index.html
  contact/
    index.html
  services/
    index.html
  index.html
  robots.txt
  sitemap.xml
  config.js
  static/
    css/
      style.css
    js/
      main.js
      config-init.js
    icons/
    img/

Key Files
---------
- static_build/config.js
  Single source of truth for business name, phone, email, address, domain, and
  optional Google Maps API key.
- static_build/static/js/config-init.js
  Applies config values to the static pages at runtime.
- static_build/contact/index.html
  Contact form uses a mailto: flow to open the user's local email client and
  includes all fields.

Updating Business Details
-------------------------
Edit static_build/config.js and update:
- businessName
- businessNameShort
- businessPhoneDisplay
- businessPhoneLink
- businessEmail
- businessAddress
- domain
- mapsQuery / mapsQueryEncoded
- googleMapsApiKey (optional)

Local Preview
-------------
Run a local server from the static_build directory:

  python -m http.server 8000 --directory static_build

Then open:
  http://localhost:8000

Deployment (Cloudflare Pages)
-----------------------------
Publish the contents of static_build as the site root. No server is required.