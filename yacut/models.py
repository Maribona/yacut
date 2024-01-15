from datetime import datetime

from settings import MAX_LENGTH_SHORT_URL, MAX_LENGTH_URL

from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(MAX_LENGTH_URL), nullable=False)
    short = db.Column(db.String(
        MAX_LENGTH_SHORT_URL), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            id=self.id,
            original=self.original,
            short=self.short,
            timestamp=self.timestamp,
        )

    def from_dict(self, data):
        for field in ('original', 'short'):
            if field in data:
                setattr(self, field, data[field])

    def add_to_db(self, **kwargs):
        db.session.add(self)
        db.session.commit()
        return self