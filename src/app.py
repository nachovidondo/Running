from tkinter import*
import datetime
import time
import locale
from datetime import datetime
from tkinter import messagebox
from consulta import *
from tkinter import*
from datetime import datetime
from tkinter.ttk import Treeview
from consulta import *
import sqlite3
<<<<<<< HEAD
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import tkinter.ttk as ttk
=======
from consulta import DBConnection

>>>>>>> 1bf140505b823671435c74998ecef68e60ad6ef2
COLOR_WHITE = "#FAFAFA"
COLOR_BLACK = "#000"
FONT_SMALL = ("lato", 10)

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

dateTimeNow = datetime.now()
currentDate = dateTimeNow.strftime("%A %d, %B %Y")
currentTime = dateTimeNow.strftime("%I:%M %p")
<<<<<<< HEAD

=======
>>>>>>> 1bf140505b823671435c74998ecef68e60ad6ef2
dbConnection = None

def delete():
    text1.delete(0, "end")
    
def persist(savedTime, runningTime):
    dbConnection = DBConnection()
<<<<<<< HEAD
    print("Conexion : ", dbConnection.con)
    dbConnection.insertData(savedTime, runningTime)
    
=======
    print("Conexion: ", dbConnection.con)
    dbConnection.insertData(savedTime, runningTime)
>>>>>>> 1bf140505b823671435c74998ecef68e60ad6ef2
    
def enviarDatos():
    textoprint = text1.get()
    
    if int(textoprint) > 180:
        messagebox.showinfo("Error", "El numero es muy alto")
    elif int (textoprint) <= 0:
        messagebox.showinfo("Error", "Inserte un numero valido")
    else:
        secs = int(textoprint) * 60
        runningTime = time.strftime("%H:%M:%S", time.gmtime(int(secs)))
        message = "Corriste: " + str(runningTime) + "hs."
        messagebox.showinfo("Resultados", message)
<<<<<<< HEAD
        savedTime= currentTime + " " + currentDate
        persist(savedTime, runningTime)

def showInfo():
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM TIEMPO_CORRIDO")
        data = (row for row in cursor.fetchall())

        ventana = tk.Tk()
        table = Table(ventana, headings=('codigo_running','save_time','running_time'), rows=data)
        table.pack(expand=tk.YES, fill=tk.BOTH)

=======
        savedTime = currentTime + " " + currentDate
        persist(str(savedTime), str(runningTime))
>>>>>>> 1bf140505b823671435c74998ecef68e60ad6ef2

ventana = Tk()
ventana.title("Programa de Running")
ventana.config(bg = COLOR_WHITE)
ventana.iconbitmap("runner.ico")
ventana.geometry("600x400")
ventana.resizable(width=False, height=False)

<<<<<<< HEAD
image=PhotoImage(file="run.png")
label_imagen=Label(ventana,image=image)
label_imagen.pack()
=======
# imagen=PhotoImage(file="imagen1.png")
# label_imagen=Label(ventana,image=imagen)
# label_imagen.pack()
>>>>>>> 1bf140505b823671435c74998ecef68e60ad6ef2

label_1 = Label(ventana, text = "¿Cuantos minutos corriste hoy?")
label_1.place(x = 20,y = 170)
label_1.config(fon = FONT_SMALL)
label_1.config(bg = COLOR_WHITE, fg = COLOR_BLACK)

label_2 = Label(ventana, text = str(currentDate) + " \n" + str(currentTime), anchor="e", justify=LEFT)
label_2.place(x = 20,y = 300)
label_2.config(fon = ("lato", 20))
label_2.config(bg = COLOR_WHITE, fg = COLOR_BLACK)

text1 = Entry(ventana)
text1.pack()
text1.place(x = 20, y = 200)

#Botones
botonBorrar = Button(ventana, text = "Borrar", command= delete , fon = FONT_SMALL).place(x = 20, y = 250)
botonGuardar = Button(ventana, text = "Guardar", fon = FONT_SMALL, command = enviarDatos).place(x = 150, y = 250)


menuMostrar=Menu(ventana)
ventana.config(menu=menuMostrar)
Mostrarmenu=Menu(menuMostrar,tearoff=0)
menuMostrar.add_cascade(label="Menu",menu = Mostrarmenu)

Mostrarmenu.add_command(label="Mostrar Datos",command=showInfo)
Mostrarmenu.add_separator

class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)
  
        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"] = headings
        table["displaycolumns"] = headings
  
        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)
  
        for row in rows:
            table.insert('', tk.END, values=tuple(row))
  
        scrolltable = tk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)

ventana.mainloop()

