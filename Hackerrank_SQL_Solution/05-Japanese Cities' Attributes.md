# Japanese Cities' Attributes

## Problem Statement:
Query all attributes of every Japanese city in the CITY table. The COUNTRYCODE for Japan is JPN.

The CITY table is described as follows:
![](./Images/City.png)

## Solution:
``` SQL
SELECT *
FROM CITY
WHERE COUNTRYCODE='JPN'
```