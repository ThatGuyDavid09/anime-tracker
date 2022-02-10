from AnilistPython import Anilist
from pprint import pprint
import pyperclip

import sqlite3
from sqlite3 import Error

from wrappers import *


def create_connection(database):
    conn = None
    try:
        conn = sqlite3.connect(database)
        return conn
    except Error as e:
        raise e

    raise Exception()


def execute_sql(sql):
    conn = create_connection("./database/anime.db")
    try:
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
        rows = c.fetchall()

        for r in rows:
            print(r)
    except Error as e:
        raise e


def setup_table():
    sql = """
        CREATE TABLE IF NOT EXISTS anime (
            id INTEGER PRIMARY KEY,
            anime_id INTEGER,
            stream_service VARCHAR
        );
    """
    execute_sql(sql)


anilist = Anilist()
setup_table()

anime_name = input("What anime would you like to see? ")
anime_info = anilist.extractID.anime(anime_name)["data"]["Page"]["media"]
# print(anime_info)
for i in range(len(anime_info)):
    anime = anime_info[i]
    # pprint(anime)
    title = anime["title"]["english"] if anime["title"]["english"] else anime["title"]["romaji"]
    print(f"{i + 1}. {title}")

choice = input("Which one of these is correct? ")
anime_id = anime_info[int(choice) - 1]["id"]
sql = f"""
INSERT INTO anime(anime_id) VALUES({anime_id});
"""
execute_sql(sql)

# pprint(anilist.extractInfo.anime(anime_id))

# pyperclip.copy(str(anime_info))
