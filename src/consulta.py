import sqlite3
import os

APP_PATH = os.getcwd()
DB_PATH = APP_PATH+ '/my_database.db'

con = sqlite3.connect (DB_PATH)
cursor = con.cursor()
cursor.execute( """
    CREATE TABLE TIEMPO_CORRIDO(
        timestamp TEXT PRIMARE KEY NOT NULL,
        running_time TEXT
    )"""
    )

con.close()