DROP TABLE IF EXISTS professor;
DROP TABLE IF EXISTS reviews;

CREATE TABLE professor (
    id INTEGER PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    overall_rating TEXT NOT NULL,
    classes TEXT NOT NULL
);

CREATE TABLE reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rate_my_professor_id INTEGER NOT NULL,
    professor_id INTEGER NOT NULL,
    comment TEXT NOT NULL,
    FOREIGN KEY (professor_id) REFERENCES professor(id)
);