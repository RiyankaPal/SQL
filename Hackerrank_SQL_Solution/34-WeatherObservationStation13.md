# Weather Observation Station 13
## Problem Statement :
Query the sum of Northern Latitudes (LAT_N) from STATION having values greater than 38.7880 and less than 137.2345. Truncate your answer to  decimal places.<br>
Input Format<br>

The STATION table is described as follows:<br><br>
![](./Images/STATION.PNG)<br><br>
where LAT_N is the northern latitude and LONG_W is the western longitude.<br>

# Solution :
```SQL
SELECT CAST(SUM(LAT_N) AS DECIMAL(10,4))
FROM STATION
WHERE LAT_N>38.7880 AND LAT_N <137.2345