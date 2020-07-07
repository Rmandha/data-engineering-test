"""
TASK 5: Insert a new client and a new profile (use sql).

Solution: As the task asks for the queries to be written
in sql. We can use insert into queries in the test database.
We are using the "prod_admin" user created in Task-1 to
login into the database and execute the below queries.
"""


# Let's add a new client with id "0850" into the clients table.

```sql
INSERT INTO clients (
id, description, adminuser_id,
guid, price_tear, create_user_id,
update_user_id, update_time, create_time,
idmasteraccount, geofence, phone,
display_id, idstatus, idaccounttype,
idprofile, timezone)
VALUES
(0850, "Anthem Health Care", 2, 3,
NULL, NULL, 200, "2020-07-06 10:26:30",
"2020-07-05 10:10:10", 1000, NULL, "5138867086",
NULL, "active", 1, 1, "America/Toronto");
```

"""
We can insert a new profile into the profiles using the below query.
Please note that the idprofile column on clients table and
contact_id column on profiles table should have same value as its
respresents the foreign key relationship between the two tables.
"""

INSERT INTO profiles (id, contact_id, attribute_id, value, crypted)
VALUES
(9988, 1, 2, "Data Engineer", 0);

# We can validate if our entries have been added to the tables.

SELECT * FROM clients WHERE id = 0805;

SELECT * FROM profiles WHERE id = 9988;

