frase = input("Escribe una frase:\n")
letra = input("Escribe una letra:\n")
cont=0
for i in frase:
    if i == letra:
        cont+=1

print("La letra " + letra + " aparece " + str(cont) + " veces ")