"""
    Ejemplo básicos de una lista en Python
"""

# Declaración de una lista sin valores
mi_lista = []

# Declaración de una lista con valores dados
mi_lista_01 = [1, 2, 3, 10, 8, 9]

# Declaración de una lista con valores por defecto (0), de acuerdo
# a un tamaño conocido
# Crea una lista con 10 elementos, todos inicializados en 0
mi_lista = [0]*10

# Presentación en pantalla de una lista
print(mi_lista_01) # Salida: [1, 2, 3, 10, 8, 9]

# Presentación en pantalla de una posición determinada de la lista
print(mi_lista_01[0]) # Salida: 1 (Primer elemento)
print(mi_lista_01[4]) # Salida: 8 (Quinto elemento, índice 4)

# Obtener el número de elementos de un arreglo, usando la función len
numero_elementos = len(mi_lista_01)

print("Número de elementos de la lista: %d" % (numero_elementos))
# Salida: Número de elementos de la lista: 6

# agregar elementos a un arreglos
mi_lista_01.append(100)

# Eliminar un elemento de una posición determinada, siempre y cuando el índice exista
del mi_lista_01[3]

print(mi_lista_01)


# Creción de una lista con diferentes tipos de datos en cada posición
mi_lista_02 = ["1", "Loja", 13, 10.2, True, 9]

# Presentación de la lista con tipos datos diversos
print(mi_lista_02)  
# Salida: ['1', 'Loja', 13, 10.2, True, 9]



