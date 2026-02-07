from flask import Blueprint, jsonify, request, current_app
from flask_mail import Message
from app import mail
from app.data import get_services, get_testimonials, get_service_by_id
from app.forms.contact import ContactForm
import logging

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


@api_bp.route('/contact', methods=['POST'])
def submit_contact():
    """Handle contact form submission - sends email only, no database storage."""
    try:
        form = ContactForm()
        if form.validate_on_submit():
            # Extract form data
            contact_data = {
                'name': form.name.data,
                'email': form.email.data,
                'phone': form.phone.data or 'Not provided',
                'service_id': form.service_id.data,
                'subject': form.subject.data or 'General Inquiry',
                'message': form.message.data,
                'vehicle_year': form.vehicle_year.data,
                'vehicle_make': form.vehicle_make.data,
                'vehicle_model': form.vehicle_model.data,
                'urgency': form.urgency.data
            }
            
            # Get service name
            service = get_service_by_id(contact_data['service_id']) if contact_data['service_id'] else None
            service_name = service['name'] if service else 'General Inquiry'
            
            # Build vehicle info string
            vehicle_parts = [str(contact_data['vehicle_year']) if contact_data['vehicle_year'] else '',
                          contact_data['vehicle_make'] or '',
                          contact_data['vehicle_model'] or '']
            vehicle_info = ' '.join(filter(None, vehicle_parts)) or 'Not specified'
            
            # Send email notification
            try:
                send_contact_notification(contact_data, service_name, vehicle_info)
                
                return jsonify({
                    'success': True,
                    'message': 'Thank you for your message! We will get back to you soon.'
                })
            except Exception as e:
                current_app.logger.error(f"Failed to send contact notification: {str(e)}")
                return jsonify({
                    'success': False,
                    'message': 'There was an issue sending your message. Please try calling us directly or try again later.'
                }), 500
        else:
            return jsonify({
                'success': False,
                'message': 'Please correct the errors in your form.',
                'errors': form.errors
            }), 400
            
    except Exception as e:
        current_app.logger.error(f"Contact form error: {str(e)}")
        return jsonify({
            'success': False,
            'message': 'An error occurred while processing your request. Please try again.'
        }), 500


def send_contact_notification(contact_data, service_name, vehicle_info):
    """Send email notification for new contact request."""
    
    # Email to business owner
    subject = f"New Contact Request - {service_name}"
    if contact_data['urgency'] in ['urgent', 'asap']:
        subject = f"🚨 URGENT - {subject}"
    
    body = f"""
New contact request received from Florida Alignment & Suspension website:

Customer Information:
- Name: {contact_data['name']}
- Email: {contact_data['email']}
- Phone: {contact_data['phone']}

Service Requested: {service_name}
Vehicle: {vehicle_info}
Urgency: {contact_data['urgency'].upper()}

Subject: {contact_data['subject']}

Message:
{contact_data['message']}

---
This message was sent from the Florida Alignment & Suspension website contact form.
"""
    
    msg = Message(
        subject=subject,
        recipients=[current_app.config['BUSINESS_EMAIL']],
        body=body,
        reply_to=contact_data['email']
    )
    
    mail.send(msg)
    
    # Send confirmation email to customer
    customer_subject = "Thank you for contacting Florida Alignment & Suspension"
    customer_body = f"""
Dear {contact_data['name']},

Thank you for contacting Florida Alignment & Suspension. We have received your request for {service_name} and will get back to you soon.

Your Request Details:
- Service: {service_name}
- Vehicle: {vehicle_info}
- Urgency: {contact_data['urgency']}

We typically respond within 24 hours during business hours. If this is an urgent matter, please call us directly at {current_app.config['BUSINESS_PHONE']}.

Best regards,
Florida Alignment & Suspension Team
{current_app.config['BUSINESS_PHONE']}
{current_app.config['BUSINESS_ADDRESS']}
"""
    
    customer_msg = Message(
        subject=customer_subject,
        recipients=[contact_data['email']],
        body=customer_body
    )
    
    mail.send(customer_msg)
