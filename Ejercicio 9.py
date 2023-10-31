# Pedir al usuario un número entero
número_filas = int(input("Por favor, ingresa un número entero: "))

# Verificar que el número de filas sea un número positivo
if número_filas <= 0:
    print("El número de filas debe ser un número positivo.")
else:
    # Usar un bucle for para iterar a través de las filas
    for fila in range(1, número_filas + 1):
        # Inicializar el primer número de la fila
        numero = 2 * fila - 1
        
        # Usar otro bucle for para imprimir los números en cada fila
        for i in range(fila):
            print(numero, end=" ")
            numero -= 2
        
        # Imprimir una línea en blanco para separar las filas
        print()