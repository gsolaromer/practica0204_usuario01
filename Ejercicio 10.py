# Definir la contraseña
contraseña_correcta = "contraseña"

# Pedir al usuario que ingrese la contraseña
while True:
    contraseña = input("Por favor, ingresa la contraseña: ")
    
    # Comprobar si la contraseña es correcta
    if contraseña == contraseña_correcta:
        print("¡Contraseña correcta! Acceso concedido.")
        break  # Salir del bucle si la contraseña es correcta
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.")