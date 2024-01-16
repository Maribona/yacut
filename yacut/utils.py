import random
import re
import string

from settings import DEFAULT_SHORT_LENGTH, REGEX_SHORT_URL

from yacut.models import URLMap


CHARS = string.ascii_letters + string.digits


def generate_short_id(length: int) -> str:
    return ''.join(random.choice(CHARS) for _ in range(length))


def get_unique_short_id() -> str:
    while True:
        short_id = generate_short_id(DEFAULT_SHORT_LENGTH)
        if re.match(REGEX_SHORT_URL, short_id
                    ) and URLMap.query.filter_by(
                        short=short_id).first() is None:
            return short_id