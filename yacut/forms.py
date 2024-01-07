from flask_wtf import FlaskForm
from wtforms import URLField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, URL, Regexp

from settings import MAX_LENGTH_URL, MAX_LENGTH_SHORT_URL, REGEX_SHORT_URL


MESSAGE_REQUIRED = 'Обязательное поле'


class UrlForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=(
            DataRequired(message=MESSAGE_REQUIRED),
            URL(message='недопустимый URL-адрес'),
            Length(
                1, MAX_LENGTH_URL,
                message=(
                    f'Длина URL-адреса не может быть '
                    f'больше {MAX_LENGTH_URL} символов'))
        )
    )
    custom_id = URLField(
        'Ваш вариант короткой ссылки',
        validators=(
            Optional(),
            Regexp(
                REGEX_SHORT_URL,
                message='Допускается использование латинских букв и цифр'),
            Length(
                1, MAX_LENGTH_SHORT_URL,
                message=(
                    f'Длина URL-адреса не может быть '
                    f'больше {MAX_LENGTH_SHORT_URL} символов'))
        )
    )
    submit = SubmitField('Создать')