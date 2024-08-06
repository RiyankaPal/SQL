# Population Density Difference

## Problem Statement:
Query the difference between the maximum and minimum populations in CITY.

Input Format

The CITY table is described as follows:<br>
![](./Images/City.PNG)<br><br>

## Solution:
```SQL
SELECT MAX(POPULATION)-MIN(POPULATION) AS Diff
FROM CITY