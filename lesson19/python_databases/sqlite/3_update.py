from sqlite.config import connection, config


cursor = connection.cursor()

# Bad example because hardcoded data!!!
sql = f"UPDATE {config.TABLE} SET address = 'TEST' WHERE name = 'Vasiliy'"

cursor.execute(sql)
connection.commit()

sql = "UPDATE contacts_app SET name = ? WHERE name = ?"
data = ("HELLOTEST", "Vasiliy")

cursor.execute(sql, data)
connection.commit()

connection.close()