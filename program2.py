# ----------------------------------------------------------
# Program 2 PSP
#
# Date: 27-Feb-2022
# Authors:
#           A01753176 Gilberto André García Gaytán
# ----------------------------------------------------------

import re


def cuenta_lineas(archivo):
    """
    It counts the number of lines of code in a Python file, ignoring comments
    and blank lines :param nombre_archivo: The name of the file to
    count lines of code in:return: The number of lines of code in the file.
    """
    lineas = 0
    tamaños = {"Funciones": 0, "Clases": 0, "Procedimientos": 0, "Otros": 0}
    with open(archivo, 'r') as archivo:
        comentario_comilla = False
        for linea in archivo:
            linea = linea.strip()
            if linea.startswith('"""') and not comentario_comilla:
                comentario_comilla = True
                continue
            elif linea.endswith('"""') and comentario_comilla:
                comentario_comilla = False
                continue
            if comentario_comilla or not linea or linea.startswith('#') or re.match(r'^import\s+', linea):
                continue
            lineas += 1
            items = {"comentarios": 0, "asignaciones": 0,
                     "llamadas": 0, "otro": 0}
            for char in linea:
                if char == "#":
                    items["comentarios"] += 1
                elif char == "=":
                    items["asignaciones"] += 1
                elif char == "(" or char == ")":
                    items["llamadas"] += 1
                else:
                    items["otro"] += 1
            print(f"Línea: {linea}\nItems: {items}\n")
            if re.match(r'^def\s+', linea):
                tamaños["Funciones"] += 1
            elif re.match(r'^class\s+', linea):
                tamaños["Clases"] += 1
            elif re.match(r'^async def\s+', linea):
                tamaños["Procedimientos"] += 1
            else:
                tamaños["Otros"] += 1
    print(f"Tamaño de cada parte del programa: {tamaños}")
    return lineas


# A way to make sure that the code in the block is only
# executed when the file is run as a script, not
# when it is imported as a module.
if __name__ == '__main__':
    archivo = input("Ingrese el nombre del archivo: ")
    lineas = cuenta_lineas(archivo)
    print(f"Este archivo {archivo} tiene {lineas} líneas de código.")
