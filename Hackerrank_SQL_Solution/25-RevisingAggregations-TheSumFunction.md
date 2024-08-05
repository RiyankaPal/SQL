#  Revising Aggregations-The Sum Function

## Problem Statement:
Query the total population of all cities in CITY where District is California.
Input Format
The CITY table is described as follows:
![](./Images/City.PNG)<br>

## Solution:
``` SQL
Select SUM(POPULATION)
FROM CITY
WHERE DISTRICT='California'