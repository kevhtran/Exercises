DROP DATABASE IF EXISTS craigslist_db;
CREATE DATABASE craigslist_db;
\c craigslist_db

CREATE TABLE regions (
    id SERIAL PRIMARY KEY,
    region_name TEXT   NOT NULL
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL
    preferred_region TEXT NOT NULL
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    category_name TEXT NOT NULL
);

CREATE TABLE patient_chart (
    id SERIAL PRIMARY KEY,
    title text,
    test text,
    post_location text,
    regions_id INTEGER REFERENCES regions ON DELETE SET NULL,
    users_id INTEGER REFERENCES users ON DELETE SET NULL,
    categories_id INTEGER REFERENCES categories ON DELETE SET NULL
);