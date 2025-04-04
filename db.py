import sqlite3

def init_db():
    conn = sqlite3.connect("cyfinebot.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            car_number TEXT,
            arc_number TEXT
        )
    ''')
    conn.commit()
    conn.close()