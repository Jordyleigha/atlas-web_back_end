#!/usr/bin/env python3
"""function called filter_datum that returns the log message obfuscated"""
import os
import mysql.connector
from mysql.connector import connection
from typing import List
import logging

logging.basicConfig(
    format="[HOLBERTON] user_data INFO %(asctime)s: %(message)s",
    level=logging.INFO
)

logging.getLogger("mysql.connector").setLevel(logging.ERROR)


def get_db() -> connection.MySQLConnection:
    """returns a connector to a database"""
    db_username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    db_password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    db_host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME', 'my_db')
    db_connection = mysql.connector.connect(
        user=db_username,
        password=db_password,
        host=db_host,
        database=db_name
    )
    return db_connection


def main():
    """connects to db, retrieves user data,
    and logs each row with sensitive fields obfuscated"""
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users;")
    rows = cursor.fetchall()
    for row in rows:
        name = "***"
        email = "***"
        phone = "***"
        ssn = "***"
        password = "***"
        ip = row['ip']
        last_login = row['last_login']
        user_agent = row['user_agent']
        log_message = (
            f"name={name}; email={email}; phone={phone}; ssn={ssn};"
            f"password={password}; ip={ip}; last_login={last_login};"
            f"user_agent={user_agent};"
        )
        logging.info(log_message)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
