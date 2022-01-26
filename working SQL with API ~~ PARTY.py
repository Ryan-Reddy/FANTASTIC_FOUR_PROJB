import sqlite3
import json
import requests


def create():
    try:
        curs.execute(
            """CREATE TABLE IF NOT EXISTS games(
        app_id INTEGER PRIMARY KEY, 
        name TEXT NOT NULL, 
        developer TEXT NOT NULL,
        publisher TEXT NOT NULL,
        positive INTEGER NOT NULL,
        negative INTEGER NOT NULL,
        userscore INTEGER NOT NULL
        )"""
        )
    except:
        pass


def insert():
    # TODO: make multiple inserts/databases: ---> https://steamspy.com/api.php

    url = "https://steamspy.com/api.php?request=all&page=0"
    data = requests.get(url).json()

    for game_id, game in data.items():  # <--- unpacks the dictionairy in dictionairy
        app_id = game.get("appid", "no_data")
        name = game.get(
            "name", "no_name_found"
        )  # <--- 'no_name_found' option as backup for .get
        developer = game.get("developer", "no_data")
        publisher = game.get("publisher", "no_data")
        positive = game.get("positive", "no_data")
        negative = game.get("negative", "no_data")
        userscore = game.get("userscore", "no_data")

        arguments = (
            app_id,
            name,
            developer,
            publisher,
            positive,
            negative,
            userscore,
        )
        try:
            curs.execute(
                """INSERT INTO games(
            app_id, 
            name, 
            developer, 
            publisher, 
            positive, 
            negative, 
            userscore) VALUES(?, ?, ?, ?, ?, ?, ?)""",
                arguments,
            )
        except:
            pass

def select(verbose=True):
    sql = "SELECT * FROM games"
    recs = curs.execute(sql)
    if verbose:
        for row in recs:
            print(row)


conn = None
conn = sqlite3.connect("steam_database.db")
curs = conn.cursor()
create()
insert()
conn.commit()  # <--- commit needed
select()
curs.close()
if conn is not None:
    conn.close()
