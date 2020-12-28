from postgres_example.config import connection, cursor

# Execute delete data query
cursor.execute("DELETE FROM contacts_app WHERE name='Test'")
connection.commit()

# CLosing connections
cursor.close()
connection.close()