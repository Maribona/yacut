from . import app, db


@app.route('/api/id/', methods=('POST',))
def create_short_url():
    pass


@app.route('/api/id/<short_id>/', methods=('GET',))
def get_original_url():
    pass