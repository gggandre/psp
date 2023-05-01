# ----------------------------------------------------------
# Program 5 PSP
#
# Date: 01-May-2023
# Authors:
#           A01753176 Gilberto André García Gaytán
# ----------------------------------------------------------

import math


def t_distribution(x, df):
    """
    Función que devuelve el valor de la distribución t para una variable
    x y grados de libertad df.
    """
    num = math.gamma((df+1)/2)
    den = math.sqrt(df * math.pi) * math.gamma(df/2)
    return (num / den) * math.pow(1 + (math.pow(x, 2) / df), -(df+1)/2)


def simpsons_rule_integration(f, a, b, n):
    """
    Función que implementa el método de Simpson's rule para calcular
    la integral de la función f
    en el intervalo [a, b] utilizando n segmentos.
    """
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            s += 2 * f(x)
        else:
            s += 4 * f(x)
    return (h / 3) * s


if __name__ == '__main__':
    # Pedir al usuario los límites de integración y el número de segmentos.
    a = float(input("Ingrese el límite inferior de integración: "))
    b = float(input("Ingrese el límite superior de integración: "))
    n = int(input("Ingrese el número de segmentos: "))

    # Calcular la integral de la distribución t utilizando Simpson's rule.
    df = 10  # Grados de libertad
    integral = simpsons_rule_integration(lambda x: t_distribution(x, df),
                                         a, b, n)

    # Mostrar el resultado de la integral.
    print(f"La integral de la distribución t con {df} grados de libertad en "
          f"el intervalo [{a}, {b}] es {integral:.6f}.")
