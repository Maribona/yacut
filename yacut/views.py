from flask import flash, redirect, render_template

from . import app, db
from yacut.forms import UrlForm
from yacut.models import URLMap
from yacut.utils import get_unique_short_id


EXISTING_SHORT_LINK = 'Предложенный вариант короткой ссылки уже существует.'


@app.route('/', methods=('GET', 'POST'))
def main_view():
    form = UrlForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        if URLMap.query.filter_by(short=custom_id).first():
            flash(EXISTING_SHORT_LINK)
            return render_template('yacut.html', form=form)
        if not custom_id:
            custom_id = get_unique_short_id()
        short_url = URLMap(
            original=form.original_link.data,
            short=custom_id
        )
        db.session.add(short_url)
        db.session.commit()
        return render_template(
            'yacut.html',
            form=form,
            short_link=short_url.short
        )
    return render_template('yacut.html', form=form)


@app.route('/<string:short_id>', methods=('GET',))
def redirect_url_view(short_id):
    redirect_url = URLMap.query.filter_by(short=short_id).first_or_404()
    return redirect(redirect_url.original)