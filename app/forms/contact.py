from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Optional, NumberRange
from app.data import get_service_choices


class ContactForm(FlaskForm):
    """Form for customer contact requests and quote inquiries."""
    
    name = StringField('Full Name', validators=[
        DataRequired(message='Please enter your name.'),
        Length(min=2, max=100, message='Name must be between 2 and 100 characters.')
    ])
    
    email = StringField('Email Address', validators=[
        DataRequired(message='Please enter your email address.'),
        Email(message='Please enter a valid email address.'),
        Length(max=120)
    ])
    
    phone = StringField('Phone Number', validators=[
        Optional(),
        Length(max=20, message='Phone number must be less than 20 characters.')
    ])
    
    service_id = SelectField('Service Needed', 
                           coerce=int,
                           validators=[Optional()],
                           choices=[])
    
    subject = StringField('Subject', validators=[
        Optional(),
        Length(max=200, message='Subject must be less than 200 characters.')
    ])
    
    message = TextAreaField('Message', validators=[
        DataRequired(message='Please enter your message.'),
        Length(min=10, max=2000, message='Message must be between 10 and 2000 characters.')
    ])
    
    # Vehicle information (optional)
    vehicle_year = IntegerField('Vehicle Year', validators=[
        Optional(),
        NumberRange(min=1900, max=2030, message='Please enter a valid year.')
    ])
    
    vehicle_make = StringField('Vehicle Make', validators=[
        Optional(),
        Length(max=50, message='Vehicle make must be less than 50 characters.')
    ])
    
    vehicle_model = StringField('Vehicle Model', validators=[
        Optional(),
        Length(max=50, message='Vehicle model must be less than 50 characters.')
    ])
    
    urgency = SelectField('Urgency', 
                        choices=[
                            ('normal', 'Normal'),
                            ('urgent', 'Urgent'),
                            ('asap', 'ASAP')
                        ],
                        default='normal')
    
    submit = SubmitField('Send Message')
    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        # Populate service choices from static data
        self.service_id.choices = get_service_choices()