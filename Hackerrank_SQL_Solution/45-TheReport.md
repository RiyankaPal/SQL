# The Report
## Problem Statement :
You are given two tables: Students and Grades. Students contains three columns ID, Name and Marks.<br>

![](./Images/STUDENT.PNG)<br>

Grades contains the following data:<br>

![](./Images/Grades.PNG)<br>

Ketty gives Eve a task to generate a report containing three columns: Name, Grade and Mark. Ketty doesn't want the NAMES of those students who received a grade lower than 8. The report must be in descending order by grade -- i.e. higher grades are entered first. If there is more than one student with the same grade (8-10) assigned to them, order those particular students by their name alphabetically. Finally, if the grade is lower than 8, use "NULL" as their name and list them by their grades in descending order. If there is more than one student with the same grade (1-7) assigned to them, order those particular students by their marks in ascending order.<br>

Write a query to help Eve.<br>

Sample Input<br>
![](./Images/TheReport_Data.PNG)<br>

Sample Output<br>

```
Maria 10 99
Jane 9 81
Julia 9 88 
Scarlet 8 78
NULL 7 63
NULL 7 68

```
Note

Print "NULL"  as the name if the grade is less than 8.

Explanation

Consider the following table with the grades assigned to the students:<br>
![](./Images/TheReport_Data1.PNG)<br>

So, the following students got 8, 9 or 10 grades:

- Maria (grade 10)
- Jane (grade 9)
- Julia (grade 9)
- Scarlet (grade 8)

# Solution :

``` SQL
SELECT 
    CASE
    WHEN grades.grade < 8 THEN 'NULL'
    ELSE students.name
    END,
    grades.grade, students.marks
    FROM students, grades 
   WHERE students.marks >= grades.min_mark AND students.marks <= grades.max_mark
   ORDER BY grades.grade DESC, students.name







