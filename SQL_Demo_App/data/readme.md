# 🧠 SQL Query Demo App

This is an **interactive SQL demo app** built using Python and Streamlit.  
It allows you to explore predefined SQL queries on a sample SQLite database.

---

## 📂 Project Structure

sql_demo_app/
│
├── data/
│ └── sample.db # SQLite database with sample tables
│
├── queries/
│ └── queries.json # Stores query names and SQL statements
│
├── setup_db.py # Script to create tables and insert sample data
├── app.py # Main Streamlit app
└── requirements.txt # Required Python packages


---

## ⚙️ Setup Instructions

1. **Clone or download the repository**  

2. **Install dependencies** (ensure Python 3.7+ is installed):
```bash
pip install streamlit pandas
```
3. **Set up the database (run this once to create sample tables and data):**

```bash 
python setup_db.py
```


4. **Run the Streamlit app:**

```bash 
streamlit run app.py
```


5. **Open the app in your browser**
Streamlit will display a URL in your terminal, usually:
```arduino
http://localhost:8501
```
## 🗂 Database

The app uses a **SQLite database** located at `data/sample.db`.

### Tables Included

#### 1. `departments`
| Column    | Type                 |
|-----------|--------------------|
| dept_id   | INTEGER PRIMARY KEY |
| dept_name | TEXT               |

#### 2. `employees`
| Column    | Type                               |
|-----------|-----------------------------------|
| emp_id    | INTEGER PRIMARY KEY                |
| emp_name  | TEXT                               |
| dept_id   | INTEGER (foreign key → departments.dept_id) |
| salary    | REAL                               |

## 🔍 Available Queries

These queries are available in the app dropdown:

### 1. All Employees
```sql
SELECT * FROM employees;
```

### 2. All Departments
```sql
SELECT * FROM departments;
```

### 3. Employee Details with Department
```sql
SELECT e.emp_name, d.dept_name, e.salary
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id;
```
### 4. Average Salary by Department
```sql
SELECT d.dept_name, AVG(e.salary) AS avg_salary
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_name;
```
### 5. Employees with Salary > X (user-input parameter)
```sql
SELECT * FROM employees WHERE salary > ?;
```
## 🚀 How to Use

1. Open the app in your browser.

2. Select a query from the dropdown menu.

3. If the query requires a parameter (e.g., salary threshold), enter a value.

4. Click Run Query to display the results.

5. Optionally, expand Show SQL to view the SQL statement.

