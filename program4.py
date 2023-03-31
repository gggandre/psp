# ----------------------------------------------------------
# Program 4 PSP
#
# Date: 11-Abr-2022
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
            return self.sum / self.count

    def desviacion_estandar(self):
        if self.count == 0:
            return 0
        elif self.count == 1:
            return 0
        else:
            media = self.media()
            variance = (self.suma_cuadrados - (self.sum ** 2) / self.count) / (self.count - 1)
            stdev = math.sqrt(variance)
            return stdev

    def calcular_rangos(self):
        media = self.media()
        desviacion = self.desviacion_estandar()
        muy_pequeno = media - 2 * desviacion
        pequeno = media - desviacion
        mediano = media + desviacion
        grande = media + 2 * desviacion
        muy_grande = media + 3 * desviacion

        return {
            "muy_pequeno": muy_pequeno,
            "pequeno": pequeno,
            "mediano": mediano,
            "grande": grande,
            "muy_grande": muy_grande
        }


print("Este programa calcula la media y la desviación estándar de n números dados por el usuario")
numeros = int(float(input("Ingresa el número de números reales a calcular: ")))
linked_list = LinkedList()

for i in range(numeros):
    num = float(input("Ingresa el número real {}: ".format(i+1)))
    linked_list.agrega_nodo(num)

print("Media: {}".format(linked_list.media()))
print("Desviación Estándar: {}".format(linked_list.desviacion_estandar()))

rangos = linked_list.calcular_rangos()

print("Rango Muy Pequeño: menor que {}".format(rangos["muy_pequeno"]))
print("Rango Pequeño: entre {} y {}".format(rangos["muy_pequeno"], rangos["pequeno"]))
print("Rango Mediano: entre {} y {}".format(rangos["pequeno"], rangos["mediano"]))
print("Rango Grande: entre {} y {}".format(rangos["mediano"], rangos["grande"]))
print("Rango Muy Grande: mayor que {}".format(rangos["muy_grande"]))
