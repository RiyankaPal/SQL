# Print Prime Numbers

# Solution :

``` SQL
    WITH Numbers AS (
    SELECT 2 AS num
    UNION ALL
    SELECT num + 1 FROM Numbers WHERE num < 1000
)
SELECT STRING_AGG(num, '&') AS Prime_Numbers
FROM Numbers 
WHERE num NOT IN (
    SELECT a.num
    FROM Numbers a, Numbers b
    WHERE a.num % b.num = 0 
    AND a.num > b.num 
    AND b.num > 1
)
OPTION (MAXRECURSION 1000);

