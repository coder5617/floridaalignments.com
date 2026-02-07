# Florida Alignment & Suspension - Website

A lightweight Flask website for Florida Alignment & Suspension, a car/truck mechanic shop. The site focuses on lead generation through contact forms with email notifications.

## 🚀 Quick Start

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or: venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env  # Then edit .env with your values

# Run the application
python app.py
```

Visit: **http://127.0.0.1:5000**

## 📁 Project Structure

```
FloridaAlignmentSuspension/
├── app/
│   ├── __init__.py         # Flask app factory
│   ├── data.py             # Static content (services, FAQs, testimonials)
│   ├── forms/              # Contact form
│   ├── views/              # Routes (main pages + API)
│   ├── templates/          # HTML templates
│   └── static/             # CSS, JS, images
├── app.py                  # Application entry point
├── config.py               # Configuration
├── requirements.txt        # Python dependencies
└── archive/                # Old documentation (pre-static conversion)
```

## ⚙️ Configuration

Create a `.env` file with:

```bash
# Required
SECRET_KEY=your-secret-key-here
BUSINESS_NAME=Florida Alignment & Suspension
BUSINESS_PHONE=(407) 555-0123
BUSINESS_EMAIL=info@floridaalignment.com
BUSINESS_ADDRESS=123 Main St, Orlando, FL 32801

# Email (for contact form notifications)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=true
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
MAIL_DEFAULT_SENDER=your-email@gmail.com

# Optional
GOOGLE_MAPS_API_KEY=your-api-key
GOOGLE_ANALYTICS_ID=G-XXXXXXXXXX
CALENDLY_URL=https://calendly.com/your-account
```

## 📄 Pages

| Route | Description |
|-------|-------------|
| `/` | Homepage with services, testimonials, CTA |
| `/services` | Full service listings |
| `/about` | About the business |
| `/contact` | Contact form with FAQ |
| `/api/contact` | Contact form submission (POST) |

## ✏️ Editing Content

All content is in **`app/data.py`**:
- `SERVICES` - Service offerings
- `TESTIMONIALS` - Customer reviews  
- `FAQS` - Frequently asked questions

Edit and restart the app to see changes.

## 🚀 Production Deployment (Ubuntu)

```bash
# Install on server
sudo apt install python3 python3-pip python3-venv nginx

# Set up app
git clone <repo> /var/www/florida-alignment
cd /var/www/florida-alignment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run with Gunicorn
gunicorn -w 3 -b 127.0.0.1:8000 app:app
```

Configure Nginx to proxy to port 8000 and set up SSL with Let's Encrypt.

## 📦 Dependencies

- Flask - Web framework
- Flask-WTF - Form handling & CSRF protection
- Flask-Mail - Email notifications
- Gunicorn - Production WSGI server

## 📜 License

Private - Florida Alignment & Suspension