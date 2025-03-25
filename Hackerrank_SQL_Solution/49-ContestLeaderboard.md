# ContestLeaderboard

# Solution :

``` SQL
    WITH MaxScores AS (
    -- Step 1: Get the max score per hacker per challenge
    SELECT S.hacker_id, H.name, S.challenge_id, MAX(S.score) AS max_score
    FROM Submissions S
    JOIN Hackers H ON S.hacker_id = H.hacker_id
    GROUP BY S.hacker_id, H.name, S.challenge_id
)
-- Step 2: Sum the max scores across all challenges per hacker
SELECT hacker_id, name, SUM(max_score) AS total_score
FROM MaxScores
GROUP BY hacker_id, name
HAVING SUM(max_score) > 0  -- Exclude hackers with a total score of 0
ORDER BY total_score DESC, hacker_id ASC;  -- Sort by highest score, then hacker_id
