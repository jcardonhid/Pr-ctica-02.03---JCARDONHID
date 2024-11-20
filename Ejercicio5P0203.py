# Los alumnos de Hogwarts se han dividido en dos casas: Gryffindor y Slytherin

nombre = str(input("Por favor ingresa tu nombre:"))
genero = str(input("Por favor indica si eres mujer u hombre:"))
letra = ord(nombre[0])

if genero.lower() == 'mujer':
    if 65<=letra<=76 or 97<=letra<=108:
        print("Te han asignado a la Casa de Gryffindor")
    else:
        print("Te han asignado a la Casa de Slytherin")
elif genero.lower() == 'hombre':
    if 79<=letra<=90 or 111<=letra<=122:
        print("Te han asignado a la Casa de Gryffindor")
    else:
        print("Te han asignado a la Casa de Slytherin")
    
        
        
    


