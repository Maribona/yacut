import re
import random
import string
from yacut.models import URLMap
from settings import REGEX_SHORT_URL, DEFAULT_SHORT_LENGTH


def generate_short_id(length):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


def get_unique_short_id():
    while True:
        short_id = generate_short_id(DEFAULT_SHORT_LENGTH)
        if re.match(REGEX_SHORT_URL, short_id) and \
           URLMap.query.filter_by(short=short_id).first() is None:
            return short_id