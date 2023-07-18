-- displays the top 3 cities temperature in July and August
SELECT city, AVG(value) FROM temperatures WHERE month IN (7,8) GROUP BY city ORDER BY 2 DESC LIMIT 3;
