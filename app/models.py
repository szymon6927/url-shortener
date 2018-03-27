import datetime
from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Users(db.Model, UserMixin):
    """
    Create a Users table
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(60), unique=True)
    username = db.Column(db.String(60), unique=True)
    first_name = db.Column(db.String(60))
    last_name = db.Column(db.String(60))
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError("Password is not readable attribute")

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<Users: {}>".format(self.email)


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Links(db.Model):
    """
    Create an Links table
    """

    __tablename__ = 'links'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    hash = db.Column(db.String(60), unique=True)
    phone = db.Column(db.String(21))
    redirect_url = db.Column(db.String(254))
    shorted_url = db.Column(db.String(150))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return '<Links: {}>'.format(self.phone)


class Openned(db.Model):
    """
    Create a table for opened links
    """

    __tablename__ = 'openned'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    link_id = db.Column(db.Integer)
    link_hash = db.Column(db.String(60))
    ip = db.Column(db.String(30))
    ga_client_id = db.Column(db.String(100))
    client_phone = db.Column(db.String(21))
    open_time = db.Column(db.DateTime, default=datetime.datetime.now)
