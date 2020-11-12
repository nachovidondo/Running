import sqlite3
import os
   
APP_PATH = os.getcwd()
DB_PATH = APP_PATH+ '/my_database.db'
con = None 
cursor = None

#def connect():
#  con = sqlite3.connect(DB_PATH)
#  cursor = con.cursor()
#  return cursor

def insertData(saveTime, runningTime):
    con = sqlite3.connect(DB_PATH)
    cursor = con.cursor()
    saveTime = str(saveTime)
    cursor.execute( 
        """INSERT INTO TIEMPO_CORRIDO VALUES (?, ?)""", (saveTime, runningTime))
    con.commit()
    
       
#con.close()