# Weather Observation Station 4

## Problem Statement:

Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.<br>
The STATION table is described as follows:<br>
![](./Images/STATION.PNG)
<br>where LAT_N is the northern latitude and LONG_W is the western longitude.
For example, if there are three records in the table with CITY values 'New York', 'New York', 'Bengalaru', there are 2 different city names: 'New York' and 'Bengalaru'. The query returns 1, because.<br>
**total number of records - number of unique city name= 3-2=1**

## Solution:
```SQL
SELECT COUNT(CITY) - COUNT(DISTINCT CITY) AS DIFF
FROM STATION
```