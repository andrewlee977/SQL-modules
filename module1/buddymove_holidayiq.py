"""Part 2: Making and populating a database"""

import pandas as pd
import sqlite3

"""Read in the data"""
df = pd.read_csv('../data/buddymove_holidayiq.csv')

def connect_to_db(db_name='../data/buddymove_holidayiq.sqlite3'):
    """Connect/Create the database"""
    conn = sqlite3.connect(db_name)
    df.to_sql(name='review', con=conn, if_exists='replace')
    return conn

def execute_query(conn, query):
    """Create cursor & execute query"""
    curs = conn.cursor()
    results = curs.execute(query).fetchall()
    curs.close()
    return results

"""SQL statements to grab data from database"""
rows = """SELECT COUNT(*)
        FROM review;"""

user_reviews = """SELECT COUNT(*)
               FROM review WHERE Nature > 100 AND Shopping > 100;"""

avg_reviews = """SELECT AVG(Sports), AVG(Religious), AVG(Nature),
              AVG(Theatre), AVG(Shopping), AVG(Picnic) FROM review;"""

if __name__ == "__main__":
    """Run functions on file call"""
    conn = connect_to_db()
    total_rows = execute_query(conn, rows)
    u_reviews = execute_query(conn, user_reviews)
    avg_rev = execute_query(conn, avg_reviews)
    print('Total Rows Query')
    print(total_rows, '\n')
    print('User Reviews Query')
    print(u_reviews, '\n')
    print('Average Reviews Query')
    print(avg_rev, '\n')

# print(df.shape)
# print(df.isnull().sum().sum())
