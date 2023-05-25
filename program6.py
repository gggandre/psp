from math import gamma, sqrt, exp, log, pi


def t(x, dof):
    """
    Calcula el valor de la función t en un punto dado x y grados
    de libertad dof.

    Args:
        x (float): Punto en el que se evalúa la función t.
        dof (int): Grados de libertad.

    Returns:
        float: Valor de la función t en el punto dado.
    """
    numerator = gamma((dof + 1) / 2)
    denominator = (sqrt(dof * pi) * gamma(dof / 2))
    exponent = -((dof + 1) / 2) * log(1 + (x ** 2) / dof)
    return numerator / denominator * exp(exponent)


def integrate_t(x, dof):
    """
    Realiza la integración numérica de la función t en el intervalo [0, x]
    utilizando el método del trapecio.

    Args:
        x (float): Límite superior del intervalo.
        dof (int): Grados de libertad.

    Returns:
        float: Valor de la integral de la función t en el intervalo [0, x].
    """
    n = 1000
    dx = x / n
    suma = t(0, dof) + t(x, dof)

    for i in range(1, n):
        if i % 2 == 0:
            suma += 2 * t(i * dx, dof)
        else:
            suma += 4 * t(i * dx, dof)

    return (dx / 3) * suma


def find_x(p, dof, error=0.00001):
    """
    Encuentra el valor de x que cumple con la ecuación integral p = P(T <= x)
    para una distribución t de Student.
    Args:
        p (float): Probabilidad deseada.
        dof (int): Grados de libertad.
        error (float, optional): Error permitido en el resultado.
        Defaults to 0.00001.
    Returns:
        float: Valor de x que cumple con la ecuación integral.
    """
    x_min = 0.0
    x_max = 10.0

    while True:
        x_mid = (x_min + x_max) / 2
        result = integrate_t(x_mid, dof)

        if abs(result - p) <= error:
            break

        if result < p:
            x_min = x_mid
        else:
            x_max = x_mid

    return x_mid


if __name__ == "__main__":
    p = float(input("Ingrese el valor de p: "))
    dof = int(input("Ingrese el valor de dof: "))
    expected_x = float(input("Ingrese el valor esperado de x: "))

    actual_x = find_x(p, dof)

    print(f"Prueba: p={p}, dof={dof}")
    print(f"x esperado: {expected_x}")
    print(f"x actual: {actual_x}")
    print(f"Resultado: {actual_x}")
