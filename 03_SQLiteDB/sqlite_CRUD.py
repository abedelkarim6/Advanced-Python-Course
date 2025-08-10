import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# === CREATE TABLES ===
cursor.executescript('''
DROP TABLE IF EXISTS Enrollments;
DROP TABLE IF EXISTS StudentProfiles;
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Instructors;
DROP TABLE IF EXISTS Students;

CREATE TABLE Students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE StudentProfiles (
    profile_id INTEGER PRIMARY KEY,
    student_id INTEGER UNIQUE,
    birthdate TEXT,
    email TEXT,
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
);

CREATE TABLE Instructors (
    instructor_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE Courses (
    course_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    instructor_id INTEGER,
    FOREIGN KEY (instructor_id) REFERENCES Instructors(instructor_id)
);

CREATE TABLE Enrollments (
    student_id INTEGER,
    course_id INTEGER,
    enrollment_date TEXT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);
''')

# === C: CREATE (INSERT) ===
cursor.execute("INSERT INTO Students (student_id, name) VALUES (?, ?)", (1, 'Alice'))
cursor.execute("INSERT INTO Students (student_id, name) VALUES (?, ?)", (2, 'Bob'))

cursor.execute("INSERT INTO StudentProfiles (profile_id, student_id, birthdate, email) VALUES (?, ?, ?, ?)",
               (1, 1, '2000-01-01', 'alice@example.com'))

cursor.execute("INSERT INTO Instructors (instructor_id, name) VALUES (?, ?)", (1, 'Dr. Smith'))
cursor.execute("INSERT INTO Courses (course_id, title, instructor_id) VALUES (?, ?, ?)",
               (1, 'Math 101', 1))

cursor.execute("INSERT INTO Enrollments (student_id, course_id, enrollment_date) VALUES (?, ?, ?)",
               (1, 1, '2025-06-01'))

conn.commit()

# === R: READ (SELECT) ===
print("All students:")
for row in cursor.execute("SELECT * FROM Students"):
    print(row)

print("\nEnrollments with student names and course titles:")
cursor.execute('''
SELECT Students.name, Courses.title, Enrollments.enrollment_date
FROM Enrollments
JOIN Students ON Students.student_id = Enrollments.student_id
JOIN Courses ON Courses.course_id = Enrollments.course_id;
''')
for row in cursor.fetchall():
    print(row)

# === U: UPDATE ===
cursor.execute("UPDATE Students SET name = ? WHERE student_id = ?", ('Alice Johnson', 1))
conn.commit()
print("\nUpdated student name:")
print(cursor.execute("SELECT * FROM Students WHERE student_id = 1").fetchone())

# === D: DELETE ===
cursor.execute("DELETE FROM Enrollments WHERE student_id = ? AND course_id = ?", (1, 1))
conn.commit()
print("\nEnrollments after deletion:")
print(cursor.execute("SELECT * FROM Enrollments").fetchall())

# Close connection
conn.close()
