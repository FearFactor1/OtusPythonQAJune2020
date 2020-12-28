import psycopg2

from types import SimpleNamespace
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

config = SimpleNamespace(
    DB_NAME='contacts_db',
    TABLE='contacts',
    HOST='0.0.0.0',
    PORT='3306',
    USER='root',
    PASSWORD='root',
)

connection = psycopg2.connect(
    user=config.USER,
    password=config.PASSWORD,
    host=config.HOST,
    port=config.PORT
)

connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Getting cursor object from connection
cursor = connection.cursor()

# Creating database
try:
    create_database = f"CREATE DATABASE {config.DB_NAME};"
    cursor.execute(create_database)
except psycopg2.errors.DuplicateDatabase as e:
    print(e)

# Switch to created database
cursor.execute(f"USE {config.DB_NAME}")
