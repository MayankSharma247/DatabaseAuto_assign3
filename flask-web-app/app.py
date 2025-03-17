from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for flashing messages

# Database configuration
db_config = {
    "host": "localhost",
    "user": "root",        # Change to your MySQL username
    "password": "Mayank@1234",  # Change to your MySQL password
    "database": "flask_app"  # Change to your database name
}

# Connect to MySQL database
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Create users table if not exists
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(100) NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Insert user data into database
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            conn.commit()
            flash("User registered successfully!", "success")
            return redirect(url_for("success"))
        except mysql.connector.IntegrityError:
            flash("Username already exists. Try another.", "danger")
        finally:
            cursor.close()
            conn.close()

    return render_template("index.html")

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    create_table()  # Ensure the table is created before running
    app.run(debug=True)

