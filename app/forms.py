from flask.ext.wtf import Form
from flask.ext.wtf.csrf import CSRFProtect
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

from app import app


csrf = CSRFProtect(app)

class UsernamePasswordForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])