# Weather Observation Station 16
## Problem Statement :
Query the smallest Northern Latitudes (LAT_N) from STATION that is greater than 38.7780. Truncate your answer to 4 decimal places.<br>
Input Format<br>

The STATION table is described as follows:<br><br>
![](./Images/STATION.PNG)<br><br>
where LAT_N is the northern latitude and LONG_W is the western longitude.<br>

# Solution :
```SQL
SELECT CAST(MIN(LAT_N) AS DECIMAL(10,4))
FROM STATION
WHERE  LAT_N >38.7780