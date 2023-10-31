# Pedir al usuario un número entero
altura = int(input("Por favor, ingresa un número entero: "))

# Verificar que la altura sea un número positivo
if altura <= 0:
    print("La altura debe ser un número positivo.")
else:
    # Usar un bucle for para imprimir el triángulo
    for i in range(1, altura + 1):
        print('*' * i)