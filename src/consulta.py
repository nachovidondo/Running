import sqlite3
import os
   
APP_PATH = os.getcwd()
DB_PATH = APP_PATH + '/my_database.db'

class DBConnection:
    def __init__(self):
        self.con = sqlite3.connect(DB_PATH)
        self.cursor = self.con.cursor()

    def insertData(self, saveTime, runningTime):
        print('debug insert', self.con, self.cursor)
        self.cursor.execute("""INSERT INTO TIEMPO_CORRIDO VALUES (?, ?)""", (saveTime, runningTime))
        self.con.commit()
        self.con.close()