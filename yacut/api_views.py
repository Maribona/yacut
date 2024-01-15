import re
from http import HTTPStatus as status
from typing import Dict, Union
from urllib.parse import urljoin

from flask import jsonify, request
from settings import EXISTING_SHORT_LINK, MAX_LENGTH_SHORT_URL, REGEX_SHORT_URL

from yacut import app
from yacut.error_handlers import InvalidAPIUsage
from yacut.models import URLMap
from yacut.utils import get_unique_short_id

ERROR_NOTFOUND_ID = 'Указанный id не найден'
ERROR_MISSING_FIELDS = 'В запросе отсутствует обязательное поле'


@app.route('/api/id/', methods=('POST',))
def create_short_url() -> Dict[str, Union[str, int]]:
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if not data.get('url'):
        raise InvalidAPIUsage('"url" является обязательным полем!')

    custom_id = data.get('custom_id')
    if not custom_id or not custom_id.strip():
        custom_id = get_unique_short_id()
    elif URLMap.query.filter_by(short=custom_id).first() is not None:
        raise InvalidAPIUsage(EXISTING_SHORT_LINK)
    elif (
        re.match(REGEX_SHORT_URL, custom_id
                 ) is None or len(custom_id) > MAX_LENGTH_SHORT_URL):
        raise InvalidAPIUsage(
            'Указано недопустимое имя для короткой ссылки')
    new_url = URLMap(
        original=data['url'],
        short=custom_id)
    new_url.add_to_db()
    return (
        jsonify(
            {'url': new_url.original,
             'short_link': urljoin(request.url_root, custom_id)}
        ), status.CREATED)


@app.route('/api/id/<string:short_id>/', methods=('GET',))
def get_original_url(short_id) -> Dict[str, str]:
    original_url = URLMap.query.filter_by(short=short_id).first()
    if original_url is not None:
        return jsonify({'url': original_url.original}), status.OK
    raise InvalidAPIUsage(ERROR_NOTFOUND_ID, status.NOT_FOUND)