from threading import Thread

from flask import jsonify, request, render_template
from . import app, rate_my_professor_scraper
from .models import db, Professor, Reviews


@app.route('/', methods=['GET'])
def home():
    return render_template('template.html')


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/professors/all', methods=['GET'])
def professors():
    professors_and_reviews = db.session.query(Professor, Reviews).join(Reviews).all()

    result = dict()

    for review in professors_and_reviews:
        if review[0].name not in result:
            result[review[0].name] = [review[0], review[1]]
        else:
            result[review[0].name].append(review[1])

    return jsonify(result)


@app.route('/professors', methods=['GET'])
def professor():
    query_parameters = request.args

    professor_name = query_parameters.get('name')

    result = db.session.query(Professor).filter(Professor.name == professor_name).all()

    return jsonify(result)


@app.route('/reviews', methods=['GET'])
def reviews():
    query_parameters = request.args

    professor_name = query_parameters.get('name')

    professor_and_review = db.session.query(Professor, Reviews).filter(Professor.name == professor_name).all()

    result = []

    for review in professor_and_review:
        result.append(review[1])

    return jsonify(result)


@app.route('/scrape')
def scrape():
    thread = Thread(target=threaded_scrape)
    thread.daemon = True
    thread.start()
    return 'Scraping'


def threaded_scrape():
    DREXEL_ID = 1521
    scraper = rate_my_professor_scraper.RateMyProfessorScraper(DREXEL_ID)
    scraper.get_all_professors()
