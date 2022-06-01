calificacion = input("Introduce tu calificación de Az-900")

calificacion = int(calificacion)

#Indentación = sangría que indica que la linea de codigo pertenece al código
if calificacion < 700 : #dos puntos para indicar en donde empieza el if
    print("No pasaste, por no estudiar")
elif calificacion > 1000: #otra condicional que te permite limitar
    print("Oso, oso, eso es mentira")
else:
    print("Felicidades, pasa por tu certificado")


#Verificador de mayoría de edad
edad = input("Introduce tu edad")
edad = int(edad)

if edad >= 18 and edad <= 100: #Agregamos operador and
    print("Ya eres mayor de edad")
elif edad > 100:
    print("Nmms estas robando oxigeno xd")
elif edad < 0:
    print("Nmms sigues siendo un feto xd")
else :
    print("Sigues siendo menor de edad")

#En Pyhton NO hay switch case

