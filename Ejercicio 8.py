# Usar un bucle for para iterar a través de los números del 1 al 10
for multiplicando in range(1, 11):
    print(f"Tabla de multiplicar del {multiplicando}:")
    
    # Usar otro bucle for para calcular los productos y mostrar la tabla
    for multiplicador in range(1, 11):
        producto = multiplicando * multiplicador
        print(f"{multiplicando} x {multiplicador} = {producto}")
    
    # Imprimir una línea en blanco para separar las tablas
    print()