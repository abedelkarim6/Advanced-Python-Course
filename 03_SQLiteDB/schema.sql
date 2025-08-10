-- ONE-TO-ONE: Each student has one profile
CREATE TABLE Students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE StudentProfiles (
    profile_id INTEGER PRIMARY KEY,
    student_id INTEGER UNIQUE,  -- Ensures one-to-one
    birthdate TEXT,
    email TEXT,
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
);

-- ONE-TO-MANY: One course is taught by one instructor, but an instructor teaches many courses
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

-- MANY-TO-MANY: Students enroll in many courses, and each course has many students
CREATE TABLE Enrollments (
    student_id INTEGER,
    course_id INTEGER,
    enrollment_date TEXT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);
