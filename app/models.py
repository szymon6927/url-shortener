import datetime
from app import db


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