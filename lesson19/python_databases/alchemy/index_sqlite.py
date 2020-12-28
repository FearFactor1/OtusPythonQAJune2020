from sqlalchemy import Table
from sqlalchemy import MetaData, create_engine
from sqlalchemy import select, insert

metadata = MetaData()

# First we need to create the table
engine = create_engine('sqlite:///../sqlite/contacts_db.sqlite')

contacts = Table('contacts', metadata, autoload=True, autoload_with=engine)

print(contacts.columns.keys())

# Prepare the request
s = select([contacts]).limit(2)

# Getting rows
rows = engine.execute(s).fetchall()

# Iterate over rows
for row in rows:
    print(row)

# Prepare and execute insert statement
i = insert(contacts).values(name="Test", email="test@mail.ru", phone="11111111111")
engine.execute(i)
