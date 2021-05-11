"""Part 2: Making and populating a database"""

import sqlite3
from queries import TOTAL_CHARACTERS

def connect_to_db(db_name='../data/rpg_db.sqlite3'):
    conn = sqlite3.connect(db_name)
    return conn

def execute_query(conn, query):
    curs = conn.cursor()
    results = curs.execute(query).fetchall()
    curs.close()
    return results

if __name__ == "__main__":
    conn = connect_to_db()
    characters = execute_query(conn, TOTAL_CHARACTERS)
    print(characters)