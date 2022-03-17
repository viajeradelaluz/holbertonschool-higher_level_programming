-- Creates the database 'hbtn_0d_usa' and inside the table 'states':
-- * id INT unique, auto generated, can’t be null and is a primary key
-- * name VARCHAR(256) can’t be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
