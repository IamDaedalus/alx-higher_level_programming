-- this script creates a table called unique_id on the server 
CREATE TABLE IF NOT EXISTS unique_id (
	`id` INT UNIQUE DEFAULT 1,
	name VARCHAR(256)
);
