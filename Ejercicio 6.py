# Pedir al usuario su edad
edad = int(input("Por favor, ingresa tu edad: "))

# Verificar que la edad sea un número positivo
if edad <= 0:
    print("La edad debe ser un número positivo.")
else:
    # Usar un bucle for para mostrar todos los años que ha cumplido
    print("Años que has cumplido:")
    for i in range(1, edad + 1):
        print(i)