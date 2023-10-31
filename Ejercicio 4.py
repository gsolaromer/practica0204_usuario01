# Solicitar al usuario su edad
edad = int(input("Ingrese su edad: "))

# Solicitar al usuario sus ingresos mensuales
ingresos = float(input("Ingrese sus ingresos mensuales en €: "))

# Verificar si el usuario debe tributar o no
if edad > 16 and ingresos >= 1000:
    print("Debe tributar.")
else:
    print("No debe tributar.")