import json
import os

from flask import request, render_template
from flask_login import login_required

from . import home

from .. import db
from ..models import Links
from ..models import Openned

from .. import utils

if os.environ['FLASK_CONFIG'] == "development":
    HOST_NAME = "http://127.0.0.1:5000/"
else:
    HOST_NAME = "http://sekowski-url-shortener.herokuapp.com/"


@home.route('/')
@login_required
def homepage():
    """
    Render the homepage template on the / route
    """

    return render_template('home/index.html', title="Welcome")


@home.route('/addLink', methods=['POST'])
def add_link():
    url = request.form['link']
    phone = request.form['phone']

    if not url and not phone:
        return json.dumps({'info': 'Wypełnij poprawnie pola!'})

    if not utils.url_checker(url):
        return json.dumps({'info': 'Podany link jest błędny, spróbuj ponownie!'})

    link_hash = utils.random_string_generator(8)

    short_link = HOST_NAME + link_hash

    is_exist = Links.query.filter_by(hash=link_hash).first()
    if is_exist is None:
        customer = Links(hash=link_hash, phone=phone,
                         redirect_url=url,
                         shorted_url=short_link)

        db.session.add(customer)
        db.session.commit()

        print(link_hash, flush=True)
        return json.dumps({'info': short_link})
    else:
        return json.dumps({'info': 'Taki hash już istnieje spróboj ponownie!'})


@home.route('/<string:short_url>')
def redirect_to_templte(short_url):
    customer = Links.query.filter_by(hash=short_url).first()
    if customer is None:
        return render_template('home/index.html', title="Welcome", error="Url with this hash doesn't exist !")

    return render_template('redirect/index.html', title="Przekierowanie", text="Trwa przekierowanie",
                           hash=customer.hash)


@home.route('/redirect', methods=['POST'])
def redirect_to_url():
    client_hash = request.form['hash']
    ga_client_id = request.form['ga_client_id']

    link = Links.query.filter_by(hash=client_hash).first()

    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr

    open_link = Openned(link_id=link.id,
                        link_hash=link.hash,
                        ip=ip,
                        ga_client_id=ga_client_id,
                        client_phone=link.phone)
    db.session.add(open_link)
    db.session.commit()

    return json.dumps({'info': link.redirect_url})
