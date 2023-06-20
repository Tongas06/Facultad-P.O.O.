import tkinter as tk
from tkinter import *

def calcular_iva():
    precio_base = float(entrada_precio_base.get())
    tasa_iva_val = tasa_iva.get()
    iva = precio_base * tasa_iva_val / 100
    precio_con_iva = precio_base + iva
    entrada_iva.delete(0, END)
    entrada_iva.insert(0, f"{iva:.2f}")
    entrada_precio_con_iva.delete(0, END)
    entrada_precio_con_iva.insert(0, f"{precio_con_iva:.2f}")

def cerrar_aplicacion():
    root.destroy()

root = Tk()
root.geometry("300x250")
root.resizable(0, 0)
root.title("Calculadora de IVA")

titulo = Label(root, text="Cálculo de IVA", font=("Arial", 16))
titulo.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

label_precio_base = Label(root, text="Precio base:")
label_precio_base.grid(row=1, column=0, padx=5, pady=5)

tasa_iva = DoubleVar()

radio_button_iva_105 = Radiobutton(root, text="IVA 10.5%", variable=tasa_iva, value=10.5)
radio_button_iva_105.grid(row=3, column=0, padx=5, pady=5)

radio_button_iva_21 = Radiobutton(root, text="IVA 21%", variable=tasa_iva, value=21)
radio_button_iva_21.grid(row=2, column=0, padx=5, pady=5)

resultado_iva = Label(root, text="IVA: ")
resultado_iva.grid(row=4, column=0, padx=5, pady=5)

entrada_iva = Entry(root)
entrada_iva.grid(row=4, column=1, padx=5, pady=5)

resultado_precio_con_iva = Label(root, text="Precio con IVA: ")
resultado_precio_con_iva.grid(row=5, column=0, padx=5, pady=5)

entrada_precio_con_iva = Entry(root)
entrada_precio_con_iva.grid(row=5, column=1, padx=5, pady=5)

entrada_precio_base = Entry(root)
entrada_precio_base.grid(row=1, column=1, padx=5, pady=5)

boton_calcular = Button(root, text="Calcular", command=calcular_iva)
boton_calcular.grid(row=6, column=0, padx=5, pady=5)

boton_salir = Button(root, text="Salir", command=cerrar_aplicacion)
boton_salir.grid(row=6, column=1, padx=5, pady=5)

root.mainloop()
