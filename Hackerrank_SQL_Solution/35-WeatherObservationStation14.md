# Weather Observation Station 14
## Problem Statement :
Query the greatest value of the Northern Latitudes (LAT_N) from STATION that is less than 137.2345. Truncate your answer to 4 decimal places.<br>
Input Format<br>

The STATION table is described as follows:<br><br>
![](./Images/STATION.PNG)<br><br>
where LAT_N is the northern latitude and LONG_W is the western longitude.<br>

# Solution :
```SQL
SELECT CAST(MAX(LAT_N) AS DECIMAL(10,4))
FROM STATION
WHERE  LAT_N <137.2345