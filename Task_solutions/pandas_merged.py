import pandas as pd
import yaml
import sys
import mysql.connector as mariadb


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

#Initiate the Connection to the Database using the config file.
conn = mariadb.connect(
        user = cfg['mysql']['user'],
        password = cfg['mysql']['password'],
        database = cfg['mysql']['database'],
        host = cfg['mysql']['host'],
        port = cfg['mysql']['port'])


def getdata(table):
    """
    The function takes table as a Argument and executes a select statement
    against that table in the user database.

    Args:
        table: The table on which we want to execute a query.

    Returns:
        The entire table is returned as output for further processing.

    """
    try:
        #Create the SELECT statement to select all data from the table passed as Argument.

        query = "SELECT * FROM {};".format(table)

        #We could load the result of the query into the Pandas Dataframe using read_sql method.

        df = pd.read_sql(query, conn)

        #We now return the dataframe to process further.
        return df

    except mariadb.Error as e:
        print(f"Error connecting to Mariadb platform : {e}")
        sys.exit(1)


if __name__== '__main__':

    # Lets load the clients table into the dataframe.
    clients = getdata("clients")

    profiles = getdata("profiles")

    #We can now merge both the clients and profiles dataframes into one dataframe.
    combined_table = pd.concat([clients, profiles], ignore_index=True)

    print(combined_table)

    #Make sure to close out the database connection.    
    conn.close()
