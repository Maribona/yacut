from datetime import datetime

from flask import url_for

from yacut import db
from settings import MAX_LENGTH_URL, MAX_LENGTH_SHORT_URL


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(MAX_LENGTH_URL), nullable=False)
    short = db.Column(db.String(
        MAX_LENGTH_SHORT_URL), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for(
                'redirect_url_view', short=self.short, _external=True))

    def from_dict(self, data):
        for field in ['original', 'short']:
            if field in data:
                setattr(self, field, data[field])