from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import mysql.connector

# Start Selenium WebDriver
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5000/")

# Wait for the username and password fields to be present
wait = WebDriverWait(driver, 10)  # Wait for a maximum of 10 seconds
username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
password = wait.until(EC.presence_of_element_located((By.NAME, "password")))

# Fill out the login form
username.send_keys("testuser")
password.send_keys("testpass")
password.send_keys(Keys.RETURN)

# Wait for form submission to complete (optional, depending on your app)
time.sleep(2)

# Check database entry
conn = mysql.connector.connect(host="localhost", user="root", password="password", database="flask_db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM users WHERE username='testuser'")
result = cursor.fetchone()

if result:
    print("Test Passed: User successfully added to the database.")
else:
    print("Test Failed: User not found in the database.")

# Close connections
cursor.close()
conn.close()
driver.quit()
