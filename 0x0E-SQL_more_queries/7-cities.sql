-- A script that creates a database hbtn_0dd_usa and table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
    id INT AUTO_INCREMENT PRIMARY KEY,
    FOREIGN KEY(state_id) REFERENCES states(id) NOT NULL,
    name VARCHAR(256) NOT NULL
);
