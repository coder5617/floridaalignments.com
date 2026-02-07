from flask import Blueprint, render_template, request, send_from_directory, current_app
from app.data import get_services, get_featured_services, get_testimonials, get_faqs
from app.forms.contact import ContactForm

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """Homepage route."""
    services = get_featured_services()
    testimonials = get_testimonials()
    contact_form = ContactForm()
    
    return render_template('index.html', 
                         services=services, 
                         testimonials=testimonials,
                         contact_form=contact_form)


@main_bp.route('/services')
def services():
    """Services page route."""
    services = get_services()
    return render_template('services.html', services=services)


@main_bp.route('/about')
def about():
    """About page route."""
    return render_template('about.html')


@main_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page route."""
    contact_form = ContactForm()
    services = get_services()
    faqs = get_faqs()
    
    return render_template('contact.html', 
                         contact_form=contact_form, 
                         services=services,
                         faqs=faqs)


@main_bp.route('/sitemap.xml')
def sitemap():
    """Serve sitemap.xml for SEO."""
    return send_from_directory(current_app.static_folder, 'sitemap.xml', mimetype='application/xml')


@main_bp.route('/robots.txt')
def robots():
    """Serve robots.txt for search engines."""
    return send_from_directory(current_app.static_folder, 'robots.txt', mimetype='text/plain')
