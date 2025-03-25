# Ollivender's Inventory:

# Solution :

``` SQL
SELECT id, age, coins_needed, power 
FROM (
    SELECT 
        W.id, 
        W.code, 
        W.coins_needed, 
        W.power,
        WP.age,
        RANK() OVER (PARTITION BY W.power, WP.age 
                     ORDER BY W.coins_needed ASC) AS rank_col
    FROM Wands W 
    JOIN Wands_Property WP ON W.code = WP.code  
    WHERE WP.is_evil = 0
) sub 
WHERE rank_col = 1
ORDER BY power DESC, age DESC;





