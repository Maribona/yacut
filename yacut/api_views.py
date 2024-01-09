from http import HTTPStatus as status
from flask import jsonify
from . import app, db

from yacut.models import URLMap
from yacut.utils import get_unique_short_id
from yacut.error_handlers import InvalidAPIUsage


@app.route('/api/id/', methods=('POST',))
def create_short_url():
    pass


@app.route('/api/id/<short_id>/', methods=('GET',))
def get_original_url(short_id):
    original_url = URLMap.query.filter_by(short=short_id).first()
    if original_url is not None:
        data = original_url.to_dict()
        return jsonify({'url': data['url']}), status.OK
    raise InvalidAPIUsage('Указанный id не найден', status.NOT_FOUND)
