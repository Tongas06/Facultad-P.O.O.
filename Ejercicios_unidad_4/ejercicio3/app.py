from tkinter import *
from tkinter import ttk, messagebox
import requests

class Aplicacion():
    __ventana=None
    __precio_dolares=None
    __precio_pesos=None
    
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('400x150')
        self.__ventana.title('Conversor de precios')
        mainframe = ttk.Frame(self.__ventana, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__precio_dolares = StringVar()
        self.__precio_pesos = StringVar()
        self.dolaresEntry = ttk.Entry(mainframe, width=10, textvariable=self.__precio_dolares)
        self.dolaresEntry.grid(column=2, row=1, sticky=(W, E))
        ttk.Label(mainframe, textvariable=self.__precio_pesos).grid(column=2, row=2, sticky=(W, E))
        ttk.Button(mainframe, text="Convertir", command=self.convertir).grid(column=2, row=3, sticky=W)
        ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(column=3, row=3, sticky=W)
        ttk.Label(mainframe, text="dólares").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="es equivalente a").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="pesos").grid(column=3, row=2, sticky=W)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=10, pady=10)
        self.dolaresEntry.focus()
        self.__ventana.mainloop()
    
    def obtener_cotizacion(self):
        url = "https://www.dolarsi.com/api/api.php?type=dolar"
        response = requests.get(url)
        data = response.json()
        cotizacion = data[0]['casa']['venta']
        return float(cotizacion.replace(',', '.'))

    def convertir(self):
        try:
            precio_dolares = float(self.dolaresEntry.get())
            cotizacion = self.obtener_cotizacion()
            precio_pesos = precio_dolares * cotizacion
            self.__precio_pesos.set(f"{precio_pesos:.2f}")
        except ValueError:
            messagebox.showerror(title='Error de tipo', message='Debe ingresar un valor numérico')
            self.__precio_dolares.set('')
            self.dolaresEntry.focus()

def testAPP():
    mi_app = Aplicacion()
if __name__ == '__main__':
    testAPP()