# Tarea 4 Andrea Mercado

# Ejercicio 1
calif_1 = 10
calif_2 = 7
calif_3 = 4

# Pesos
peso_1 = 0.15
peso_2 = 0.35
peso_3 = 0.50

# Calcular el promedio ponderado
promedio = (calif_1 * peso_1) + (calif_2 * peso_2) + (calif_3 * peso_3)

print(f"El promedio ponderado de las calificaciones es: {promedio}")

# Ejercicio 2
matriz = [
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
]

# Corregir la matriz
for fila in matriz:
    fila[3] = sum(fila[:3])

print("Matriz corregida:")
for fila in matriz:
    print(fila)