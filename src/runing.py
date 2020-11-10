from tkinter import *

ventana=Tk()
ventana.title("Programa de Running")
ventana.geometry("500x400")



    
frame=Frame(ventana)
frame.pack()
frame.config(bg="#00CED1",width=300, height=250)
frame.place(y=10, x=100)


#etiqueta
label1=Label(frame,text="Digite la cantidad de minutos que corrio hoy")
label1.config(bg="#DCDCDC",fg="black")
label1.place(y=8,x=45)

#campo de texto
text1=Entry(frame)
text1.place(y=55,x=45)

#botones

boton_nuevo=Button(frame,text=" Nuevo Registro ")
boton_nuevo.config(y=90, x=55)

boton_guardar=Button(frame,text=" Guardar ")
boton_guardar.config(y=90, x=35)

ventana.mainloop()
