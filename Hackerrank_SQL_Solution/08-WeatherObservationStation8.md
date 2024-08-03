# Weather Observation Station 8

## Problem Statement:
Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.

Input Format

The STATION table is described as follows:
![](./Images/STATION.PNG)

## Solution

```SQL
SELECT CITY
FROM STATION
WHERE SUBSTRING(CITY,len(CITY),1) in ('a','e','i','o','u') AND SUBSTRING(CITY,1,1) in ('a','e','i','o','u')
```