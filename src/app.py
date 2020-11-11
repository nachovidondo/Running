from tkinter import *
from tkinter import messagebox
from datetime import datetime

ventana=Tk()
ventana.title("Programa de Running")
ventana.config(bg="#D8D8D8")
ventana.geometry("400x300")
ventana.iconbitmap("runner.ico")

imagenL=PhotoImage(file="imagen1.png")
labelimagen=Label(ventana,image=imagenL).place(x=0,y=0)


def nuevo():
    text1.config (state='normal')
    
def Enviardatos():
    textoprint= text1.get( )
    messagebox.showinfo( "corriste : ",textoprint)
    ventana.destroy()






label1=Label(ventana,text="¿Cuantos minutos corriste hoy? ")
label1.place(x=20,y=120)
label1.config(fon=("lato",10))

label1.config(bg="#DCDCDC",fg="black")




text1=Entry(ventana)
text1.pack()
text1.place(y=120,x=230)


#botones
boton_nuevo=Button(ventana,text=" Nuevo Registro ",fon=("lato",10)).place(x=180,y=200)


boton_guardar=Button(ventana,text=" Guardar ",fon=("lato",10),command=Enviardatos).place(x=320,y=200)


ventana.mainloop()
