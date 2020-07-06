"""
TASK 2: Write a sql query that gets all data from both table in one result set.
"""

"""
Log into the database using the prod_dba account created in Task1 and execute the below
query on test database.
1. Lets perform a join on both the tables using the idprofile and contact_id columns.
2. The output can either be printed out or store into a csv file on the container under /var/lib/mysql folder.
3. We can verify the ouput of the files by executing "head merged_tables.csv" command.
"""

SELECT * FROM clients c JOIN profiles p
ON c.idprofile = p.contact_id
INTO OUTPUT FILE '/var/lib/mysql/merged_tables.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
