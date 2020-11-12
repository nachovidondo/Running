from tkinter import *
from tkinter import messagebox

from datetime import datetime
import time
import locale

COLOR_WHITE = "#FAFAFA"
COLOR_BLACK = "#000"
FONT_SMALL = ("lato", 10)

def delete():
    text1.delete(0,"end")
    
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
    
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

dateTimeNow = datetime.now()
currentDate = dateTimeNow.strftime("%A %d, %B %Y")
currentTime = dateTimeNow.strftime("%I:%M %p")

ventana = Tk()
ventana.title("Programa de Running")
ventana.config(bg = COLOR_WHITE)
ventana.geometry("500x300")
ventana.iconbitmap("runner.ico")

imagen=PhotoImage(file="imagen1.png")

label_imagen=Label(ventana,image=imagen)
label_imagen.pack()

label_1 = Label(ventana, text = "¿Cuantos minutos corriste hoy?")
label_1.place(x = 20,y = 170)
label_1.config(fon = FONT_SMALL)
label_1.config(bg = COLOR_WHITE, fg = COLOR_BLACK)

label_2 = Label(ventana, text = str(currentDate) + " \n" + str(currentTime), anchor="e", justify=LEFT)
label_2.place(x = 20,y = 50)
label_2.config(fon = ("lato", 20))
label_2.config(bg = COLOR_WHITE, fg = COLOR_BLACK)

text1 = Entry(ventana)
text1.pack()
text1.place(x = 20, y = 200)

#Botones
botonBorrar = Button(ventana, text = "Borrar", command= delete , fon = FONT_SMALL).place(x = 20, y = 250)
botonGuardar = Button(ventana, text = "Guardar", fon = FONT_SMALL, command = enviarDatos).place(x = 150, y = 250)



ventana.mainloop()

