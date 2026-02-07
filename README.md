# Florida Alignment & Suspension

A modern, responsive static website for Florida Alignment & Suspension, a professional automotive alignment and suspension service in Pinellas County, Florida.

## Overview

This is a pure static website built with vanilla HTML, CSS, and JavaScript. It features:

- **Modern Design**: Clean, professional interface with smooth animations
- **Responsive Layout**: Mobile-first design using Bootstrap 5
- **Interactive Features**: Service cards, contact forms, interactive map with 14 nearby businesses
- **SEO Optimized**: Meta tags, sitemap, robots.txt, semantic HTML
- **Fast Loading**: Minimal dependencies, CDN-hosted assets, optimized caching
- **Accessibility**: ARIA labels, keyboard navigation, semantic HTML

## Directory Structure

```
floridaalignments.com/
├── index.html              # Homepage
├── config.js               # Site configuration (business info)
├── robots.txt              # Search engine directives
├── sitemap.xml             # SEO sitemap
├── 404.html                # Custom 404 error page
├── 500.html                # Custom 500 error page
├── _headers                # Cloudflare Pages headers (security & caching)
├── _redirects              # Cloudflare Pages redirects
├── services/
│   └── index.html          # Services page
├── about/
│   └── index.html          # About page
├── contact/
│   └── index.html          # Contact page
└── static/
    ├── css/
    │   └── style.css       # Custom styles
    ├── js/
    │   ├── main.js         # Main functionality (557 lines)
    │   └── config-init.js  # Config loader
    └── icons/
        └── (favicons)
```

## Configuration

All business information is centralized in `config.js`:

```javascript
window.SITE_CONFIG = {
  businessName: "Florida Alignment & Suspension",
  businessNameShort: "FL Alignment",
  businessPhoneDisplay: "(727) 358-1710",
  businessPhoneLink: "7273581710",
  businessEmail: "service@floridaalignments.com",
  businessAddress: "",
  domain: "https://floridaalignment.com",
  currentYear: "2026"
};
```

To update business information:
1. Edit `config.js`
2. Commit and push changes
3. Cloudflare Pages will auto-deploy

## Local Development

Run a local server to test the site:

```bash
# Using Python 3
python -m http.server 8000

# Using Node.js (if installed)
npx http-server -p 8000

# Using PHP (if installed)
php -S localhost:8000
```

Then open http://localhost:8000 in your browser.

### Testing Checklist

- [ ] All pages load without errors (/, /services/, /about/, /contact/)
- [ ] Business phone displays correctly
- [ ] Business email displays correctly
- [ ] Contact form opens email client with pre-filled data
- [ ] Form validation works (required fields, phone formatting)
- [ ] Map displays with 14 markers
- [ ] Service cards have hover effects
- [ ] Mobile menu toggles correctly
- [ ] Fade-in animations trigger on scroll
- [ ] No console errors
- [ ] Responsive on mobile, tablet, desktop

## Deployment

### Cloudflare Pages (Recommended)

1. **Connect Repository**:
   - Log in to Cloudflare Dashboard
   - Go to Pages → Create a project
   - Connect your GitHub repository

2. **Build Settings**:
   - Build command: *(leave empty)*
   - Build output directory: `/` (root)
   - Root directory: `/` (root)
   - Branch: `main`

3. **Deploy**:
   - Click "Save and Deploy"
   - Cloudflare Pages will auto-deploy on every push to `main`

4. **Custom Domain** (optional):
   - Add custom domain in Cloudflare Pages settings
   - Update DNS records as instructed
   - HTTPS certificate auto-provisioned

### Other Static Hosts

This site works on any static hosting provider:

- **Netlify**: Drag & drop the root folder or connect GitHub
- **Vercel**: Import GitHub repo, leave build settings empty
- **GitHub Pages**: Enable Pages in repo settings, set source to root
- **AWS S3 + CloudFront**: Upload files to S3 bucket, configure CloudFront

## Features

### Pages

1. **Homepage** (`/`): Hero section, services overview, call-to-action
2. **Services** (`/services/`): Detailed list of alignment and suspension services
3. **About** (`/about/`): Company information and expertise
4. **Contact** (`/contact/`): Contact form (mailto:), interactive map with 14 nearby businesses

### Interactive Map

The contact page features a Leaflet map showing Florida Alignment & Suspension plus 14 nearby businesses:
- Interactive markers with business names
- Zoom/pan controls
- Mobile-friendly
- No API key required (uses OpenStreetMap)

### Contact Form

- Client-side validation (required fields, phone formatting)
- Opens email client with pre-filled subject/body
- No backend required (uses `mailto:` protocol)
- Spam-resistant (requires user's email client)

### Animations

- Fade-in on scroll for sections
- Smooth hover effects on service cards
- Mobile menu slide animation
- CSS transitions for smooth interactions

## Browser Support

- **Modern Browsers**: Chrome, Firefox, Safari, Edge (last 2 versions)
- **Mobile**: iOS Safari, Chrome Mobile, Samsung Internet
- **Progressive Enhancement**: Core content works without JavaScript

## Performance

- **Lighthouse Scores** (typical):
  - Performance: 95-100
  - Accessibility: 90-95
  - Best Practices: 95-100
  - SEO: 100

- **Asset Loading**:
  - CDN-hosted libraries (Bootstrap, Font Awesome, Leaflet)
  - Minimal custom CSS/JS
  - Optimized caching headers (via `_headers`)

## SEO

- Meta tags on all pages (title, description, keywords)
- Open Graph tags for social sharing
- Semantic HTML5 structure
- `robots.txt` allows all crawlers
- `sitemap.xml` lists all pages
- Mobile-friendly (Google requirement)
- Fast loading times

## Updating Content

### Change Business Info

Edit `config.js` and commit/push:

```javascript
businessPhoneDisplay: "(727) 358-1710",  // Update here
businessEmail: "service@floridaalignments.com"
```

### Update Services

Edit `services/index.html`:
- Find the service cards section
- Add/remove/edit service descriptions
- Commit and push

### Update Map Markers

Edit `contact/index.html`:
- Find the `nearbyBusinesses` array in the script section
- Add/remove markers with name and coordinates
- Commit and push

### Update Styles

Edit `static/css/style.css`:
- Modify colors, fonts, spacing
- Test locally before deploying
- Commit and push

## Security

- **Headers**: Security headers configured in `_headers` (X-Frame-Options, CSP, etc.)
- **HTTPS**: Enforced by Cloudflare Pages
- **No Secrets**: No API keys, no environment variables, no server-side code
- **Form Protection**: `mailto:` forms prevent automated submissions

## Maintenance

### Regular Tasks

- Update copyright year in `config.js` annually
- Review and update service descriptions quarterly
- Test contact form functionality monthly
- Check for broken links monthly
- Review analytics data (if configured)

### Dependencies

All dependencies are CDN-hosted, no local installation required:

- Bootstrap 5.3.0 (CSS framework)
- Font Awesome 6.5.1 (icons)
- Google Fonts (Montserrat)
- Leaflet 1.9.4 (maps)

## Troubleshooting

### Map Not Displaying

- Check browser console for JavaScript errors
- Verify Leaflet CDN is accessible
- Ensure coordinates are valid (latitude, longitude)

### Contact Form Not Working

- Verify user has email client configured
- Check `mailto:` links in browser console
- Test with different email clients

### Styles Not Loading

- Check browser console for CSS 404 errors
- Verify CDN links are accessible
- Clear browser cache

### 404 Errors on Subpages

- Ensure Cloudflare Pages is serving directory indexes
- Check `_redirects` file syntax
- Verify folder structure matches expected paths

## License

Proprietary - © 2026 Florida Alignment & Suspension. All rights reserved.

## Support

For technical issues or questions:
- Email: service@floridaalignments.com
- Phone: (727) 358-1710

---

**Last Updated**: February 2026
**Version**: 2.0 (Static Site Migration)
