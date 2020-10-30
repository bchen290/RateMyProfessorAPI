import json

from apispec import APISpec
from apispec_webframeworks.flask import FlaskPlugin
from apispec.ext.marshmallow import MarshmallowPlugin
from app.routes import *
from app.schemas import *


# noinspection PyTypeChecker
def generate_doc():
    print("Generating doc...")
    spec = APISpec(
        title="RateMyProfessorAPI",
        version="1.0.0",
        openapi_version="2.0",
        info=dict(description="An API that scraped Rate My Professor's Website built on Flask"),
        servers=[
            dict(
                description="Main API",
                url="https://rate-my-professor-api.herokuapp.com/"
            )
        ],
        tags=[
            dict(
                name="Professors",
                description="For getting professors and details about professors"
            ),
            dict(
                name="Reviews",
                description="For getting all reviews"
            )
        ],
        plugins=[FlaskPlugin(), MarshmallowPlugin()]
    )

    spec.components.schema("Professor", schema=ProfessorSchema)
    spec.components.schema("Review", schema=ReviewSchema)

    with app.test_request_context():
        for function_name in app.view_functions:
            if function_name == 'static':
                 continue

            view_function = app.view_functions[function_name]
            spec.path(view=view_function)

    with open('swagger.json', 'w') as f:
        json.dump(spec.to_dict(), f)

    @app.route('/swagger.json')
    def create_swagger_spec():
        return jsonify(spec.to_dict())
