import sqlite3

def init_db():
    conn = sqlite3.connect('database/database.db')
    conn.execute('CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, name TEXT NOT NULL, value TEXT NOT NULL)')
    conn.close()

if __name__ == "__main__":
    init_db()
