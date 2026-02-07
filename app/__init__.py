from flask import Flask, request
from flask_wtf import CSRFProtect
from config import config

# Initialize Flask extensions
csrf = CSRFProtect()


def create_app(config_name='default'):
    """Application factory pattern for Flask app creation."""
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    csrf.init_app(app)
    
    # Register blueprints
    from app.views.main import main_bp
    app.register_blueprint(main_bp)
    
    from app.views.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    
    # Register error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        from flask import render_template
        return render_template('errors/404.html'), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        from flask import render_template
        return render_template('errors/500.html'), 500
    
    # Security and performance headers middleware
    @app.after_request
    def after_request(response):
        # Security headers for all responses
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        
        # Performance headers
        if request.endpoint == 'static':
            # Cache static assets for 1 year
            response.headers['Cache-Control'] = 'public, max-age=31536000, immutable'
            response.headers['Expires'] = 'Thu, 31 Dec 2037 23:55:55 GMT'
        elif request.endpoint in ['main.sitemap', 'main.robots']:
            # Cache SEO files for 1 day
            response.headers['Cache-Control'] = 'public, max-age=86400'
        else:
            # Cache HTML pages for 1 hour
            response.headers['Cache-Control'] = 'public, max-age=3600'
        
        # Compression hint
        response.headers['Vary'] = 'Accept-Encoding'
        
        # Production-only security headers
        if not app.config.get('DEBUG', False):
            response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
            response.headers['Content-Security-Policy'] = (
                "default-src 'self'; "
                "script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://cdnjs.cloudflare.com https://maps.googleapis.com https://www.googletagmanager.com; "
                "style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://cdnjs.cloudflare.com https://fonts.googleapis.com; "
                "font-src 'self' https://fonts.gstatic.com https://cdnjs.cloudflare.com; "
                "img-src 'self' data: https: blob:; "
                "connect-src 'self' https://maps.googleapis.com https://www.google-analytics.com; "
                "frame-src 'self' https://maps.google.com; "
                "object-src 'none'; "
                "base-uri 'self'; "
                "form-action 'self';"
            )
        
        return response
    
    # Context processors for template variables
    @app.context_processor
    def inject_business_info():
        from datetime import datetime
        return {
            'business_name': 'Florida Alignment & Suspension',
            'business_phone': '(727) 358-1710',
            'business_email': 'service@floridaalignments.com',
            'business_address': '',
            'google_maps_api_key': app.config.get('GOOGLE_MAPS_API_KEY', ''),
            'current_year': datetime.now().year
        }
    
    return app
