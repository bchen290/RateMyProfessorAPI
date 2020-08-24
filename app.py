from flask import Flask
from . import db

import RateMyProfessorScraper

DREXEL_ID = 1521

app = Flask(__name__)
db.init_app(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/scrape')
def scrape():
    RateMyProfessorScraper.RateMyProfessorScraper(DREXEL_ID)


if __name__ == '__main__':
    app.run()
