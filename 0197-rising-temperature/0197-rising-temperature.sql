# Write your MySQL query statement below
SELECT
    A.id
FROM
    Weather AS A
JOIN
    Weather AS B
ON 
    DATEDIFF(A.recordDate,B.recordDate) = 1
WHERE 
    A.temperature > B.temperature
;