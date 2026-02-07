"""
Static data for Florida Alignment & Suspension website.
This replaces the database-driven content with hardcoded data.
"""

# Services data
SERVICES = [
    {
        'id': 1,
        'name': 'General Mechanical Repairs',
        'short_description': 'Oil changes, tire repair, fluid changes, and routine maintenance',
        'description': 'Complete automotive maintenance services including oil changes, tire repairs, fluid changes, filter replacements, and general mechanical repairs to keep your vehicle running smoothly.',
        'icon_class': 'fas fa-wrench',
        'is_featured': True,
        'display_order': 1
    },
    {
        'id': 2,
        'name': 'Brake Service & Repairs',
        'short_description': 'Professional brake service, pad replacement, and brake system repairs',
        'description': 'Expert brake services including brake pad replacement, rotor resurfacing, brake fluid changes, and complete brake system diagnostics and repairs for your safety.',
        'icon_class': 'fas fa-car',
        'is_featured': True,
        'display_order': 2
    },
    {
        'id': 3,
        'name': 'DOT Inspections',
        'short_description': 'Commercial vehicle DOT inspections and compliance services',
        'description': 'Professional DOT inspections for commercial vehicles, ensuring compliance with federal regulations and safety standards for your fleet.',
        'icon_class': 'fas fa-truck',
        'is_featured': True,
        'display_order': 3
    },
    {
        'id': 4,
        'name': 'Alignments & Suspension Work',
        'short_description': 'Wheel alignments, suspension repairs, and steering services',
        'description': 'Professional wheel alignment services, suspension system repairs, shock and strut replacement, and steering system maintenance for optimal vehicle handling.',
        'icon_class': 'fas fa-cog',
        'is_featured': True,
        'display_order': 4
    },
    {
        'id': 5,
        'name': 'Minor Engine Repairs',
        'short_description': 'Engine diagnostics, tune-ups, and minor repair services',
        'description': 'Engine diagnostic services, tune-ups, minor engine repairs, and performance optimization to keep your engine running efficiently.',
        'icon_class': 'fas fa-engine',
        'is_featured': True,
        'display_order': 5
    },
    {
        'id': 6,
        'name': 'Fleet Maintenance & Tire Repairs',
        'short_description': 'Commercial fleet maintenance and tire repair services',
        'description': 'Comprehensive fleet maintenance services and professional tire repairs for commercial vehicles to minimize downtime and maximize efficiency.',
        'icon_class': 'fas fa-tire',
        'is_featured': True,
        'display_order': 6
    }
]

# FAQs data
FAQS = [
    {
        'id': 1,
        'question': 'Do you provide estimates over the phone?',
        'answer': 'We prefer to see your vehicle in person to provide accurate estimates. However, we can give you a rough estimate over the phone for common services. Contact us to schedule a free inspection.',
        'category': 'general',
        'display_order': 1
    },
    {
        'id': 2,
        'question': 'What payment methods do you accept?',
        'answer': 'We accept cash, credit cards (Visa, MasterCard, Discover, American Express), and checks. We also offer financing options for major repairs.',
        'category': 'general',
        'display_order': 2
    },
    {
        'id': 3,
        'question': 'How long do most repairs take?',
        'answer': 'Repair time varies depending on the service. Oil changes typically take 30 minutes, while major repairs may take several days. We will provide a time estimate when you bring in your vehicle.',
        'category': 'services',
        'display_order': 3
    },
    {
        'id': 4,
        'question': 'Do you offer warranties on your work?',
        'answer': 'Yes, we stand behind our work. We offer warranties on parts and labor. Warranty terms vary by service - we will explain the warranty coverage before starting any work.',
        'category': 'services',
        'display_order': 4
    }
]

# Testimonials data
TESTIMONIALS = [
    {
        'id': 1,
        'customer_name': 'John Smith',
        'review_text': 'Excellent service! They fixed my alignment issues quickly and at a fair price. Highly recommend Florida Alignment & Suspension.',
        'rating': 5,
        'star_rating': '★★★★★',
        'is_featured': True
    },
    {
        'id': 2,
        'customer_name': 'Maria Rodriguez',
        'review_text': 'Professional service and honest pricing. They diagnosed my brake problem accurately and had me back on the road the same day.',
        'rating': 5,
        'star_rating': '★★★★★',
        'is_featured': True
    },
    {
        'id': 3,
        'customer_name': 'Dave Johnson',
        'review_text': 'Great experience with their DOT inspection service. Fast, thorough, and professional. Will definitely be back.',
        'rating': 5,
        'star_rating': '★★★★★',
        'is_featured': True
    }
]


def get_services():
    """Get all services ordered by display_order."""
    return sorted(SERVICES, key=lambda x: x['display_order'])


def get_featured_services():
    """Get featured services."""
    return [s for s in get_services() if s.get('is_featured', False)]


def get_service_by_id(service_id):
    """Get a service by its ID."""
    for service in SERVICES:
        if service['id'] == service_id:
            return service
    return None


def get_service_choices():
    """Get service choices for form dropdown."""
    return [(0, 'Select a service...')] + [(s['id'], s['name']) for s in get_services()]


def get_faqs():
    """Get all active FAQs."""
    return sorted(FAQS, key=lambda x: x['display_order'])


def get_testimonials():
    """Get featured testimonials."""
    return [t for t in TESTIMONIALS if t.get('is_featured', False)]
