from flask import Flask


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

from app import routes
