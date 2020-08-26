from flask import Flask, jsonify, request
from . import db, RateMyProfessorScraper

DREXEL_ID = 1521

app = Flask(__name__)
db.init_app(app)


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Rate My Professor API</h1>
    <p>A WIP api that fetches data about Drexel's professors</p>'''


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/professors/all', methods=['GET'])
def professors():
    cursor = db.get_db().cursor()
    results = cursor.execute('SELECT * FROM professor').fetchall()
    items = [dict(zip([key[0] for key in cursor.description], row)) for row in results]
    return jsonify(items)


@app.route('/professors', methods=['GET'])
def professor():
    query_parameters = request.args

    professor_name = query_parameters.get('name')

    query = "SELECT * FROM professor WHERE name=?"
    cursor = db.get_db().cursor()
    results = cursor.execute(query, (professor_name,)).fetchall()

    items = [dict(zip([key[0] for key in cursor.description], row)) for row in results]

    return jsonify(items)


@app.route('/scrape')
def scrape():
    scraper = RateMyProfessorScraper.RateMyProfessorScraper(DREXEL_ID)
    scraper.get_all_professors()

    return 'Scraping'


if __name__ == '__main__':
    app.run()
