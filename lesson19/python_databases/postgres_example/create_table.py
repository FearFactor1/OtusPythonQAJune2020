import psycopg2
from postgres_example.config import connection, cursor

try:
    with open("contacts_table.sql", "r") as script:
        cursor.execute(script.read())
except psycopg2.errors.DuplicateTable as e:
    print(e)

cursor.close()
connection.close()
