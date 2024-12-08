# Triangulo de números primos.

n=int(input("Por favor ingresa un número entero para formar un triangulo de números primos:"))

for j in range(1,n+1,1):
    print("")
    for i in range(2*j-1,0,-2):
         print(i,end="")