from flask import render_template
from flask_login import login_required

from . import opened
from ..models import Openned


@opened.route('/opened')
@login_required
def opened():
    """
    Render the cutomers template on the / route
    """
    all_opened = Openned.query.all()

    return render_template('opened/opened.html', title="Tabela wszystkich zebranych info",
                           opened=all_opened)
