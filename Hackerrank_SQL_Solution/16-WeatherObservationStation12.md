# Weather Observation Station 12

## Problem Statement:
Query the list of CITY names from STATION that do not end with vowels and do not end with vowels. Your result cannot contain duplicates.

Input Format

The STATION table is described as follows:<br>
![](./Images/STATION.PNG)

<br>where LAT_N is the northern latitude and LONG_W is the western longitude.

## Solution:
```SQL
SELECT DISTINCT CITY
FROM STATION
WHERE SUBSTRING(CITY,len(CITY),1) NOT IN ('a','e','i','o','u') AND SUBSTRING(CITY,1,1) NOT IN ('a','e','i','o','u')

