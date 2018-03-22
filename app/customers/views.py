from flask import render_template

from . import customers 
from ..models import Customers

@customers.route('/all')
def all_customers():
    """
    Render the cutomers template on the / route
    """
    all_customers = Customers.query.all()

    return render_template('customers/customers.html', title="Tabela wszystkim utworzonych linkow dla klientów", customers=all_customers)