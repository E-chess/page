from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError

from market.models import User


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Ta nazwa użytkownika została już użyta! Proszę spróbuj inną nazwę.')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Ten adres email został już użyty! Proszę spróbuj inny adres email.')

    username = StringField(label='Nazwa użytkownika:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Adres email:', validators=[Email(), DataRequired()])
    password = PasswordField(label='Hasło:', validators=[Length(min=6), DataRequired()])
    confirm_password = PasswordField(label='Powtwierć hasło:', validators=[EqualTo('password'), DataRequired()])
    submit = SubmitField(label='Zarejestruj')


class LoginForm(FlaskForm):
    username = StringField(label='Nazwa urzytkownika:', validators=[DataRequired()])
    password = PasswordField(label='Hasło:', validators=[DataRequired()])
    submit = SubmitField(label='Zaloguj')


class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Dołącz')
