from tkinter import *
from tkinter import ttk, messagebox

class Aplicacion():
    __ventana=None
    __vestimenta=None
    __alimentos=None
    __educacion=None

    def __init__(self):
        self.__ventana= Tk()
        self.__ventana.geometry('450x230')
        self.__ventana.title('IPC 2022/2023')
        mainframe = ttk.Frame(self.__ventana, padding="10 10 20 20")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'

        self.__vestimenta1= StringVar()
        self.__vestimenta2 = StringVar()
        self.__vestimenta3 = StringVar()
        self.__alimentos1 = StringVar()
        self.__alimentos2 = StringVar()
        self.__alimentos3 = StringVar()
        self.__educacion1 = StringVar()
        self.__educacion2 = StringVar()
        self.__educacion3 = StringVar()

        self.vestimentaEntry1 = ttk.Entry(mainframe, width=5, textvariable=self.__vestimenta1,)
        self.vestimentaEntry1.grid(column=1, row=1, sticky=(W, E))
        self.vestimentaEntry2 = ttk.Entry(mainframe, width=5, textvariable=self.__vestimenta2)
        self.vestimentaEntry2.grid(column=2, row=1, sticky=(W, E))
        self.vestimentaEntry3 = ttk.Entry(mainframe, width=5, textvariable=self.__vestimenta3)
        self.vestimentaEntry3.grid(column=3, row=1, sticky=(W, E))

        self.alimentosEntry1 = ttk.Entry(mainframe, width=5, textvariable=self.__alimentos1)
        self.alimentosEntry1.grid(column=1, row=2, sticky=(W, E))
        self.alimentosEntry2 = ttk.Entry(mainframe, width=5, textvariable=self.__alimentos2)
        self.alimentosEntry2.grid(column=2, row=2, sticky=(W, E))
        self.alimentosEntry3 = ttk.Entry(mainframe, width=5, textvariable=self.__alimentos3)
        self.alimentosEntry3.grid(column=3, row=2, sticky=(W, E))

        self.educacionEntry1 = ttk.Entry(mainframe, width=5, textvariable=self.__educacion1)
        self.educacionEntry1.grid(column=1, row=3, sticky=(W, E))
        self.educacionEntry2 = ttk.Entry(mainframe, width=5, textvariable=self.__educacion2)
        self.educacionEntry2.grid(column=2, row=3, sticky=(W, E))
        self.educacionEntry3 = ttk.Entry(mainframe, width=5, textvariable=self.__educacion3)
        self.educacionEntry3.grid(column=3, row=3, sticky=(W, E))

        ttk.Button(mainframe, text="Calcular", command=self.calcular).grid(column=1, row=6, sticky=W)
        ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(column=3, row=6, sticky=W)

        ttk.Label(mainframe, text="Item").grid(column=0, row=0, sticky=W)
        ttk.Label(mainframe, text="Cantidad").grid(column=1, row=0, sticky=W)
        ttk.Label(mainframe, text="Precio Base").grid(column=2, row=0, sticky=W)
        ttk.Label(mainframe, text="Precio Actual").grid(column=3, row=0, sticky=W)

        ttk.Label(mainframe, text="Vestimenta").grid(column=0, row=1, sticky=W)
        ttk.Label(mainframe, text="Alimentos").grid(column=0, row=2, sticky=W)
        ttk.Label(mainframe, text="Educacion").grid(column=0, row=3, sticky=W)

        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=20, pady=10)
        
        self.vestimentaEntry1.focus()
        self.__ventana.mainloop()

    def calcular(self):
        try:
            vestimenta1 = float(self.__vestimenta1.get())
            vestimenta2 = float(self.__vestimenta2.get())
            vestimenta3 = float(self.__vestimenta3.get())
            alimentos1 = float(self.__alimentos1.get())
            alimentos2 = float(self.__alimentos2.get())
            alimentos3 = float(self.__alimentos3.get())
            educacion1 = float(self.__educacion1.get())
            educacion2 = float(self.__educacion2.get())
            educacion3 = float(self.__educacion3.get())

            total1 = vestimenta1 * vestimenta3 / (vestimenta1 * vestimenta2)
            total2 = alimentos1 * alimentos3 / (alimentos1 * alimentos2)
            total3 = educacion1 * educacion3 / (educacion1 * educacion2)

            messagebox.showinfo('Total', 'El total para vestimenta es: {}'.format(total1))
            messagebox.showinfo('Total', 'El total para alimentos es: {}'.format(total2))
            messagebox.showinfo('Total', 'El total para educacion es: {}'.format(total3))
        except ValueError:
            messagebox.showerror(title='Error de tipo', message='Debe ingresar valores numericos')


def testAPP():
    mi_app = Aplicacion()
if __name__ == '__main__':
    testAPP()