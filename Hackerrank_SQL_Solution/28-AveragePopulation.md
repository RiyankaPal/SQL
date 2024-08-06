#  Average Population

## Problem Statement:
Query the average population for all cities in CITY, rounded down to the nearest integer.

Input Format

The CITY table is described as follows:<br><br>
![](./Images/City.PNG)<br><br>
## Solution:
``` SQL
SELECT FLOOR(AVG(POPULATION))
FROM CITY