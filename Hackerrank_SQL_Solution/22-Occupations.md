# Occupations

## Problem Statement:
[Pivot](https://en.wikipedia.org/wiki/Pivot_table) the Occupation column in OCCUPATIONS so that each Name is sorted alphabetically and displayed underneath its corresponding Occupation. The output column headers should be Doctor, Professor, Singer, and Actor, respectively.<br>
**Note: Print NULL when there are no more names corresponding to an occupation.**
<br> Input Format
The OCCUPATIONS table is described as follows:<br>
![](./Images/Occupation.PNG)<br>
Occupation will only contain one of the following values: Doctor, Professor, Singer or Actor.<br>
Sample Input<br>
![](./Images/Occupation_Input1.PNG)<br>
Sample Output
```
Jenny    Ashley     Meera  Jane
Samantha Christeen  Priya  Julia
NULL     Ketty      NULL   Maria
```

**Explanation**<br>
The first column is an alphabetically ordered list of Doctor names.
The second column is an alphabetically ordered list of Professor names.
The third column is an alphabetically ordered list of Singer names.
The fourth column is an alphabetically ordered list of Actor names.
The empty cell data for columns with less than the maximum number of names per occupation (in this case, the Professor and Actor columns) are filled with NULL values.

## Solution :
``` SQL
WITH Occupation_CTE AS
(
SELECT *,
ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name ) AS Row_num
FROM OCCUPATIONS
)

SELECT MAX(CASE WHEN Occupation='Doctor' THEN Name  END) AS Doctor,
             MAX(CASE WHEN Occupation='Professor' THEN Name END) AS Professor,
            MAX( CASE WHEN Occupation='Singer' THEN Name END) AS Singer,
             MAX(CASE WHEN Occupation='Actor' THEN Name END) AS Actor
FROM Occupation_CTE
group by Row_num
```
