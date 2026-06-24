from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, email

class LoginForm(FlaskForm):
    """Form for user login."""
    email = StringField("Email", validators = [InputRequired(), email()])
    password = PasswordField("Password", validators = [InputRequired()])
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    """Form for user registration."""
    firstname = StringField("Your first name", validators = [InputRequired()])
    lastname = StringField("Your surname", validators = [InputRequired()])
    email = StringField("Email", validators = [InputRequired(), email()])
    phone = StringField("Your phone number", validators = [InputRequired()])
    password = PasswordField("Password", validators = [InputRequired()])
    submit = SubmitField("Make Account")

