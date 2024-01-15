from flask import Response, flash, redirect, render_template
from settings import EXISTING_SHORT_LINK

from yacut import app, db
from yacut.forms import UrlForm
from yacut.models import URLMap
from yacut.utils import get_unique_short_id


@app.route('/', methods=('GET', 'POST'))
def main_view() -> Response:
    form = UrlForm()
    if not form.validate_on_submit():
        return render_template('yacut.html', form=form)
    custom_id = form.custom_id.data
    original_link = form.original_link.data
    if URLMap.query.filter_by(short=custom_id).first():
        flash(EXISTING_SHORT_LINK)
        return render_template('yacut.html', form=form)
    short_url = custom_id or get_unique_short_id()
    new_url = URLMap(
        original=original_link,
        short=short_url
    )
    db.session.add(new_url)
    db.session.commit()
    return render_template(
        'yacut.html',
        form=form,
        short_link=new_url.short
    )


@app.route('/<string:short_id>', methods=('GET',))
def redirect_url_view(short_id: str) -> Response:
    redirect_url = URLMap.query.filter_by(short=short_id).first_or_404()
    return redirect(redirect_url.original)