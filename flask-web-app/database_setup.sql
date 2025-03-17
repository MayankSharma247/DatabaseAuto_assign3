-- Create the database
CREATE DATABASE IF NOT EXISTS flask_app;

-- Use the database
USE flask_app;

-- Create the users table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);

