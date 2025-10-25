# Placements

# Solution :

```SQL
SELECT Name
FROM Students S
JOIN Packages P1
ON S.ID=P1.ID
JOIN Friends F 
ON S.ID=F.ID
JOIN Packages P2
ON F.Friend_ID=P2.ID
WHERE P2.Salary > P1.Salary
order by P2.salary;
```