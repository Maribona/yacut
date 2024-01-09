from http import HTTPStatus as status
from flask import jsonify, request
from . import app, db

from yacut.models import URLMap
from yacut.utils import get_unique_short_id
from yacut.error_handlers import InvalidAPIUsage


ERROR_NOTFOUND_ID = 'Указанная ссылка не найдена'
ERROR_MISSING_FIELDS = 'В запросе отсутствует обязательное поле'


@app.route('/api/id/', methods=('POST',))
def create_short_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage(ERROR_MISSING_FIELDS)
    if 'url' not in data:
        raise InvalidAPIUsage(ERROR_MISSING_FIELDS)
    if not data.get('custom_id'):
        data['custom_id'] = get_unique_short_id()
        raise InvalidAPIUsage('Данный вариант ссылки уже используется')
    new_url = URLMap()
    new_url.from_dict(data)
    db.session.add(new_url)
    db.session.commit()
    return jsonify(new_url.to_dict()), status.CREATED


@app.route('/api/id/<short_id>/', methods=('GET',))
def get_original_url(short_id):
    original_url = URLMap.query.filter_by(short=short_id).first()
    if original_url is not None:
        data = original_url.to_dict()
        return jsonify({'url': data['url']}), status.OK
    raise InvalidAPIUsage(ERROR_NOTFOUND_ID, status.NOT_FOUND)
