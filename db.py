# db.py
import sqlite3
from datetime import datetime

# ✅ Initializes the database and creates the students table
def init_db():
    with sqlite3.connect("students.db") as conn:
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                roll_no TEXT UNIQUE,
                department TEXT,
                year TEXT,
                email TEXT,
                phone TEXT,
                updated_on TEXT
            )
        ''')
        conn.commit()

# ✅ Adds a new student
def add_student(name, roll_no, department, year, email, phone):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with sqlite3.connect("students.db") as conn:
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO students (name, roll_no, department, year, email, phone, updated_on)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (name, roll_no, department, year, email, phone, now))
        conn.commit()

# ✅ Returns a list of all students
def list_students():
    with sqlite3.connect("students.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM students")
        return cur.fetchall()

# ✅ Searches for a student by roll number
def find_student_by_roll(roll_no):
    with sqlite3.connect("students.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM students WHERE roll_no=?", (roll_no,))
        return cur.fetchone()

# ✅ Updates an existing student record
def update_student(roll_no, name, department, year, email, phone):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with sqlite3.connect("students.db") as conn:
        cur = conn.cursor()
        cur.execute('''
            UPDATE students
            SET name=?, department=?, year=?, email=?, phone=?, updated_on=?
            WHERE roll_no=?
        ''', (name, department, year, email, phone, now, roll_no))
        conn.commit()

# ✅ Deletes a student by roll number
def remove_student(roll_no):
    with sqlite3.connect("students.db") as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM students WHERE roll_no=?", (roll_no,))
        conn.commit()
