password = "HolaMundo"

contra = input("Introduce tu contraseña: \n")

if password.lower() == contra.lower():
    print("La contraseña es correcta")
else:
    print("La contraseña es incorrecta")