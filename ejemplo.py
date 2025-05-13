
# Inicio

# Solicitar el tamaño del arreglo
tamanio = int(input("Ingrese el tamaño del arreglo: "))  # Captura el tamaño ingresado por el usuario

# Declaración del arreglo con el tamaño ingresado
numeros = [0] * tamanio  # Se crea una lista de tamaño 'tamanio' inicializada en 0

# Acumulador de cadena para almacenar los valores ingresados
valoresIngresados = "Valores ingresados:\n"

# Ingresar valores en el arreglo con validación
for indice in range(tamanio):
    numero = int(input(f"Ingrese un número para la posición {indice + 1}: "))  # Captura del usuario

    # Verificación del rango permitido (20-40)
    if numero >= 20 and  numero <= 40:
        numeros[indice] = numero  # Se almacena el número ingresado
    else:   
        numeros[indice] = 100  # Se asigna 100 si el número no está en el rango permitido

# Agregar los valores a la cadena acumuladora
for i in numeros: # se hace uso de la secuencia con los valores previos ingresados
    valoresIngresados = f"{valoresIngresados}{i}\n"  # Concatenar valores a la cadena

# Mostrar los resultados
print(valoresIngresados)

# Fin
