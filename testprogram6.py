from program6 import find_x

p_values = [0.2, 0.45, 0.495]
dof_values = [6, 15, 4]
expected_x_values = [0.55338, 1.75305, 4.60409]

for p, dof, expected_x in zip(p_values, dof_values, expected_x_values):
    actual_x = find_x(p, dof)
    print(f"Prueba: p={p}, dof={dof}")
    print(f"x esperado: {expected_x}")
    print(f"x actual: {actual_x}")
    if abs(actual_x - expected_x) <= 0.01:
        print("Resultado: Pass🛂")
    else:
        print("Resultado: Failed⚠️")
    print()
