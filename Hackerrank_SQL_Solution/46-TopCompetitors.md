# TOP Competitors:

# Solution :

``` SQL
    SELECT s.hacker_id,name
    FROM Submissions S
    JOIN Difficulty D
ON S.score=D.score
JOIN Challenges C
ON C.challenge_id=S.challenge_id AND C.difficulty_level=D.difficulty_level
JOIN Hackers H
ON H.hacker_id=S.hacker_id
GROUP BY S.hacker_id, name
having count(name)>1
ORDER BY COUNT(S.hacker_id) DESC,S.hacker_id ASC







