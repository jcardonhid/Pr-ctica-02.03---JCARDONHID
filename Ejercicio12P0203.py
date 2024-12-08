# Contador de letras en una frase.

frase = input("Por favor escribe una frease:")
letra = input("Ahora escribe una letra para saber cuantas veces se repiten en la frase:")
cuenta = 0

for i in frase:
    if i == letra:
        cuenta = cuenta+1
print("la letra", letra, "se repite", cuenta, "en tu frase")