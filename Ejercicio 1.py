# Almacena la contraseña en una variable
contrasena_guardada = "ContraseñaSegura"

while True:
    # Pide al usuario que ingrese la contraseña
    contrasena_ingresada = input("Ingrese su contraseña: ")

    # Compara las contraseñas sin importar mayúsculas y minúsculas
    if contrasena_guardada.lower() == contrasena_ingresada.lower():
        print("¡Contraseña correcta!")
        break  # Sale del bucle si la contraseña es correcta
    else:
        print("Contraseña incorrecta. Inténtelo de nuevo.")