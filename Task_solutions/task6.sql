"""
TASK 6: Add a new column in the profiles table and fill it with random data.
"""

"""
Log into the database using the prod_dba account created in Task1 and execute the below
query on test database.
1. Lets add a new column for storing "email_id" on the profiles table.
2. We would need to ALTER the table to add a new column for storing email_id.
3. Once the ALTER TABLE query has been executed against the profiles tables,
   we can perform a DESCRIBE on the profiles table to confirm it has been updated.
4. As the profiles table has been updated, we can now insert values into the table.
"""


```sql
ALTER TABLE profiles
ADD email_id VARCHAR(255);
```

"""
Verify that the profiles table has been updated.
"""

```sql
DESCRIBE profiles;
```


"""
Lets insert some random values into the profiles table.
"""

```sql
INSERT INTO profiles (
id, contact_id, attribute_id,
value, crypted, email_id)
VALUES
(890303, 1, 2, "Cloud Native Developer",
0, "Hank_Moody@gmail.com");
```

"""
Validate that the new profile was inserted into the profiles table.
"""

```sql
SELECT * FROM profiles WHERE id = 890303;
```
