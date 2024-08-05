# New Companies
## Amber's conglomerate corporation just acquired some new companies. Each of the companies follows this hierarchy:<br>
![](./Images/Company_diag.PNG)<br>
Given the table schemas below, write a query to print the company_code, founder name, total number of lead managers, total number of senior managers, total number of managers, and total number of employees. Order your output by ascending company_code.<br>

**Note:**<br>

- The tables may contain duplicate records.<br>
- The company_code is string, so the sorting should not be numeric. For example, if the company_codes are C_1, C_2, and C_10, then the ascending company_codes will be C_1, C_10, and C_2.<br>
Input Format<br>
The following tables contain company data:<br>

- Company: The company_code is the code of the company and founder is the founder of the company. <br>
![](./Images/Company.PNG)<br>
-Lead_Manager: The lead_manager_code is the code of the lead manager, and the company_code is the code of the working company.<br>
![](./Images/LeadManager.PNG)<br>
- Senior_Manager: The senior_manager_code is the code of the senior manager, the lead_manager_code is the code of its lead manager, and the company_code is the code of the working company.<br>
![](./Images/SeniorManager.PNG)<br>
- Manager: The manager_code is the code of the manager, the senior_manager_code is the code of its senior manager, the lead_manager_code is the code of its lead manager, and the company_code is the code of the working company.<br>
![](./Images/Manager.PNG)<br>
- Employee: The employee_code is the code of the employee, the manager_code is the code of its manager, the senior_manager_code is the code of its senior manager, the lead_manager_code is the code of its lead manager, and the company_code is the code of the working company.<br>
![](./Images/Employee.PNG)<br>
Sample Input<br>
Company Table:<br>
![](./Images/Company_data.PNG)<br>
Lead_Manager Table:<br>
![](./Images/Lead_Manager_data.PNG)<br>
Senior_Manager Table:<br>
![](./Images/SeniorManagerData.PNG)<br>

![](./Images/Manager_Data.PNG)<br>

![](./Images/Employee_Data.PNG)<br>
Sample Output<br>
```
C1 Monika 1 2 1 2
C2 Samantha 1 1 2 2
```
Explanation <br>

In company C1, the only lead manager is LM1. There are two senior managers, SM1 and SM2, under LM1. There is one manager, M1, under senior manager SM1. There are two employees, E1 and E2, under manager M1.<br>

In company C2, the only lead manager is LM2. There is one senior manager, SM3, under LM2. There are two managers, M2 and M3, under senior manager SM3. There is one employee, E3, under manager M2, and another employee, E4, under manager, M3.<br>

## Solution :
```SQL
SELECT A.company_code,founder,
             Count(DISTINCT B.lead_manager_code) as lead_count,
             COUNT(DISTINCT C.senior_manager_code) as senior_count,
             COUNT(DISTINCT D.Manager_code) as Manager_count,
             COUNT(DISTINCT E.Employee_code) as Employee_count
FROM Company A
JOIN Lead_Manager B 
ON A.company_code=B.company_code
JOIN Senior_Manager C
ON  B.lead_manager_Code=C.lead_manager_Code
JOIN Manager D
ON  C.senior_manager_code=D.senior_manager_code 
JOIN Employee E
ON D.manager_code=E.manager_Code 
group by A.company_code,founder
order by A.company_code ASC








