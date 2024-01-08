from flask import abort, flash, redirect, render_template, url_for

from . import app, db
from yacut.forms import OpinionForm
from yacut.models import URLMap
from yacut.utils import get_unique_short_id


@app.route('/', methods=('GET', 'POST'))
def main_view():
    pass


@app.route('/<string:short_id>', methods=('GET',))
def redirect_url_view(short_id):
    redirect_url = URLMap.query.filter_by(short=short_id).first_or_404()
    return redirect(redirect_url.original)