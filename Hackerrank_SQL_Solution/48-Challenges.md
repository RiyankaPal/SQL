# Challenges:

# Solution :

``` SQL
    WITH ChallengeCounts AS (
    SELECT H.hacker_id, H.name, COUNT(C.challenge_id) AS Challenges_created
    FROM Hackers H
    JOIN Challenges C ON H.hacker_id = C.hacker_id
    GROUP BY H.hacker_id, H.name
)
SELECT hacker_id, name, Challenges_created
FROM ChallengeCounts
WHERE Challenges_created = (SELECT MAX(Challenges_created) FROM ChallengeCounts)  -- Get max challenges
   OR Challenges_created NOT IN (  
        SELECT Challenges_created 
        FROM ChallengeCounts 
        GROUP BY Challenges_created 
        HAVING COUNT(*) > 1  -- Exclude duplicate counts unless they are the max
    )
ORDER BY Challenges_created DESC, hacker_id;








