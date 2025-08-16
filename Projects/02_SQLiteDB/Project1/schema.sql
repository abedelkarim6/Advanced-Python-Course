CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS tips (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    category_id INTEGER,
    is_favorite INTEGER DEFAULT 0,
    created_at TEXT,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);