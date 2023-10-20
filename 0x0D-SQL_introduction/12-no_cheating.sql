-- this is a script that alters the score of Bob without using his ID
UPDATE second_table
SET score = 10
WHERE name = 'Bob';
