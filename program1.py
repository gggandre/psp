# ----------------------------------------------------------
# Program 1 PSP
#
# Date: 24-Feb-2022
# Authors:
#           A01753176 Gilberto André García Gaytán
# ----------------------------------------------------------
import math


class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
        self.sum = 0
        self.suma_cuadrados = 0

    def agrega_nodo(self, data):
        nodo_nuevo = Nodo(data)
        nodo_nuevo.next = self.head
        self.head = nodo_nuevo
        self.count += 1
        self.sum += data
        self.suma_cuadrados += data ** 2

    def media(self):
        if self.count == 0:
            return 0
        else:
            return round(self.sum / self.count, 2)

    def desviacion_estandar(self):
        if self.count == 0:
            return 0
        elif self.count == 1:
            return 0
        else:
            media = self.media()
            variance = (self.suma_cuadrados - (self.sum ** 2) / self.count) / (self.count - 1)
            stdev = math.sqrt(variance)
            return round(stdev, 2)


print("Este programa calcula la media y la desviación estándar de n números dados por el usuario")
numeros = int(float(input("Ingresa e número de números reales a calcular: ")))
linked_list = LinkedList()

for i in range(numeros):
    num = float(input("Ingresa el número real {}: ".format(i+1)))
    linked_list.agrega_nodo(num)

print("Media: {}".format(linked_list.media()))
print("Desviacion Estándar: {}".format(linked_list.desviacion_estandar()))
