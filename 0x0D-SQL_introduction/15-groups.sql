-- A script that lists the numcer of records with the same score in the table 'second_table'
SELECT score, COUNT(score) AS number FROM second_table
GROUP BY score;
