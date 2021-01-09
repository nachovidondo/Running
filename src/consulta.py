import os
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
            
    
       
