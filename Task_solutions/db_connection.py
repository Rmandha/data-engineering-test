import pandas
import mysql.connector as mariadb
import sys
import yaml

class Database_Connectioni:

    def __init__(self, username, password):

        # We can read the "db_config.yaml" file which has our environ variables.
        file = open('db_config.yaml', 'r')

        # We can now load the contents of the yaml config file.
        cfg = yaml.load(file, Loader=yaml.FullLoader)

        self.username = username
        self.password = password
        self.conn = mariadb.connect(
                user = cfg['mysql']['user'],
                password = cfg['mysql']['password'],
                database = cfg['mysql']['database'],
                host = cfg['mysql']['host'],
                port = cfg['mysql']['port'])

        cur = conn.cursor(buffered=True)

    def create_user(username,password):

        try:

            cur.execute("CREATE USER '{}'@'%' IDENTIFIED BY '{}';".format(username, password))

            #print(cur.execute("SELECT USER FROM mysql.user;")

            cur.execute("GRANT ALL PRIVILEGES ON test.* TO '{}';".format(username))

            cur.execute("FLUSH PRIVILEGES;")

        except mariadb.Error as e:
            print(f"Error connecting to Mariadb platform : {e}")
            sys.exit(1)

        conn.close()


        def user_connection(username, password):

        self.create_user(username, password)

        conn = mariadb.connect(
                host = '127.0.0.1',
                user = username,
                password = password,
                database = 'test',
                port = 3306)

        cur = conn.cursor(buffered=True)

        query = "SELECT * FROM profiles LIMIT 5;"

        print(pd.read_sql(query, conn))

        return conn

