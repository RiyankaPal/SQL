# WEATHER OBSERVATION Station 20:

# Solution :

``` SQL
    WITH Ordered AS (
    SELECT LAT_N, 
           ROW_NUMBER() OVER (ORDER BY LAT_N) AS row_num, 
           COUNT(*) OVER () AS total_rows
    FROM STATION
)
SELECT CAST(ROUND(AVG(LAT_N), 4) AS DECIMAL(10,4)) AS MEDIAN
FROM Ordered
WHERE row_num IN (
    FLOOR((total_rows + 1) / 2), 
    CEILING((total_rows + 1) / 2)
);







