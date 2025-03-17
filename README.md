# DatabaseAuto_assign3

Project Overview
This is a simple web application built with Flask that includes a login form. The user submits their username and password, which are stored in a MySQL database. The application also includes an automated Selenium script to test the login functionality and validate that the data is correctly inserted into the MySQL database.

Prerequisites
Before you begin, ensure you have the following installed:

Python 3.x
MySQL Server
pip (Python package installer)
Selenium
Flask
MySQL Connector (or PyMySQL as an alternative)
Setup Instructions
Step 1: Install Python Dependencies
Create and activate a virtual environment (optional but recommended):


python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the necessary Python packages:


pip install flask mysql-connector-python selenium
If you're using PyMySQL instead of mysql-connector-python, install it with:


pip install pymysql
Step 2: Setup MySQL Database
Log into your MySQL server:


mysql -u root -p
Create a new database:

sql
Copy
Edit
CREATE DATABASE flask_app;
You can also manually create a users table with the following command, though the app will automatically create it if it doesn't exist:


CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);
Step 3: Configure Database Credentials
In app.py, update the database connection settings with your MySQL credentials:

python
Copy
Edit
db_config = {
    "host": "localhost",          # MySQL host
    "user": "root",               # MySQL username
    "password": "Mayank@1234",  # MySQL password
    "database": "flask_app"       # Database name
}
Step 4: Run the Flask Application
Run the Flask application:


python app.py
The web application will be available at http://127.0.0.1:5000 in your browser.

Step 5: Running the Selenium Tests
Install a web driver for Selenium (e.g., ChromeDriver for Chrome).

Modify the Selenium script (test_login.py) to match your application URL and credentials.

Run the Selenium script to automate the login process and validate that the data was inserted into the database:


python test_login.py
