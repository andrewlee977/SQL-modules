"""Pipeline example from sqlite to mongodb"""

import sqlite3
import pymongo

"""
MongoDB was easier to work with than PostgreSQL because you don't have to apply the same rigid
standards to data that get inserted into the database. 

MongoDB was harder in that the data you're inserting isn't structured and similar to one another,
so figuring out how to insert it into the database in a scalable way was more difficult from
what I saw (the for looping). Setting up the MongoDB seemed more counterintuitive than PostgreSQL,
and the commands for MongoDB seem unintuitive also, such as accessing data and printing them out.
"""

PASSWORD = "9nwZpqG8XimVtBKh"
DBNAME = "myFirstDatabase"


def connect_to_mongo(password, dbname):
    # Client that connects to a database
    client = pymongo.MongoClient(
    f"mongodb+srv://andrewlee977:{password}@cluster0.szokv.mongodb.net/{dbname}?retryWrites=true&w=majority"
)
    return client


def connect_to_sldb(dbname="../data/rpg_db.sqlite3"):
    conn = sqlite3.connect(dbname)
    curs = conn.cursor()
    return conn, curs


def handle_characters(curs, collection):
    """Handles character pipeline"""
    characters_list = curs.execute("SELECT * FROM charactercreator_character;")

    for character in characters_list:
        character_doc = {
            "name": character[1],
            "level": character[2],
            "exp": character[3],
            "hp": character[4],
            "strength": character[5],
            "intelligence": character[6],
            "dexterity": character[7],
            "wisdom": character[8],
            # "items": TODO: Assignment
            # "weapons": TODO: Assignment
        }
        collection.insert_one(character_doc)

def handle_inventory(curs, collection):
    inventory_list = curs.execute("SELECT * FROM charactercreator_character_inventory;")

    for item in inventory_list:
        inventory_doc = {
            "character_id": item[1],
            "item_id": item[2]
        }
        collection.insert_one(inventory_doc)

def handle_armory_item(curs, collection):
    armory_item_list = curs.execute("SELECT * FROM armory_item;")

    for item in armory_item_list:
        armory_doc = {
            "name": item[1],
            "value": item[2],
            "weight": item[3]
        }
        collection.insert_one(armory_doc)

def handle_armory_weapon(curs, collection):
    armory_weapon_list = curs.execute("SELECT * FROM armory_weapon;")

    for weapon in armory_weapon_list:
        weapon_doc = {
            "power": weapon[1]
        }
        collection.insert_one(weapon_doc)
        
if __name__ == "__main__":
    mongo_client = connect_to_mongo(PASSWORD, DBNAME)
    sl_conn, sl_curs = connect_to_sldb()
    collection = mongo_client.myFirstDatabase.myFirstDatabase
    collection.delete_many({})

    handle_characters(sl_curs, collection)
    handle_inventory(sl_curs, collection)
    handle_armory_item(sl_curs, collection)
    handle_armory_weapon(sl_curs, collection)

    print(list(collection.find()))
    sl_curs.close()