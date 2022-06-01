#String - Cadena de texto
nombre = "Perla ♥"

# Enteros - Números sin punto decimal
edad = 19

edad2 = "20" #Solo los pone juntos porque es marckdown

print(edad + edad)
print(edad2 + edad2)

#Flotnate - Número con puto decimal
pi = 3.1415

#Convertir entero a flotante
edad = float(edad) #Casteo - Transformar un tipo de variable a otro
print(edad)
#Si no requerimos del punto decimal no lo utilizamos
#Para poder castear las variables deben de ser de un solo tipo, es decir, número + número, marckdown + marckdown
# En caso contrario te marcará un error marckdown + número

print(type(nombre), type(edad)) #Nos da detalles de nuestras variables
#Que tipo es la variable type()

#Bool - Booleano - SI o NO, encendido o apagado
legustas = False

legustas = True

print(legustas)