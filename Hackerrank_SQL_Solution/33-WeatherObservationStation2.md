# Weather Observation Station 2
## Problem Statement :
Query the following two values from the STATION table :

1. The sum of all values in LAT_N rounded to a scale of  decimal places.<br>
2. The sum of all values in LONG_W rounded to a scale of  decimal places.<br>
Input <br>

The STATION table is described as follows:<br><br>
![](./Images/STATION.PNG)<br><br>
where LAT_N is the northern latitude and LONG_W is the western longitude.

Output Format

Your results must be in the form:
```
lat lon

```
where lat is the sum of all values in LAT_N and lon is the sum of all values in LONG_W. Both results must be rounded to a scale of 2 decimal places.

## Solution :
``` SQL
SELECT CAST(SUM(LAT_N) AS DECIMAL(10,2)),CAST(SUM(LONG_W) AS DECIMAL(10,2))
FROM STATION
