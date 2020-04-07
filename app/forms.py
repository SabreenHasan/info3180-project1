from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Email
from flask_wtf.fie import FileField, FileAllowed, FileRequired

class LoginForm(FlaskForm):
    firstname = StringField('First Name', validators = [InputRequired(message = 'Please enter your first name')])
    lastname = StringField('Last Name', validators = [InputRequired(message = 'Please enter your last name')])
    gender = SelectField('Gender', choices = [('male', 'Male'), ('female', 'Female')], validators = [InputRequired(message = 'Please enter a gender')])
    email = StringField('Email', validators = [InputRequired(message = 'Please enter your email address')])
    location = StringField('Location', validators = [InputRequired(message = 'Please enter your location')])
    biography = TextAreaField('Biography', validators = [InputRequired(message = 'Please enter a biography')])
    profilePic = FileField('Profile Picture', vaidators = [InputRequired(message = 'Please upload your profile picture'), FileAllowed(['jpg', 'png'])])