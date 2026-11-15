import sqlite3

def get_connection():
    connect = sqlite3.connect('database.db')
    connect.row_factory = sqlite3.Row

    return connect

def create_user():
    connect = get_connection()
    connect.execute("""
        CREATE TABLE IF NOT EXISTS user(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            name TEXT NOT NULL
        )
    """)
    connect.commit()
    connect.close()
    print("Table user Created")

create_user()
