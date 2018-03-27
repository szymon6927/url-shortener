from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import Users


class RegistrationForm(FlaskForm):
    """
    Form for create new account
    """
    email = StringField('Email', validators=[DataRequired(message="Podaj e-mail"), Email()])
    username = StringField('Username', validators=[DataRequired(message="Podaj nazwę użytkownika")])
    first_name = StringField('First Name', validators=[DataRequired(message="Podaj imię")])
    last_name = StringField('Last Name', validators=[DataRequired(message="Podaj nazwisko")])
    password = PasswordField('Password', validators=[
        DataRequired(message="Złe potwierdzenie hasła"),
        EqualTo('confirm_password')
    ])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Register')

    def validate_email(self, field):
        if Users.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')

    def validate_username(self, field):
        if Users.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use.')


class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    email = StringField('Email', validators=[DataRequired(message="Podaj e-mail"), Email()])
    password = PasswordField('Password', validators=[DataRequired(message="Podaj hasło")])
    submit = SubmitField('Login')