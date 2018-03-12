from flask.ext.bcrypt import Bcrypt
from flask.ext.login import LoginManager, UserMixin
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

from app import app, db


bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view =  'login'

@login_manager.user_loader
def load_user(userid):
    return User.query.filter(User.id==userid).first()


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    _password = db.Column(db.String(128), nullable=False)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext_password):
        self._password = bcrypt.generate_password_hash(plaintext_password)

    @hybrid_method
    def is_correct_password(self, plaintext_password):
        return bcrypt.check_password_hash(self.password, plaintext_password)

    def __init__(self, username, plaintext_password):
        self.username = username
        self.password = plaintext_password

    def __repr__(self):
        return '<User %r>' % self.username
