import sqlite3
    
conn = sqlite3.connect(database="tasks.db")

query = """
    CREATE TABLE IF NOT EXISTS my_task(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL, 
    description TEXT,
    due_date TEXT,
    is_completed INTEGER DEFAULT 0
    )
        """
conn.execute(query)
conn.commit()

query = "INSERT INTO my_task (title, description, due_date, is_completed) VALUES (?, ?, ?, ?)"
conn.execute(query, ("exercise", "football", "2025-11-23 20:00:00", 1))
conn.commit()

query = "SELECT * FROM my_task"
cursor = conn.execute(query)
print(cursor.fetchall())

query = "DELETE FROM my_task WHERE id = ?"
conn.execute(query, (1,))
conn.commit()

conn.close()
