while True:
    # Solicitar al usuario dos números
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))

    # Verificar si el divisor es cero
    if numero2 == 0:
        print("Error: No se puede dividir por cero. Intente nuevamente.")
    else:
        # Realizar la división y mostrar el resultado
        resultado = numero1 / numero2
        print("El resultado de la división es:", resultado)
        break  # Salir del bucle si la división se realizó con éxito