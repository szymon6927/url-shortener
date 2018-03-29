from flask import render_template
from flask_login import login_required
from flask import make_response

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
import csv
import datetime

from . import opened
from ..models import Openned


@opened.route('/opened')
@login_required
def show_opened():
    """
    Render the cutomers template on the / route
    """
    all_opened = Openned.query.all()

    return render_template('opened/opened.html', title="Tabela wszystkich zebranych info",
                           opened=all_opened)


@opened.route('/generatecsv')
@login_required
def generate_csv():
    all_opened = Openned.query.all()
    csv_list = []

    for open_info in all_opened:
        temp = []
        if open_info.client_phone is not None and open_info.ga_client_id is not None:
            temp.append(open_info.ga_client_id)
            temp.append(open_info.client_phone)
            csv_list.append(temp)

    dest = StringIO()
    writer = csv.writer(dest)

    for row in csv_list:
        writer.writerow(row)

    output = make_response(dest.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=export-{}.csv".format(datetime.date.today())
    output.headers["Content-type"] = "text/csv"
    return output
