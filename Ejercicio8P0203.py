# Tabla de Multiplicar.

numero = int(input("Por favor ingresa un número del 1 al 10 para conocer su tabla de multiplicación:"))

for i in range(1,11):
    tabla = numero * i
    print(numero, "X", i, "=", tabla)