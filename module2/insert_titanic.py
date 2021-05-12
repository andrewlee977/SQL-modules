"""Uploads Titanic csv data """

import pandas as pd
import psycopg2 as pg2


DBNAME = "wnphosbi"
USER = "wnphosbi"
PASSWORD = "NlMaJqzK0DRgjdU7aNdroiaEmXONFPOU"
HOST = "queenie.db.elephantsql.com"

# df = pd.read_csv('../data/titanic.csv')
# curs.copy_from(df, temp_unicommerce_status, sep=',')
# f.close()age INT NOT NULL,

def csv_to_db(conn):
    curs = conn.cursor()
    f = open('../data/titanic.csv', 'r')
    next(f)
    curs.copy_from(f, 'titanic', sep=',', columns=('Survived', 'Pclass', 'Name', 'Sex', 'Age',
                                                   '\"Siblings/Spouses Aboard\"', '\"Parents/Children Aboard\"', 'Fare'))
    f.close()
    curs.close()


def connect_to_db(dbname, user, password, host):
    conn = pg2.connect(dbname=dbname, user=user, password=password, host=host)
    # df.to_sql(name='titanic', con=conn, if_exists='replace')
    return conn

# df.to_sql(name='titanic', con=conn, if_exists='replace')


def execute_query(conn, query, read=True):
    curs = conn.cursor()
    curs.execute(query)
    if read:
        results = curs.fetchall()
        curs.close()
        return results
    else:
        conn.commit()
        curs.close()
        return "CUD Query Executed"
    

SQL_TITANIC_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS titanic (
        id SERIAL PRIMARY KEY,
        Survived INT,
        Pclass INT,
        Name VARCHAR(180),
        Sex VARCHAR(30),
        Age FLOAT(4),
        \"Siblings/Spouses Aboard\" INT,
        \"Parents/Children Aboard\" INT,
        Fare FLOAT(4)
    );
"""

SQL_TITANIC_SHOW_TABLE = """
    SELECT * FROM titanic
"""

def show_test_table(conn):
    curs = conn.cursor()
    curs.execute(SQL_TITANIC_SHOW_TABLE)
    return curs.fetchall()



if __name__ == "__main__":
    conn = connect_to_db(DBNAME, USER, PASSWORD, HOST)
    execute_query(conn=conn, query=SQL_TITANIC_CREATE_TABLE, read=False)
    csv_to_db(conn)
    results = show_test_table(conn)
    print(results)


