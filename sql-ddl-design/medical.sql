DROP DATABASE IF EXISTS med_db;
CREATE DATABASE med_db;
\c med_db

CREATE TABLE medical_center (
    id SERIAL PRIMARY KEY,
    physician TEXT   NOT NULL
);

CREATE TABLE diseases (
    id SERIAL PRIMARY KEY,
    disease_name TEXT NOT NULL
);

CREATE TABLE patients (
    id SERIAL PRIMARY KEY,
    patient_name TEXT NOT NULL,
    DOB TEXT NOT NULL
);

CREATE TABLE patient_chart (
    id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients ON DELETE SET NULL,
    attending_id INTEGER REFERENCES medical_center ON DELETE SET NULL,
    disease_id INTEGER REFERENCES diseases ON DELETE SET NULL
);