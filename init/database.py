import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), "../schema.db")
schema_path = os.path.join(os.path.dirname(__file__), "schema.sql")

if os.path.exists(db_path):
    connection = sqlite3.connect(db_path)
    with open(schema_path, "r") as f:
        cursor = connection.cursor()
        cursor.executescript(f.read())
    connection.commit()
else:
    print("Database not exists at: " + db_path)
