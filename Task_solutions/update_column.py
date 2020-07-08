"""
TASK 4: On your copy of the profiles table, update the value column to 'fifth_row' (please don't write queries manually).
"""


import pandas as pd
import yaml
import sys
import pymysql


"""
Its a best practice not to give the user_id and password of the account
that will be used to access the prod database. As such, we could use a
configuration file which will contain the environment variables that will
be utilized to pass the following details for creating a connection to the
database: user, password, database, host and port
"""

# We can read the "db_config.yaml" file which has our environ variables.
file = open('db_config.yaml', 'r')

# We can now load the contents of the yaml config file.
cfg = yaml.load(file, Loader=yaml.FullLoader)


# Initiate the Connection to the Database using the config file.
mydb = create_engine('mysql+pymysql://' + cfg['mysql']['user']
        + ':' + cfg['mysql']['password'] + '@' + cfg['mysql']['host']
        + ':' + str(cfg['mysql']['port']) + '/' + cfg['mysql']['database'],
        echo=False)

try:
    # Create the SELECT statement to select all data from the profiles table.
    query = "SELECT * FROM profiles;"

    # We could load the result of the query into the Pandas Dataframe using read_sql method.
    profiles_df = pd.read_sql(query, con = mydb)

    # Lets use the 'rename' function of pandas to rename the specific column for the pandas dataframe.
    profiles_df.rename(columns={'value':'fifth_row'}, inplace = True)

    # We would convert the dataframe into sql table through "to_sql" method and replace the whole profiles table.
    profiles_df.to_sql(name = 'profiles', con = mydb, if_exists = 'replace', index = False)

except mariadb.Error as e:
    print(f"Error connecting to Mariadb platform : {e}")
    sys.exit(1)
