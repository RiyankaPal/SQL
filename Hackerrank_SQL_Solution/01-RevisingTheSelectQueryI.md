# Revising the Select Query I

## Problem Statement:
Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA.<br>
The CITY table is described as follows:
![](./Images/City.png)

## Solution:

```SQL
Select * 
FROM CITY
WHERE COUNTRYCODE='USA'
And POPULATION >100000
```










