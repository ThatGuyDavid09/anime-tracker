from AnilistPython import Anilist
from pprint import pprint

import sqlite3
from sqlite3 import Error

from wrappers import *


def create_connection(database):
    conn = None
    try:
        conn = sqlite3.connect(database)
        return conn
    except Error as e:
        print(e)

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
        print(e)

if __name__ == "__main__":
    print("ok")
    sql = """
    SELECT * FROM test
    """
    execute_sql(sql)