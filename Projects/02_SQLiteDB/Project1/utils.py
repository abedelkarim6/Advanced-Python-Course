import sqlite3
from datetime import datetime

# Connect to DB
conn = sqlite3.connect("tips.db")
cursor = conn.cursor()

with open("schema.sql", "r") as file:
    script = file.read()

cursor.executescript(script)
conn.commit()
print("✅ Database connected and schema initialized.")


# -------------------- Functions --------------------
def add_category(name):
    cursor.execute("INSERT INTO categories (name) VALUES (?)", (name,))
    conn.commit()


def add_tip(title, content, category_id):
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(
        """
        INSERT INTO tips (title, content, category_id, created_at)
        VALUES (?, ?, ?, ?)
    """,
        (title, content, category_id, created_at),
    )
    conn.commit()


def update_tip(tip_id, title=None, content=None, category_id=None):
    fields, values = [], []
    if title:
        fields.append("title = ?")
        values.append(title)
    if content:
        fields.append("content = ?")
        values.append(content)
    if category_id:
        fields.append("category_id = ?")
        values.append(category_id)

    if not fields:
        return  # No update

    values.append(tip_id)
    query = f"UPDATE tips SET {', '.join(fields)} WHERE ID = ?"
    cursor.execute(query, values)
    conn.commit()


def delete_tip(tip_id):
    cursor.execute("DELETE FROM tips WHERE ID = ?", (tip_id,))
    conn.commit()


def filter_by_category(category_id):
    cursor.execute(
        """
        SELECT tips.ID, tips.title, categories.name, tips.created_at
        FROM tips
        JOIN categories ON tips.category_id = categories.category_id
        WHERE categories.category_id = ?
    """,
        (category_id,),
    )
    return cursor.fetchall()


def search_by_keyword(keyword):
    cursor.execute(
        """
        SELECT ID, title, content
        FROM tips
        WHERE title LIKE ? OR content LIKE ?
    """,
        (f"%{keyword}%", f"%{keyword}%"),
    )
    return cursor.fetchall()


def mark_favorite(tip_id):
    cursor.execute(
        """
        UPDATE tips SET is_favorite = CASE WHEN is_favorite = 0 THEN 1 ELSE 0 END
        WHERE ID = ?
    """,
        (tip_id,),
    )
    conn.commit()


def get_recent_tips(limit=5):
    cursor.execute(
        """
        SELECT ID, title, created_at
        FROM tips
        ORDER BY datetime(created_at) DESC
        LIMIT ?
    """,
        (limit,),
    )
    return cursor.fetchall()


def get_categories():
    cursor.execute("SELECT category_id, name FROM categories")
    return cursor.fetchall()
