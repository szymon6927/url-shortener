from flask import render_template

from . import customers 

@customers.route('/customers')
def customers():
    """
    Render the cutomers template on the / route
    """
    return render_template('customers/customers.html', title="Hi Custom!")