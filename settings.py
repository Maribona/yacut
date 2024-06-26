import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', default='sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')


MAX_LENGTH_URL = 2000
MAX_LENGTH_SHORT_URL = 16
REGEX_SHORT_URL = r'^[A-Za-z0-9]+$'
DEFAULT_SHORT_LENGTH = 6

EXISTING_SHORT_LINK = 'Предложенный вариант короткой ссылки уже существует.'
