import datetime
from app import db


class Customers(db.Model):
    """
    Create an Customers table
    """

    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    hash = db.Column(db.String(60), unique=True)
    phone = db.Column(db.String(21))
    redirect_url = db.Column(db.String(254))
    shorted_url = db.Column(db.String(150))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return '<Customers: {}>'.format(self.phone)


class Openned(db.Model):
    """
    Create a table for opened links
    """

    __tablename__ = 'openned'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    customer_id = db.Column(db.Integer)
    customer_hash = db.Column(db.String(60))
    customer_ip = db.Column(db.String(30))
    open_time = db.Column(db.DateTime, default=datetime.datetime.now)