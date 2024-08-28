# Tarea 3 Andrea Mercado

# Diccionario de ejemplo
mi_dict = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Madrid'}

# pop(key) - Remueve y devuelve el valor asociado a la clave
valor_pop = mi_dict.pop('edad')
print("Resultado de pop('edad'):", valor_pop)
print("Diccionario después de pop:", mi_dict)

# get(key) - Devuelve el valor de la clave si existe, sino None
valor_get = mi_dict.get('nombre')
print("\nResultado de get('nombre'):", valor_get)

# copy() - Devuelve una copia superficial del diccionario
mi_dict_copia = mi_dict.copy()
print("\nCopia del diccionario:", mi_dict_copia)

# keys() - Devuelve las claves del diccionario
claves = mi_dict.keys()
print("\nClaves del diccionario:", list(claves))

# items() - Devuelve los pares clave-valor como tuplas
items = mi_dict.items()
print("\nElementos del diccionario:", list(items))

# clear() - Vacía el diccionario
mi_dict.clear()
print("\nDiccionario después de clear:", mi_dict)

# fromkeys(iterable, value) - Crea un nuevo diccionario con claves de un iterable y valores definidos
nuevo_dict = dict.fromkeys(['a', 'b', 'c'], 0)
print("\nDiccionario creado con fromkeys:", nuevo_dict)

# popitem() - Remueve y devuelve el último par clave-valor insertado
ultimo_item = nuevo_dict.popitem()
print("\nResultado de popitem:", ultimo_item)
print("Diccionario después de popitem:", nuevo_dict)

# setdefault(key, default_value) - Devuelve el valor de una clave, si no existe la añade con el valor por defecto
valor_predeterminado = nuevo_dict.setdefault('d', 1)
print("\nResultado de setdefault('d', 1):", valor_predeterminado)
print("Diccionario después de setdefault:", nuevo_dict)

# update(dict) - Actualiza el diccionario con pares clave-valor de otro diccionario o iterable
nuevo_dict.update({'e': 2, 'f': 3})
print("\nDiccionario después de update:", nuevo_dict)

# values() - Devuelve los valores del diccionario
valores = nuevo_dict.values()
print("\nValores del diccionario:", list(valores))
