from flask import render_template

from . import opened
from ..models import Openned


@opened.route('/opened')
def opened():
    """
    Render the cutomers template on the / route
    """
    all_opened = Openned.query.all()

    return render_template('opened/opened.html', title="Tabela wszystkich zebranych info",
                           opened=all_opened)
