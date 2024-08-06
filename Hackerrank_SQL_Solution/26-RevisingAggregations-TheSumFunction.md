#  Revising Aggregations-The Sum Function

## Problem Statement:
Query the total population of all cities in CITY where District is California.<br>

Input Format<br><br>
The CITY table is described as follows:<br><br>
![](./Images/City.PNG)<br>

## Solution:
``` SQL
Select SUM(POPULATION)
FROM CITY
WHERE DISTRICT='California'