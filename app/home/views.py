import json

from flask import request, flash, render_template, abort, redirect

from . import home

from .. import db
from ..models import Customers
from ..models import Openned

from .. import utils

HOST_NAME = "http://127.0.0.1:5000/"

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

    if not url and not phone:
        return json.dumps({'info':'Wypełnij poprawnie pola!'})

    if not utils.url_checker(url):
        return json.dumps({'info':'Podany link jest błędny, spróbuj ponownie!'})

    link_hash = utils.random_string_generator(8)

    short_link = HOST_NAME + link_hash

    is_exist = Customers.query.filter_by(hash=link_hash).first()
    if is_exist is None:
        customer = Customers(hash=link_hash,
                            phone=phone,
                            redirect_url=url,
                            shorted_url=short_link)

        db.session.add(customer)
        db.session.commit()

        print(link_hash, flush=True)
        return json.dumps({'info':short_link})
    else:
        return json.dumps({'info':'Taki hash już istnieje spróboj ponownie!'})


@home.route('/<string:short_url>')
def redirect_to_url(short_url):
    customer = Customers.query.filter_by(hash=short_url).first()
    if customer is None:
        return render_template('home/index.html', title="Welcome", error="Url with this hash doesn't exist !")

    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr
    
    open = Openned(customer_id=customer.id,
                customer_hash=customer.hash,
                customer_ip=ip)
    db.session.add(open)
    db.session.commit()

    return redirect(customer.redirect_url)



