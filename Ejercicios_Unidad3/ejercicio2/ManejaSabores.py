import csv
from claseSabor import Sabor

class ManejaSabores:
    def __init__(self):
        self.__sabores = []
    
    def load_sabores(self, filename):
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                idSabor = int(row[0])
                nombreSabor = row[1]
                ingredientes = row[2]
                sabor = Sabor(idSabor, nombreSabor, ingredientes)
                self.__sabores.append(sabor)
