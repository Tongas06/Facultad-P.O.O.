from abc import ABC, abstractmethod

class ElementCollection(ABC):
    @abstractmethod
    def insert_element(self, element: int, position: int) -> None:
        pass

    @abstractmethod
    def agregar_element(self, element: int) -> None:
        pass

    @abstractmethod
    def mostrar_element(self, posicion: int) -> int:
        pass

class MyCollection(ElementCollection):
    def __init__(self):
        self.elements = []

    def insert_element(self, element: int, position: int) -> None:
        if position < 0 or position > len(self.elements):
            raise ValueError("La posición dada no es válida para la inserción")
        self.elements.insert(position, element)

    def agregar_element(self, element: int) -> None:
        self.elements.append(element)

    def mostrar_element(self, posicion: int) -> int:
        if posicion < 0 or posicion >= len(self.elements):
            raise ValueError("La posición dada no es válida para mostrar el elemento")
        return self.elements[posicion]

def main():
    my_collection = MyCollection()
    my_collection.insert_element(5, 0)
    my_collection.agregar_element(10)
    elemento = my_collection.mostrar_element(0)  # Obtenemos el elemento en la posición 1
    print(elemento)  # Imprimimos el elemento en la consola

if __name__ == "__main__":
    main()