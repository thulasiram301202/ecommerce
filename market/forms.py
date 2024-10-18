from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, Email, EqualTo, DataRequired, ValidationError
from market.model import User

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("Username already exists. Please try another username.")

    def validate_email(self, email_to_check):
        email = User.query.filter_by(email_address=email_to_check.data).first() 
        if email:
            raise ValidationError("Email address already registered. Please try another email address.")

    username = StringField('Username:', validators=[Length(min=5, max=30), DataRequired()])
    email = StringField('Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField('Password:', validators=[Length(min=5), DataRequired()])
    password2 = PasswordField('Re-enter Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    submit = SubmitField('Login')

class purchaseForm(FlaskForm):
    submit = SubmitField("Purchase!")

class sellForm(FlaskForm):
    submit = SubmitField("Sell!")
