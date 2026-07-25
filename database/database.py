import sqlite3
from datetime import datetime
from pathlib import Path

# 1. Get the 'database' folder path
DB_FOLDER_PATH = Path(__file__).resolve().parent

# 2. Go UP one level to the root folder (root_folder)
ROOT_DIR = DB_FOLDER_PATH.parent

# 3. Now go DOWN into the 'data' folder to find notes.db
DB_PATH = ROOT_DIR / "data" / "notes.db"


def create_connection():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS notes (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT NOT NULL,
                            content TEXT,
                            created_at TEXT NOT NULL,
                            updated_at TEXT NOT NULL)'''
    )
    conn.commit()
    return conn

def add_note(title, content):
    conn = create_connection()
    cursor = conn.cursor()
    now = datetime.now().isoformat()
    cursor.execute('''INSERT INTO notes (title, content, created_at, updated_at) VALUES (?, ?, ?, ?)''',
                   (title, content, now, now))
    conn.commit()
    conn.close()

def get_all_notes():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes ORDER BY updated_at DESC")
    notes = cursor.fetchall()
    conn.close()
    return notes

def update_note(note_id, title, content):
    conn = create_connection()
    cursor = conn.cursor()
    now = datetime.now().isoformat()
    cursor.execute(
        "UPDATE notes SET title = ?, content = ?, updated_at = ? WHERE id = ?",
        (title, content, now, note_id)
    )
    conn.commit()
    conn.close()

def delete_note(note_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    conn.close()
