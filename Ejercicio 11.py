# Pedir al usuario una palabra
palabra = input("Por favor, ingresa una palabra: ")

# Usar un bucle for para recorrer las letras en orden inverso
for i in range(len(palabra) - 1, -1, -1):
    letra = palabra[i]
    print(letra)