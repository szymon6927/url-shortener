from app import db

class Customers(db.Model):
    """
    Create an Customers table
    """

    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    hash = db.Column(db.String(60), index=True)
    phone = db.Column(db.String(21), index=True)
    redirect_url = db.Column(db.String(254), index=True)
    shorted_url = db.Column(db.String(150), index=True)
    created_at = db.Column(db.Integer(11))

    def __repr__(self):
        return '<Customers: {}>'.format(self.phone)

class Openned(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    customer_hash = db.Column(db.Integer, db.ForeignKey('customers.hash'))
    time =  db.Column(db.Integer(11))