# Elegibilidad para pago de tributo.

edad = int(input("Por favor ingresa tu edad:"))
salario = float(input("Por favor ingresa el monto de tu salario mensual:"))

if edad > 16:
    if salario > 1000:
        print("Eres elegible para pagar el impuesto especial")
else:
    print("Te encuentras exonerado de pagar el impuesto especial")