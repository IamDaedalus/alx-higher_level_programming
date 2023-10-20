-- this script creates a table called id_not_null on the server 
CREATE TABLE IF NOT EXISTS id_not_null (
	`id` INT NOT NULL DEFAULT 1,
	name VARCHAR(256)
);
