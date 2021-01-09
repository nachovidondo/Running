import os
<<<<<<< HEAD
import sqlite3
APP_PATH=os.getcwd()
DB_PATH = APP_PATH + "\src\my_database.db"

class DBConnection():
    def __init__(self):
        self.con = sqlite3.connect(DB_PATH)
        self.cursor = self.con.cursor()
        print("test", DB_PATH)
        
    def insertData(self, savedTime, runningTime):
        print ('debug insert', self.con, self.cursor)
        self.cursor.execute("""INSERT INTO TIEMPO_CORRIDO VALUES(?,?, ?)""", (None,savedTime, runningTime))
        self.con.commit()
        self.con.close()
            
    
       
=======
   
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
>>>>>>> 1bf140505b823671435c74998ecef68e60ad6ef2
