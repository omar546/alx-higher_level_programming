--  lists the number of records with eq score from the table
SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY score DESC;