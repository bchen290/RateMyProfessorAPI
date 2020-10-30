from flask_swagger_ui import get_swaggerui_blueprint
from app import app

SWAGGER_URL = '/api/docs'
API_URL = '/swagger.json'

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "RateMyProfessorAPI"
    }
)

app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)
