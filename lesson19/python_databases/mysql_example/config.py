import mysql.connector
from types import SimpleNamespace

config = SimpleNamespace(
    DB_NAME='contacts_db',
    TABLE='contacts',
    HOST='0.0.0.0',
    PORT='3306',
    USER='root',
    PASSWORD='root',
)

connection = mysql.connector.connect(
    user=config.USER,
    password=config.PASSWORD,
    host=config.HOST,
    port=config.PORT
)

# Getting cursor object from connection
cursor = connection.cursor()

# Creating database
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {config.DB_NAME} DEFAULT CHARACTER SET 'utf8'")

# Switch to created database
cursor.execute(f"USE {config.DB_NAME}")
