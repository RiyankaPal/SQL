# Top Earners
## Problem Statement
We define an employee's total earnings to be their monthly salary*months  worked, and the maximum total earnings to be the maximum total earnings for any employee in the Employee table. Write a query to find the maximum total earnings for all employees as well as the total number of employees who have maximum total earnings. Then print these values as 2 space-separated integers.

Input Format

The Employee table containing employee data for a company is described as follows:<br>
![](./Images/Employee.PNG)<br><br>
where employee_id is an employee's ID number, name is their name, months is the total number of months they've been working for the company, and salary is the their monthly salary.

Sample Input<br>
![](./Images/Top_Earners_data.PNG)<br><br>

Sample Output<br>
``` 
69952  1

```
The maximum earnings value is 69952.The only employee with earnings=69952 is Kimberly, so we print the maximum earnings value (69952) and a count of the number of employees who have earned $69952  (which is 1) as two space-separated values.

## Solution:
``` SQL
SELECT MAX(SALARY*MONTHS), COUNT(*)
FROM EMPLOYEE
WHERE (SALARY*MONTHS) = (SELECT MAX(SALARY*MONTHS)
                         FROM EMPLOYEE)

