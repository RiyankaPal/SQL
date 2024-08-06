#  Revising Aggregations-The Count Function

## Problem Statement:
Query a count of the number of cities in CITY having a Population larger than 100,000.<br>

Input Format<br>

The CITY table is described as follows:<br><br>
![](./Images/City.PNG)<br>

## Solution:
``` SQL
SELECT COUNT(DISTRICT)
FROM CITY
WHERE POPULATION >100000