edad = int(input("Escribe tu edad porfavor:\n"))
sueldo = int(input("Escribe tus ingresos mensuales: \n"))

if edad > 16 and sueldo >= 1000:
    print("Tienes que tributar")
else:
    print("No tienes que tributar")