import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Base configuration class."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Email configuration
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
    
    # Business information
    BUSINESS_NAME = os.environ.get('BUSINESS_NAME') or 'Florida Alignment & Suspension'
    BUSINESS_PHONE = os.environ.get('BUSINESS_PHONE') or '(555) 123-4567'
    BUSINESS_EMAIL = os.environ.get('BUSINESS_EMAIL') or 'info@floridaalignment.com'
    BUSINESS_ADDRESS = os.environ.get('BUSINESS_ADDRESS') or '123 Main St, Orlando, FL 32801'
    
    # Third-party API keys
    GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')
    CALENDLY_URL = os.environ.get('CALENDLY_URL')
    GOOGLE_ANALYTICS_ID = os.environ.get('GOOGLE_ANALYTICS_ID')
    
    # Security
    WTF_CSRF_TIME_LIMIT = int(os.environ.get('WTF_CSRF_TIME_LIMIT') or 3600)


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    
    # Production security headers
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # Additional security configurations
    FORCE_HTTPS = True
    SEND_FILE_MAX_AGE_DEFAULT = 31536000  # 1 year for static assets
    PERMANENT_SESSION_LIFETIME = 86400   # 24 hours


class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    WTF_CSRF_ENABLED = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}