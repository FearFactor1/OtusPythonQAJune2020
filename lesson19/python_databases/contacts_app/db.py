import sqlite3

DB = "contacts"


class SqliteConnector:
    connection = None

    def __init__(self, db_name):
        self.connect(db_name)
        with open("sqls/contacts.sql", "r") as script:
            self.connection.execute(script.read())
        self.cursor = self.connection.cursor()

    @classmethod
    def connect(cls, db_name):
        if cls.connection is None:
            cls.connection = sqlite3.connect(db_name)


def close_connection():
    contacts_db().connection.close()


def contacts_db():
    return SqliteConnector("database.db")


def _execute(sql=None, params=None):
    db = contacts_db()
    try:
        if params:
            db.cursor.execute(sql, params)
        else:
            db.cursor.execute(sql)
        db.connection.commit()
    except sqlite3.OperationalError as e:
        print(f"Oooops... something is broken. {e}")


def insert_contact(params: tuple):
    sql = f"INSERT INTO {DB} (name, email, phone, address) VALUES (?, ?, ?, ?)"
    _execute(sql=sql, params=params)


def delete_contact(name):
    sql = f"DELETE FROM {DB} WHERE name = ?"
    _execute(sql=sql, params=(name,))


def select_contact(name):
    db = contacts_db()
    sql = f"SELECT * FROM {DB} WHERE name = ?"
    result = db.cursor.execute(sql, (name,)).fetchone()
    return result


def get_all_rows():
    # https://stackoverflow.com/questions/31745613/fetching-mysql-data-as-python-dictionary
    db = contacts_db()
    result = db.cursor.execute(f"SELECT * FROM {DB}")
    if result:
        return result.fetchall()
    else:
        return []


def update_contact(name, field, new_value):
    sql = f"UPDATE contacts_app SET {field} = '{new_value}' WHERE name = '{name}'"
    _execute(sql=sql)
