import json

from flask import flash, render_template
from flask import request

from . import home

from ..models import Customers
from ..models import Openned

from .. import utils

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")

@home.route('/addLink', methods=['POST'])
def addLink():
    url = request.form['link']
    phone = request.form['phone']

    if not utils.url_checker(url):
        return json.dumps({'html':'<span>Podany link jest błędny, spróbuj ponownie!</span>'})

    link_hash = utils.random_string_generator(8)

    print(link_hash, flush=True)
    return json.dumps({'html':'<span>Link added!</span>', 'hash':link_hash})
