from tkinter import *
from tkinter import messagebox
from datetime import datetime
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
ventana.geometry("400x300")
ventana.iconbitmap("runner.ico")

# Podes quitar el comentario para ver la imagen si te interesa.
# imagenL = PhotoImage(file="imagen1.png")
# labelimagen = Label(ventana,image=imagenL).place(x=0,y=0)
    
def Enviardatos():
    textoprint = text1.get()
    messagebox.showinfo("Corriste: ", textoprint)
    ventana.destroy()

label1 = Label(ventana, text = "¿Cuantos minutos corriste hoy?")
label1.place(x = 20,y = 120)
label1.config(fon = FONT_SMALL)
label1.config(bg = COLOR_WHITE, fg = COLOR_BLACK)

label2 = Label(ventana, text = str(currentDate) + " \n" + str(currentTime), anchor="e", justify=LEFT)
label2.place(x = 20,y = 50)
label2.config(fon = ("lato", 20))
label2.config(bg = COLOR_WHITE, fg = COLOR_BLACK)

text1 = Entry(ventana)
text1.pack()
text1.place(x = 20, y = 150)

#botones
boton_nuevo = Button(ventana, text = "Nuevo Registro ", fon = FONT_SMALL).place(x = 20, y = 200)
boton_guardar = Button(ventana, text = "Guardar ", fon = FONT_SMALL, command = Enviardatos).place(x = 150, y = 200)

def fecha_hora():
    now = datetime.now()
    messagebox.showinfo("Fecha y Hora", now)

#En vez de usar el boton pensaba en mostrar la hora todo el tiempo. 
#En ningun programa he visto que tengas que usar un boton para ver la hora
#botonfecha_hora = Button(ventana,text = "Fecha y hora ", command = fecha_hora).place (x = 20, y = 20)

ventana.mainloop()
