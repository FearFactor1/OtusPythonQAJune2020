from mysql_example.config import config
from mysql_example.config import connection, cursor

# Creating table inside database using external sql file
with open("contacts_table.sql", "r") as script:
    cursor.execute(script.read())

# Inserting single data entry
sql = f"INSERT INTO {config.TABLE} (name, phone, email, address) VALUES (%s, %s, %s, %s)"
values = ("Vasya1", "89009009999", None, "Moscow")
cursor.execute(sql, values)
connection.commit()

# Inserting multiple lines
values = [
    ("Vasya000", "89009009569", None, "Moscow"),
    ("Vasya2", "89009057699", None, "London"),
    ("Vasya3", "89065709999", "no@mail.ru", "Minsk"),
    ("Vasya5", "89009765999", None, "Petropavlovsk"),
]

sql = f"INSERT INTO {config.TABLE} (name, phone, email, address) VALUES (%s, %s, %s, %s)"
cursor.executemany(sql, values)
connection.commit()

cursor.close()
connection.close()
