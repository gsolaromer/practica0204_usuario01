# Pedir al usuario una frase
frase = input("Por favor, ingresa una frase: ")

# Pedir al usuario una letra
letra = input("Por favor, ingresa una letra: ")

# Inicializar un contador para el número de veces que aparece la letra
contador = 0

# Usar un bucle for para contar las ocurrencias de la letra en la frase
for caracter in frase:
    if caracter == letra:
        contador += 1

# Mostrar el resultado
print(f'La letra "{letra}" aparece {contador} veces en la frase: "{frase}"')