# Separación de las letras de una palabra.

palabra = str(input("Por favor ingresa una palabra:"))
letras = len(palabra)

for i in range(letras):
    if i == 0:
        print(palabra[i-1])
    elif i != 0:
        print(palabra[(i*-1)-1])


