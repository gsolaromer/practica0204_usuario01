# Solicitar al usuario su nombre
nombre = input("Ingrese su nombre: ")

# Solicitar al usuario su sexo
sexo = input("Ingrese su sexo (M para mujer, H para hombre): ")

# Convertir el nombre a minúsculas para facilitar la comparación
nombre = nombre.lower()

# Verificar a qué casa pertenece el usuario
if (sexo == 'm' and nombre < 'm') or (sexo == 'h' and nombre > 'n'):
    casa = "Gryffindor"
else:
    casa = "Slytherin"

print("Usted pertenece a la casa de", casa)