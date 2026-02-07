# 🏪 Business Information Update Checklist
## Florida Alignment & Suspension Website

This checklist covers all the specific items that need to be updated with real business information before going live.

---

## 📞 CONTACT INFORMATION UPDATES

### ✅ Phone Number
**Current**: `(407) 555-0123` (sample)
**Update Required**: Replace with actual business phone number

**Files to Update:**
1. **`.env`** (Line 6)
   ```bash
   BUSINESS_PHONE=(407) XXX-XXXX
   ```

2. **Template Display** (Auto-populated from .env)
   - Navigation bar phone buttons
   - Contact page
   - Footer
   - Error pages (404/500)

**Format**: `(XXX) XXX-XXXX` (U.S. format with parentheses and dash)

### ✅ Email Address
**Current**: `info@floridaalignment.com` (sample)
**Update Required**: Replace with actual business email

**Files to Update:**
1. **`.env`** (Lines 7, 12, 13)
   ```bash
   BUSINESS_EMAIL=info@yourdomain.com
   MAIL_USERNAME=your-business-email@gmail.com
   MAIL_DEFAULT_SENDER=your-business-email@gmail.com
   ```

2. **Template Display** (Auto-populated from .env)
   - Footer contact info
   - Contact page
   - Error pages

**Requirements**: 
- Must be a real, monitored email address
- Recommended: business@yourdomain.com or info@yourdomain.com

### ✅ Physical Address
**Current**: `123 Main St, Orlando, FL 32801` (sample)
**Update Required**: Replace with actual business address

**Files to Update:**
1. **`.env`** (Line 8)
   ```bash
   BUSINESS_ADDRESS=Your Real Street Address, Orlando, FL XXXXX
   ```

2. **Google Maps Integration** (Line 392 in contact.html)
   - Coordinates will auto-update based on address
   - Or manually update coordinates in `/home/yi/FloridaAlignmentSuspension/app/templates/contact.html`

**Format**: `Street Address, City, State ZIP` (for best Google Maps integration)

### ✅ Business Name
**Current**: `Florida Alignment & Suspension`
**Update Required**: Confirm or update business name

**Files to Update:**
1. **`.env`** (Line 5)
   ```bash
   BUSINESS_NAME=Your Actual Business Name
   ```

**Note**: This populates throughout all templates automatically

---

## 🎨 BRANDING AND VISUAL UPDATES

### ✅ Logo and Images
**Current**: Text-based logo with wrench icon
**Update Required**: Replace with actual business logo

**Files to Update:**
1. **Logo Images** - Create directory `/home/yi/FloridaAlignmentSuspension/app/static/img/`
   - `logo.png` (300x100px recommended)
   - `logo-white.png` (for dark backgrounds)
   - `favicon.ico` (32x32px)
   - `apple-touch-icon.png` (180x180px)

2. **Navigation Template**: `/home/yi/FloridaAlignmentSuspension/app/templates/base.html` (Line 123)
   ```html
   <!-- Replace the wrench icon with actual logo -->
   <img src="{{ url_for('static', filename='img/logo.png') }}" alt="{{ business_name }}" height="40">
   ```

### ✅ Business Photos
**Current**: No business photos (icons only)
**Update Required**: Add real business photos

**Photos Needed:**
- Shop exterior (storefront)
- Shop interior (work bays)
- Team/staff photos
- Equipment photos
- Before/after work examples

**Location**: `/home/yi/FloridaAlignmentSuspension/app/static/img/gallery/`
- `exterior.jpg`
- `interior-1.jpg`, `interior-2.jpg`
- `team.jpg`
- `equipment-1.jpg`, `equipment-2.jpg`
- `work-example-1.jpg`, etc.

### ✅ Color Scheme (Optional)
**Current**: Blue (#0066cc), Orange (#ffc107), Green (#28a745)
**Update**: Modify if needed to match brand colors

**File**: `/home/yi/FloridaAlignmentSuspension/app/static/css/style.css` (Lines 4-12)
```css
:root {
  --primary-color: #0066cc;    /* Main brand color */
  --secondary-color: #28a745;  /* Success/secondary color */
  --accent-color: #ffc107;     /* Call-to-action color */
}
```

---

## 🛠️ SERVICE INFORMATION UPDATES

### ✅ Services Offered
**Current**: 6 sample services
**Update Required**: Verify and customize service descriptions

**Files to Update:**
1. **Database Initialization**: `/home/yi/FloridaAlignmentSuspension/app.py` (Lines 25-74)
   - Update service names, descriptions, and features
   - Add/remove services as needed
   - Update icon classes if desired

2. **Service Features**: `/home/yi/FloridaAlignmentSuspension/app/templates/index.html` (Lines 123-137)
   - Update service-specific features listed under each service card

**Current Services to Review:**
1. General Mechanical Repairs
2. Brake Service & Repairs
3. DOT Inspections
4. Alignments & Suspension Work
5. Minor Engine Repairs
6. Fleet Maintenance & Tire Repairs

### ✅ Business Hours
**Current**: Mon-Fri 8AM-6PM, Sat 8AM-4PM, Sun Closed
**Update Required**: Update with actual business hours

**Files to Update:**
1. **Contact Page**: `/home/yi/FloridaAlignmentSuspension/app/templates/contact.html` (Lines 213-223)
   ```html
   <div class="hours-item d-flex justify-content-between mb-2">
       <span><strong>Monday - Friday</strong></span>
       <span>8:00 AM - 6:00 PM</span>
   </div>
   ```

2. **Structured Data**: `/home/yi/FloridaAlignmentSuspension/app/templates/base.html` (Lines 70-81)
   - Update opening hours for SEO

---

## 📝 CONTENT UPDATES

### ✅ About Page Content
**Current**: Basic placeholder content
**Update Required**: Add real business story and information

**File**: `/home/yi/FloridaAlignmentSuspension/app/templates/about.html`
- Business history
- Owner/team information
- Certifications and licenses
- Why choose your business

### ✅ FAQ Content
**Current**: 4 sample FAQs
**Update Required**: Add real frequently asked questions

**File**: Database initialization in `/home/yi/FloridaAlignmentSuspension/app.py` (Lines 82-107)
- Replace with actual questions customers ask
- Add pricing-related FAQs
- Include warranty information
- Add appointment/scheduling FAQs

### ✅ Customer Testimonials
**Current**: 3 sample testimonials
**Update Required**: Replace with real customer reviews

**File**: Database initialization in `/home/yi/FloridaAlignmentSuspension/app.py` (Lines 116-139)
- Use actual customer names (with permission)
- Include real review text
- Add service-specific testimonials
- Consider varying star ratings (not all 5-star)

### ✅ Homepage Content
**Update Required**: Customize hero section and messaging

**File**: `/home/yi/FloridaAlignmentSuspension/app/templates/index.html`

**Lines 11-12**: Update headline
```html
<h1 class="display-3 fw-bold mb-4 text-shadow">Orlando's Trusted Auto Repair Experts</h1>
```

**Lines 67-90**: Update statistics
```html
<h3 class="display-6 fw-bold text-warning">15+</h3>  <!-- Years in business -->
<h3 class="display-6 fw-bold text-warning">5000+</h3>  <!-- Cars serviced -->
<h3 class="display-6 fw-bold text-warning">4.9★</h3>  <!-- Actual rating -->
```

---

## 🔧 TECHNICAL CONFIGURATION

### ✅ Domain and SSL
**Current**: Running on localhost
**Update Required**: Configure for production domain

**Files to Update:**
1. **Sitemap**: `/home/yi/FloridaAlignmentSuspension/app/static/sitemap.xml`
   - Replace `https://floridaalignment.com` with actual domain

2. **Structured Data**: `/home/yi/FloridaAlignmentSuspension/app/templates/base.html`
   - Update all URLs with actual domain

### ✅ Third-Party Service Integration

#### Google Maps API
**File**: `.env`
```bash
GOOGLE_MAPS_API_KEY=your-actual-google-maps-api-key
```

#### Google Analytics
**File**: `.env`
```bash
GOOGLE_ANALYTICS_ID=G-XXXXXXXXXX  # Your actual GA4 measurement ID
```

#### Calendly Integration (Optional)
**File**: `.env`
```bash
CALENDLY_URL=https://calendly.com/your-business-account
```

### ✅ Email Configuration
**Update Required**: Set up business email system

**File**: `.env`
```bash
# Gmail setup (recommended for small business)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=true
MAIL_USERNAME=your-business-email@gmail.com
MAIL_PASSWORD=your-gmail-app-password

# Alternative: Professional email service
# MAIL_SERVER=smtp.your-email-provider.com
# MAIL_USERNAME=info@yourdomain.com
# MAIL_PASSWORD=your-email-password
```

---

## 📊 SEO AND METADATA

### ✅ Meta Descriptions
**Files to Update:**

1. **Homepage**: `/home/yi/FloridaAlignmentSuspension/app/templates/index.html`
   - No specific meta description (uses base template default)

2. **Base Template**: `/home/yi/FloridaAlignmentSuspension/app/templates/base.html` (Line 11)
   ```html
   <meta name="description" content="Professional automotive repair in Orlando, FL...">
   ```
   Update with specific business description

3. **Contact Page**: `/home/yi/FloridaAlignmentSuspension/app/templates/contact.html` (Line 5)
   Update contact page description

### ✅ Keywords and Local SEO
**File**: `/home/yi/FloridaAlignmentSuspension/app/templates/base.html` (Line 14)
```html
<meta name="keywords" content="auto repair Orlando, brake service, wheel alignment...">
```
Update with your specific services and location

---

## 🔐 SECURITY UPDATES

### ✅ Secret Keys
**File**: `.env`
```bash
SECRET_KEY=generate-new-32-character-secret-key
```

**Generate new key:**
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### ✅ Production Database
**File**: `.env`
```bash
DATABASE_URL_PROD=postgresql://user:password@host:port/database
```

---

## ✅ QUICK UPDATE SUMMARY

**Most Critical Updates (Do These First):**
1. ✅ Business phone number in `.env`
2. ✅ Business email address in `.env`
3. ✅ Physical address in `.env`
4. ✅ Email configuration in `.env`
5. ✅ Secret key generation in `.env`

**Content Updates:**
6. ✅ Service descriptions in `app.py`
7. ✅ Business hours in `contact.html`
8. ✅ FAQ content in `app.py`
9. ✅ Testimonials in `app.py`
10. ✅ About page content

**Technical Updates:**
11. ✅ Google Maps API key in `.env`
12. ✅ Google Analytics ID in `.env`
13. ✅ Domain updates in `sitemap.xml`
14. ✅ Logo and business photos
15. ✅ Meta descriptions in templates

---

**🎯 Priority Level:**
- **HIGH**: Contact information, email setup, secret keys
- **MEDIUM**: Content updates, photos, branding  
- **LOW**: Advanced SEO, optional integrations

**💡 Tip**: Start with the HIGH priority items to get a functional website, then gradually add MEDIUM and LOW priority improvements.