-- A script that displays the top 3 cities of temperature during July and August
USE hbtn_0c_0;
SELECT city, AVG(`value`) AS avg_temp
FROM temperatures
WHERE month = 'July' OR month = 'August'
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
