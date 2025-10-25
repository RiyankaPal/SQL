import sqlite3
import os

os.makedirs("data", exist_ok=True)

conn = sqlite3.connect('data/sample.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS departments (
    dept_id INTEGER PRIMARY KEY,
    dept_name TEXT
)
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS employees (
    emp_id INTEGER PRIMARY KEY,
    emp_name TEXT,
    dept_id INTEGER,
    salary REAL,
    FOREIGN KEY(dept_id) REFERENCES departments(dept_id)
)
''')

cur.executemany("INSERT INTO departments VALUES (?, ?)", [
    (1, 'IT'), (2, 'HR'), (3, 'Finance')
])

cur.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", [
    (101, 'Ram', 1, 70000),
    (102, 'Ankit', 1, 60000),
    (103, 'Meena', 2, 50000),
    (104, 'Sourav', 3, 80000)
])

conn.commit()
conn.close()
print("✅ Database created with sample data.")
