from flask_wtf import FlaskForm # pylint: disable=import-error
from wtforms import StringField, PasswordField, BooleanField, SubmitField # pylint: disable=import-error
from wtforms.validators import DataRequired # pylint: disable=import-error

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')