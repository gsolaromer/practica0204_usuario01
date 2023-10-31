while True:
    entrada = input("Introduce algo (o escribe 'salir' para terminar): ")
    
    if entrada.lower() == "salir":
        print("¡Saliendo del programa!")
        break
    else:
        print("Eco: " + entrada)