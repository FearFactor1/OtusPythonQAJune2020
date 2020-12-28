import sqlite3
from sqlite.config import connection, config

cursor = connection.cursor()

# cursor.execute("DROP TABLE contacts_app;")
# cursor.execute(f"DROP TABLE IF EXISTS {config.TABLE};")

sql = f"DELETE FROM {config.TABLE} WHERE name = ?"

cursor.execute(sql, ("Vasiliy",))
connection.commit()

connection.close()