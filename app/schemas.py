from app.models import *
from app import ma


class ProfessorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Professor
        include_fk = True
        include_relationships = True


class ReviewSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Reviews
        include_fk = True
        include_relationships = True
