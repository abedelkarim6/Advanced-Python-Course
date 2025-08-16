# Streamlit Assignments

This repository contains three separate projects, all implemented using **Streamlit**.  

---

## 1. Chatbot with Streamlit GUI (Optional)

**Goal**:  
Take the chatbot built in the previous assignment and implement a simple **Streamlit interface** for it.  

**Features**:
- Input box for the user to type messages.  
- Display the conversation in a chat-like interface.  
- Show both user messages and chatbot responses dynamically.  

---

## 2. Excel Comparator App

**Goal**:  
Create a **Streamlit application** that compares two Excel files.

**Requirements**:
- Upload two Excel files (`file1.xlsx` and `file2.xlsx`) through the Streamlit file uploader.  
- Clean the data by removing rows with null values.  
- Provide **basic insights** (row count, column names, number of nulls before cleaning, etc.).  
- Match between the **names** in both files.  
- If names match → compare the **amounts** for correctness.  

**Example Data**:  
You can test using these sample Excel files:  
- [File 1 Example](https://docs.google.com/spreadsheets/d/1_G7Qp3hRN6H1X66qQaNtnfzNbhTYhTc7/edit?usp=drive_link&ouid=108718846898525631624&rtpof=true&sd=true)  
- [File 2 Example](https://docs.google.com/spreadsheets/d/1z_AAACrLgGiScFofDYKraxecDjNQaCvy/edit?usp=drive_link&ouid=108718846898525631624&rtpof=true&sd=true)  

---

## 3. Courses Registration Platform (3 Pages)

**Goal**:  
Build a **3-page Streamlit application** to manage course registration.  

**Pages**:
1. **Admin Dashboard**  
   - Show all registered students.  
   - Display summary statistics on course registrations.  

2. **Available Courses**  
   - Display list of all available courses.  
   - Each course should have a **title** and **description**.  

3. **Registration Form**  
   - Allow students to fill in their details (name, email, etc.).  
   - Select a course to register.  
   - Submit data to the database.  

**Database**:
- Use **SQLite** to store:  
  - `courses` table (course_id, name, description)  
  - `students` table (student_id, name, email, registered_course_id)  

---