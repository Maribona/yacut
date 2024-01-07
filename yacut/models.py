from datetime import datetime

from yacut import db
from settings import MAX_LENGTH_URL, MAX_LENGTH_SHORT_URL


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(MAX_LENGTH_URL), nullable=False)
    short = db.Column(db.String(
        MAX_LENGTH_SHORT_URL), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
