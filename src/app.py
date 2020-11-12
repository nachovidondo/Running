from tkinter import *
from tkinter import messagebox

from datetime import datetime
import time
import locale

COLOR_WHITE = "#FAFAFA"
COLOR_BLACK = "#000"
FONT_SMALL = ("lato", 10)

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

def delete():
    text1.delete(0,"end")

# Podes quitar el comentario para ver la imagen si te interesa.
# imagenL = PhotoImage(file="imagen1.png")
# labelimagen = Label(ventana,image=imagenL).place(x=0,y=0)
    
def Enviardatos():
    textoprint = text1.get()
    
    if int(textoprint) > 180:
        messagebox.showinfo("Error", "El numero es muy alto")
    elif int (textoprint) <= 0:
        messagebox.showinfo("Error", "Inserte un numero valido")
    else:
        secs = int(textoprint) * 60
        runningTime = time.strftime("%H:%M:%S", time.gmtime(int(secs)))
        message = "Corriste: " + str(minutes) + "hs."
        messagebox.showinfo("Resultados", minutes)
    
    #ventana.destroy()

label1 = Label(ventana, text = "¿Cuantos minutos corriste hoy?")
label1.place(x = 20,y = 170)
label1.config(fon = FONT_SMALL)
label1.config(bg = COLOR_WHITE, fg = COLOR_BLACK)

label2 = Label(ventana, text = str(currentDate) + " \n" + str(currentTime), anchor="e", justify=LEFT)
label2.place(x = 20,y = 50)
label2.config(fon = ("lato", 20))
label2.config(bg = COLOR_WHITE, fg = COLOR_BLACK)

v=IntVar()
text1 = Entry(ventana,textvariable=v)
text1.pack()
text1.place(x = 20, y = 200)

#botones
boton_borrar = Button(ventana, text = "Borrar", command= delete , fon = FONT_SMALL).place(x = 20, y = 250)
boton_guardar = Button(ventana, text = "Guardar", fon = FONT_SMALL, command = Enviardatos).place(x = 150, y = 250)

def fecha_hora():
    now = datetime.now()
    messagebox.showinfo("Fecha y Hora", now)

#En vez de usar el boton pensaba en mostrar la hora todo el tiempo. 
#En ningun programa he visto que tengas que usar un boton para ver la hora
#botonfecha_hora = Button(ventana,text = "Fecha y hora ", command = fecha_hora).place (x = 20, y = 20)

ventana.mainloop()
