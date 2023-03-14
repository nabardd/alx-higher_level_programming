-- script that displays the top 3 cities temperature during
-- july and august ordered by tempeature (descending)
SELECT `city`, AVG(`value`) as `avg_temp`
FROM `temperatures`
WHERE month IN (7, 8)
GROUP BY `city`
ORDER BY 2 DESC
LIMIT 3;