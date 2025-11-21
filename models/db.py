import sqlite3

# Создаём или подключаемся к базе
conn = sqlite3.connect("database.db", check_same_thread=False)
cursor = conn.cursor()

# Создаём таблицу tasks, если её нет
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
)
""")

conn.commit()