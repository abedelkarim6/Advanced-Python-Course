# Tips Management App

This project is a **Streamlit application** backed by a **SQLite database** that allows users to manage and explore tips effectively.  

---

## Features

### Core Features
- **Add Tips**: Create new tips with a title, content, and category.  
- **Update Tips**: Edit existing tips.  
- **Delete Tips**: Remove tips from the database.  
- **Filter by Category**: View tips belonging to a specific category.  
- **Search by Keyword**: Quickly find tips using text search.  
- **Mark Favorites**: Highlight important tips by marking them as favorites.  
- **Recent Tips**: Display the latest tips sorted by date.  

### Bonus Features
- **Random Tip of the Day**: Display a random tip for inspiration.  
- **Export to CSV**: Download all tips as a `.csv` file.  
- **Markdown Formatting**: Tips can be written using **Markdown-style** text for better readability.  

---

## Database Schema

The app uses **SQLite** with two tables:  

```sql
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
