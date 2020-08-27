from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from . import app

db = SQLAlchemy(app)


@dataclass
class Professor(db.Model):
    __tablename__ = 'professor'

    id: int = db.Column(db.INTEGER, primary_key=True, nullable=False)
    name: str = db.Column(db.String, nullable=False)
    overall_rating: str = db.Column(db.String, nullable=False)
    classes: str = db.Column(db.String, nullable=False)


@dataclass
class Reviews(db.Model):
    __tablename__ = 'reviews'

    id: int = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    rate_my_professor_id: int = db.Column(db.INTEGER, nullable=False)
    comment: str = db.Column(db.String, nullable=False)

    professor_id: int = db.Column(db.INTEGER, db.ForeignKey('professor.id'), nullable=False)
    professor = db.relationship('Professor', backref=db.backref('reviews', lazy=True))
