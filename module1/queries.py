"""
Part 1 Query Assignment
"""

TOTAL_CHARACTERS = 'SELECT COUNT(DISTINCT(name)) FROM charactercreator_character;'

TOTAL_SUBCLASS = 'SELECT * FROM charactercreator_necromancer;'

TOTAL_ITEMS = 'SELECT COUNT(DISTINCT(name)) FROM armory_item;'

WEAPONS = 'SELECT COUNT(*) FROM armory_weapon;'

NON_WEAPONS = """SELECT COUNT(*)
                FROM armory_item as ai
                LEFT OUTER JOIN armory_weapon as aw
                ON ai.item_id = aw.item_ptr_id"""

CHARACTER_ITEMS = """SELECT character_id, COUNT(item_id) AS num_items
                    FROM charactercreator_character_inventory
                    GROUP BY character_id
                    LIMIT 20;
                    """

CHARACTER_WEAPONS = """SELECT name, COUNT(*) as num_weapons
                    FROM
                        (SELECT * 
                        FROM armory_item AS ai
                        INNER JOIN armory_weapon as aw
                        ON ai.item_id = aw.item_ptr_id)
                    GROUP BY name
                    ORDER BY num_weapons DESC
                    LIMIT 20;"""

AVG_CHARACTER_ITEMS = """
                    SELECT AVG(total_items)
                    FROM
                        (SELECT name, COUNT(item_id) as total_items
                        FROM charactercreator_character as cc_char
                        INNER JOIN charactercreator_character_inventory as  cc_ci
                        WHERE cc_char.character_id = cc_ci.character_id
                        GROUP BY name);
                    """

AVG_CHARACTER_WEAPONS = """SELECT AVG(num_weapons)
                        FROM
                            (SELECT name, COUNT(*) as num_weapons
                            FROM
                                (SELECT * 
                                FROM armory_item AS ai
                                INNER JOIN armory_weapon as aw
                                ON ai.item_id = aw.item_ptr_id)
                            GROUP BY name);
                        """
