from flask import jsonify, request, render_template
from . import app, rate_my_professor_scraper
from .models import db, Professor, Reviews


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/professors/all', methods=['GET'])
def professors():
    all_professors = db.session.query(Professor, Reviews).join(Reviews).all()
    return jsonify(all_professors)


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
    DREXEL_ID = 1521
    scraper = rate_my_professor_scraper.RateMyProfessorScraper(DREXEL_ID)
    scraper.get_all_professors()

    return 'Scraping'
