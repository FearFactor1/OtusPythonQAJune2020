from mysql_example.config import config
from mysql_example.config import connection, cursor

# Выполняем запрос
cursor.execute(f"SELECT * FROM {config.TABLE}")

# Getting all available rows
for row in cursor.fetchall():
    print(row)

# Getting first entry
print(cursor.fetchone())
cursor.reset()

# Close connection and cursor
cursor.close()
connection.close()
