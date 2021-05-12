"""SQLite to PostGreSQL pipeline"""
import sqlite3
import psycopg2 as pg2
from query import EXTRACT_CHARACTERS, CREATE_characterscreator_character, INSERT_INTO_charactercreator_character


<<<<<<< HEAD
DBNAME = "wnphosbi"
USER = "wnphosbi"
PASSWORD = "NlMaJqzK0DRgjdU7aNdroiaEmXONFPOU"
HOST = "queenie.db.elephantsql.com"
=======
DBNAME = "?"
USER = "?"
PASSWORD = "?"
HOST = "?"

>>>>>>> 87feb7f35388249260c813b9a7e82c4701ea92e4

# We want to move charactercreator_character from sqlite -> postgresql
def create_connections(dbname, user, password, host, sqlite_db="../data/rpg_db.sqlite3"):
    """Creates a connection to sqlite and postgresql"""
    sl_conn = sqlite3.connect(sqlite_db)
    pg_conn = pg2.connect(dbname=dbname, user=user,
                          password=password, host=host)
    return sl_conn, pg_conn


def execute_query(conn, query, read=True):
    """Executes queries depending on conn object passed in"""
    curs = conn.cursor()
    curs.execute(query)
    if read:
        # Will fetch data if we are reading so we dont get error
        results = curs.fetchall()
        curs.close()
        return results
    else:
        # Will commit our changes if we are Creating, Updating, Deleting
        conn.commit()
        curs.close()
        return "CUD Query Executed"


if __name__ == "__main__":
    sl_conn, pg_conn = create_connections(DBNAME, USER, PASSWORD, HOST)
    character_list = execute_query(sl_conn, EXTRACT_CHARACTERS)
    # character_list = [(1, 'Aliquid iste optio reiciendi', 0, 0, 10, 1, 1, 1, 1), (...), (...), ...]
    execute_query(
        conn=pg_conn, query=CREATE_characterscreator_character, read=False)

    pg_curs = pg_conn.cursor()
    for character in character_list:
        pg_curs.execute(INSERT_INTO_charactercreator_character, character)
        pg_conn.commit()
        pg_curs.close()
