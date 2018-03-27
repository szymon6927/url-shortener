from flask import render_template
from flask_login import login_required

from . import customers
from ..models import Links


@customers.route('/all')
@login_required
def all_customers():
    """
    Render the cutomers template on the / route
    """
    all_links = Links.query.all()

    return render_template('customers/customers.html', title="Tabela wszystkim utworzonych linkow dla klientów",
                           customers=all_links)
