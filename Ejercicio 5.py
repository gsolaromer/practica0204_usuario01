nombre = input("Escribe tu nombre:\n")
sexo = input("Escribe tu sexo como M o H: \n")

if sexo == "M":
    if nombre.lower()<"m":
        print("Tu grupo es Gryffindor")
    else:
        print("Tu grupo es Slytheryn")

else:
    if nombre.lower()>"n":
        print("Tu grupo es Slytheryn")
    else:
        print("tu grupo es Gryffindor")