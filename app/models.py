from dataclasses import dataclass

from app import db


@dataclass
class Professor(db.Model):
    __tablename__ = 'professor'

    id: int = db.Column(db.INTEGER, primary_key=True, nullable=False)
    name: str = db.Column(db.String, nullable=False)
    overall_rating: str = db.Column(db.String, nullable=False)
    classes: str = db.Column(db.String, nullable=False)

    def __hash__(self):
        return hash((self.id, self.name, self.overall_rating, self.classes))

    def __eq__(self, other):
        return (self.id, self.name, self.overall_rating, self.classes) == (other.id, other.name, other.overall_rating, other.classes)

    def __lt__(self, other):
        return self.name < other.name

@dataclass
class Reviews(db.Model):
    __tablename__ = 'reviews'

    id: int = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    rate_my_professor_id: int = db.Column(db.INTEGER, nullable=False)
    comment: str = db.Column(db.String, nullable=False)

    professor_id: int = db.Column(db.INTEGER, db.ForeignKey('professor.id'), nullable=False)
    professor = db.relationship('Professor', backref=db.backref('reviews', lazy=True))
