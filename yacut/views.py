from flask import abort, flash, redirect, render_template, url_for

from . import app, db
from .forms import OpinionForm
from .models import Opinion


@app.route('/', methods=('GET', 'POST'))
def main_view():
    pass


@app.route('/<string:short_id>', methods=('GET',))
def redirect_url_view(short_id):
    pass