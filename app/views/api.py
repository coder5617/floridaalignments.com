from flask import Blueprint, jsonify
from app.data import get_services, get_testimonials

api_bp = Blueprint('api', __name__)


@api_bp.route('/services')
def get_services_api():
    """Get all services as JSON."""
    services = get_services()
    return jsonify(services)


@api_bp.route('/testimonials')
def get_testimonials_api():
    """Get featured testimonials as JSON."""
    testimonials = get_testimonials()
    return jsonify(testimonials)
