from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import pafy
import threading

#componentes de la ventana
ventana = Tk()
ventana.geometry("720x500") 
ventana.configure(background="gray80")
ventana.title("LS Youtube Downloader")
URLL = StringVar()
directorio_actual = StringVar()


    #imagenes para los botones y el fondo
imgBoton_select = PhotoImage(file ="./imagenes/btn_dir_select.png")
imgBoton_descargarV = PhotoImage(file = "./imagenes/btn_Video.png")
imgBoton_descargarAud = PhotoImage(file = "./imagenes/btn_Audio.png")
imgBoton_exit = PhotoImage(file= "./imagenes/btn_salir.png")
imgBotonLimpiar = PhotoImage(file = "./imagenes/limpiar.png")

    #contenido de la ventanica
entrada = Entry(ventana, font=('Arial', 15, 'bold'), textvariable=URLL, width = 25)
entrada.place(x=195, y=130)

entrada2 = Entry(ventana,font=('calibri', 9), textvariable = directorio_actual,width=60)
entrada2.place(x=185, y=210)

    #labels o etiquetas
Label(ventana, font=('Arial',20, 'bold','underline'), text="LS Youtube Downloader", fg= "black").place(x=190, y=17)
Label(ventana, font=('Arial',12), text="(c) Lionel Sanchez, sn.Lionel90. Todos los derechos reservados", fg= "black").place(x=123, y=60)
Label(ventana, width=25, font=('Arial',10),text="Directorio destino").place(x=230, y =180)
Label(ventana, width=25, font=('Arial',10),text = "Insertar direccion de video").place(x=230, y = 100)

Label(ventana, width=15, text = "Descargar Video").place(x=430, y = 270)
Label(ventana, width=15, text = "Descargar Sonido").place(x=430, y = 320)
Label(ventana, width=15, text = "Seleccionar Carpeta").place(x=260, y = 270)
Label(ventana, width=15, text = "Salir").place(x=260, y = 320)

etiqueta=Label(ventana,width=12,text="PROGRESO") 
etiqueta.place(x=307,y=380)

eti_porcentaje=Label(ventana,width=4) 
eti_porcentaje.place(x=398,y=380)

    #botones
boton_dir=Button(ventana, image= imgBoton_select) #sleccionar directorio de descarga
boton_dir.place(x=200, y = 250)
btn_salir = Button(ventana,image = imgBoton_exit )# salir del programa, a la puta calle
btn_salir.place(x=200,y=300) 

btn_limpia = Button(ventana,image = imgBotonLimpiar)# salir del programa, a la puta calle
btn_limpia.place(x=480,y=110) 

boton_descarga=Button(ventana, image = imgBoton_descargarV) #DESCARGAR VIDEO
boton_descarga.place(x=380, y = 250)
boton_audio=Button(ventana, image = imgBoton_descargarAud)#descargar solo el audio
boton_audio.place(x=380, y=300)

pr = progressbar = ttk.Progressbar(ventana) #barra de progreso
pr.place(x = 196, y=400, width=335)

ventana.mainloop()

