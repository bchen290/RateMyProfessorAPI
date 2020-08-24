DROP TABLE IF EXISTS professor;
DROP TABLE IF EXISTS reviews;

CREATE TABLE professor (
    id INTEGER PRIMARY KEY NOT NULL,
    name TEXT UNIQUE NOT NULL,
    overall_rating INTEGER NOT NULL,
    classes TEXT NOT NULL,
    reviews TEXT NOT NULL
);

CREATE TABLE reviews (
    id INTEGER PRIMARY KEY NOT NULL,
    professor_id INTEGER NOT NULL,
    comment TEXT NOT NULL,
    FOREIGN KEY (professor_id) REFERENCES professor(id)
);