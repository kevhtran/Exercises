DROP DATABASE IF EXISTS soccer_db;
CREATE DATABASE soccer_db;
\c soccer_db

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    team_name TEXT  NOT NULL,
    city_name TEXT  NOT NULL
);

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    player_name TEXT NOT NULL,
    player_birthday TEXT NOT NULL,
    player_height TEXT NOT NULL,
    current_team_id INTEGER REFERENCES teams ON DELETE SET NULL 
);
CREATE TABLE referees (
    id SERIAL PRIMARY KEY,
    referee_name TEXT NOT NULL
);

CREATE TABLE season (
    id SERIAL PRIMARY KEY,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL
);

CREATE TABLE matches (
    id SERIAL PRIMARY KEY,
    home_team_id INTEGER REFERENCES teams ON DELETE SET NULL,
    away_team_id INTEGER REFERENCES teams ON DELETE SET NULL,
    location TEXT NOT NULL,
    date TEXT NOT NULL,
    start_time TEXT NOT NULL,
    season_id INTEGER REFERENCES season ON DELETE SET NULL,
    head_referee_id INTEGER REFERENCES referees ON DELETE SET NULL
);
CREATE TABLE results (
    id SERIAL PRIMARY KEY,
    team_id INTEGER REFERENCES teams ON DELETE SET NULL,
    match_id INTEGER REFERENCES matches ON DELETE SET NULL,
    results TEXT NOT NULL
);
CREATE TABLE goals (
    id SERIAL PRIMARY KEY,
    player_id INTEGER REFERENCES players ON DELETE SET NULL 
    match_id INTEGER REFERENCES matches ON DELETE SET NULL 
);
CREATE TABLE lineups (
    id SERIAL PRIMARY KEY,
    player_id INTEGER REFERENCES players ON DELETE SET NULL,
    match_id INTEGER REFERENCES matches ON DELETE SET NULl,
    team_id INTEGER REFERENCES teams ON DELETE SET NULL
);