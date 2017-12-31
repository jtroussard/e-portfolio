from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Optional, Email, Length, Required
from wtforms.widgets import SubmitInput, HTMLString

class ContactForm(FlaskForm):
	name = StringField(HTMLString('Name <span class="required">*</span>'), validators=[Required("Please enter your name."), InputRequired()])
	email = StringField(HTMLString('Email <span class="required">*</span>'), validators=[Required("Please enter your email address."), InputRequired(),Email()])
	subject = StringField('Subject', validators=[Optional()])
	comments = TextAreaField(HTMLString('Message <span class="required">*</span>'), validators=[Required("Don't be shy. Say something."), InputRequired(), Length(max=300)])
	submit = SubmitField('Send')