from sqlite.config import connection, config

cursor = connection.cursor()

sql = f"SELECT * FROM {config.TABLE} WHERE name = ?"

request_result = cursor.execute(sql, ('Vasiliy',))

# Fetch results as list
print(request_result.fetchall())

# Wont work if data was fetched
for el in request_result:
    print(el)

connection.close()
