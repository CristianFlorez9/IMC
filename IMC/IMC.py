from tkinter import *

# Función para calcular el IMC
def calcular_imc():
    try:
        altura_valor = float(altura.get())
        peso_valor = float(peso.get())
        imc = peso_valor / (altura_valor ** 2)
        resultado_label.config(text=f"Tu imc es de {imc:.2f}")   # .2f para redondear resultado hacia dos decimales
    except ValueError:
        resultado_label.config(text="Por favor, ingrese valores válidos.")

# Crear la ventana principal
raiz = Tk()
raiz.title("Índice de masa corporal")
raiz.resizable(1, 1)
raiz.iconbitmap("pesoBien.ico")
raiz.geometry("650x350")

frame = Frame(raiz)
frame.config(width="1920", height="1080")
frame.pack()

label1 = Label(frame, text="CALCULADORA DE IMC", font=("Times New Roman", 20))
label1.place(x=600, y=5)

miImagen1= PhotoImage(file="run.gif")
label2 = Label(frame, image=miImagen1)
label2.place(x=450, y=50)

Imagen2=PhotoImage(file="imc.gif")
labelimc=Label(frame, image=Imagen2)
labelimc.place(x=850,y=460)

label3 = Label(frame, text="Altura:", font=("Times new Roman", 15))
label3.place(x=500, y=500)

label4 = Label(frame, text="Peso:", font=("Times new Roman", 15))
label4.place(x=500, y=530)

label5 = Label(frame, text="Ingrese su Peso (KG) y Altura (Metros):", font=("Times New Roman", 15))
label5.place(x=500, y=440)

altura = Entry(frame)
altura.place(x=565, y=505)

peso = Entry(frame)
peso.place(x=565, y=535)

# Crear un botón que llame a la función calcular_imc cuando se presione
boton = Button(frame, text="Calcular IMC", command=calcular_imc)
boton.place(x=565, y=565)

# Label para mostrar el resultado del IMC
resultado_label = Label(frame, text="", font=("Times New Roman", 15))
resultado_label.place(x=500, y=600)

raiz.mainloop()


