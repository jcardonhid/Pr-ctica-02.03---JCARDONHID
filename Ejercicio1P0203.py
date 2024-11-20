# Verificacion de clave.

clave1 = str(input("Por favor ingresa una clave: \n"))
clave2 = str(input("Por favor confirma la clave: \n"))

if clave1.lower() == clave2.lower():
    print("La clave es correcta!")
else:
    print("La clave es incorrecta!")


