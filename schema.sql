DROP TABLE IF EXISTS professor;

CREATE TABLE professor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    rating_numerator INTEGER NOT NULL,
    rating_denominator INTEGER NOT NULL,
    classes TEXT NOT NULL,
    would_take_percentage INTEGER NOT NULL,
    difficulty FLOAT NOT NULL,
    reviews TEXT NOT NULL
);