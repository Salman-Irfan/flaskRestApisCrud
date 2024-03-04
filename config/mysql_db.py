# config/mysql_db.py

import mysql.connector

# Function to establish a MySQL database connection
def get_mysql_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="flask_tutorial"
    )
