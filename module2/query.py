# PostGreSQL queries


<<<<<<< HEAD
# SQLite queries - for sql_pipeline_example.py
=======
# SQLite queries
>>>>>>> 87feb7f35388249260c813b9a7e82c4701ea92e4
EXTRACT_CHARACTERS = """
  SELECT *
  FROM charactercreator_character;
"""

CREATE_characterscreator_character = """
  CREATE TABLE IF NOT EXISTS charactercreator_character (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    level INT NOT NULL,
    exp INT NOT NULL,
    hp INT NOT NULL,
    strength INT NOT NULL,
    intelligence INT NOT NULL,
    dexterity INT NOT NULL,
    wisdom INT NOT NULL
  );
"""

INSERT_INTO_charactercreator_character = """
  INSERT INTO charactercreator_character (
    character_id,
    name,
    level,
    exp,
    hp,
    strength,
    intelligence,
    dexterity,
    wisdom
  ) VALUES (
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s
  );
"""


<<<<<<< HEAD
# For postgresql_example.py
=======
# For Postgresl_example.py
>>>>>>> 87feb7f35388249260c813b9a7e82c4701ea92e4
SQL_CREATE_TABLE = """
  CREATE TABLE IF NOT EXISTS test_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(40) NOT NULL,
    age INT
  );
"""

SQL_INSERT_DATA = """
  INSERT INTO test_table (
    name,
    age
  ) VALUES (
    'Carl',
    102
  );
"""

SQL_SHOW_TABLE = """
  SELECT * FROM test_table;
"""
