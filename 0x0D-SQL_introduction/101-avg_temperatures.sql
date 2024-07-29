-- A script that displays the average temperature by city ordered by temperature
USE hbtn_0c_0;
SELECT city, AVG(`value`) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
