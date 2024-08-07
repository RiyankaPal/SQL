# Weather Observation Station 18
## Problem Statement :
Consider P1(a,b) and P2(c,d)  to be two points on a 2D plane.<br>
- a happens to equal the minimum value in Northern Latitude (LAT_N in STATION).<br>
- b happens to equal the minimum value in Western Longitude (LONG_W in STATION).<br>
- c happens to equal the maximum value in Northern Latitude (LAT_N in STATION).<br>
- d happens to equal the maximum value in Western Longitude (LONG_W in STATION).<br>
Query the Manhattan Distance between points P1 and P2 and round it to a scale of 4 decimal places.<br>
The STATION table is described as follows:<br><br>
![](./Images/STATION.PNG)<br><br>
where LAT_N is the northern latitude and LONG_W is the western longitude.<br>

# Solution :
```SQL
SELECT CAST(
ABS(MAX(LAT_N) - MIN(LAT_N)) + ABS(MAX(LONG_W) - MIN(LONG_W)) 
AS DECIMAL(20, 4)) 
FROM STATION
