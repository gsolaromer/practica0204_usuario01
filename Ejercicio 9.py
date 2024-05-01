num = int(input("Escribe un numero entero positivo:\n"))

for i in range(1,num,2):
    print("\n")
    for j in range(i,0,-2):
        print(j,end="")