# Tarea 2 Andrea Mercado
## Creación de un objeto range

# 1. Mutabilidad
print("Mutabilidad:")
r = range(0, 10)
try:
    r[0] = 5
except TypeError as e:
    print("Range es inmutable:", e)

# 2. Suma
print("\nSuma:")
try:
    r1 = range(0, 5)
    r2 = range(5, 10)
    resultado = r1 + r2
    print("Rango sumado:", resultado)
except TypeError as e:
    print("Range no permite suma:", e)

# 3. Producto por un entero
print("\nProducto por un entero:")
try:
    r3 = r1 * 2
    print("Rango multiplicado:", r3)
except TypeError as e:
    print("Range no permite producto por un entero:", e)

# 4. Slicing
print("\nSlicing:")
try:
    r4 = r[1:5]
    print("Slicing de rango:", r4)
except TypeError as e:
    print("Range no permite slicing:", e)

# 5. Convertir a lista o tupla
print("\nConversión a lista o tupla:")
lista = list(r)
tupla = tuple(r)
print("Lista:", lista)
print("Tupla:", tupla)

# 6. Función len
print("\nFunción len:")
print("Longitud del rango:", len(r))
