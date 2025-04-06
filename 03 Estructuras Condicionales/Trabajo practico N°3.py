##1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad = int(input("ingrese su edad: ")) #Pedimos al usuario que ingrese su edad.
if edad > 18:                          #Vemos si la edad es mayor a 18.
    print("Es mayor de edad :)")       #Si lo es, decimos que es mayor de edad.

##2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso 
## contrario deberá mostrar el mensaje “Desaprobado”
nota = float(input("Ingrese su calificacion: ")) #Pedimos al usuario su calificacion
if nota >= 6:                                    #Vemos si es >= a 6
    print("Aprobado :)")                         #Si lo es, imprimimos Aprobado
else:                                               
    print("Desaprobado :(")                      #Si no lo es, impriminos Desaprobado

##3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; 
## en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.
num = int(input("ingrese un numero: ")) #Pedimos al usuario un numero
if num % 2 == 0:                        #Vemos si el numero es par
    print("El numero es par!!")         #Si lo es, decimos que es par
else:                                   #Si no lo es imprimimos ese mensaje
    print("El programa solo perimite ingresar numeros pares. Por favor, ingrese un numero par.")    

##4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.
edad = int(input("Ingrese su edad: "))          #Pedimos al usuario que ingrese su edad
if edad < 12:                                   #Vemos si es menor de 12
    print("El usuario es un/a niño/a")
elif edad >= 12 and edad < 18:                  #Vemos si es mayor o igual a 12 y menor de 18
    print("El usuario es un/a adolecente")
elif edad >= 18 and edad < 30:                  #Vemos si es mayor o igual a 18 y menor de 30
    print("El usuario es un/a adulto joven")
elif edad >= 30:                                #Vemos si es mayor de 30
    print("El usuario es un adulto mayor")

##5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, 
# imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 
# Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.
print("El programa permite ingresar contraseñas desde 8 hasta 14 caracteres")   #Explicamos el programa al usuario
contraseña = input("Ingrese su contraseña: ")                                   #Pedimos que ingrese la contraseña
if len(contraseña) > 7 and len(contraseña) < 15:                                #si la contraseña esta entre los parametros
    print("Ha ingresado una contraseña correcta")                               #Enviamos este mensaje
else:                                                                           #Si no lo esta, enviamos estre otro
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

##6)escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar sihay sesgo positivo, negativo o no hay sesgo. 
# Imprimir el resultado por pantalla
import random                                       #Libreria del numero aleatorio
from statistics import mode, median, mean           #Libreria de mode, median y mena
num = [random.randint(1, 100) for i in range(50)]   #Generar numero aleatorio
#print("&&& ", num, " &&&")                         #Imprimir numero aleatorio
media = (mean(num))       #media                    Asignacion de variables
mediana = (median(num))   #mediana                  Asignacion de variables 
moda = float((mode(num))) #moda                     Asignacion de variables
print("media: ", media)                             #Imprimimos el valor de media
print("mediana: ", mediana)                         #Imprimimos el valor de mediana    
print("moda: ", moda)                               #Imprimimos el valor de moda
if media > mediana and mediana > moda:              #Condiciones para que sea positivio
    print("Sesgo positivo")
elif media < mediana and mediana < moda:            #Condiciones para que sea negativo
    print("Sesgo negativo")
elif media == mediana and media == moda:            #Condiciones para que no tenga sesgo
    print("Sin sesgo")
else:                                               #Por si no es ninguna de las tres anteriores
    print("no se hay veces que no son positivo, negativo ni sin")

##7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante 
# por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
palabra = input("ingrese una frase o palabra: ")  #Pedimos al usuario que ingrese una palabra
if palabra[-1] in "aeiou":                        #Verificamos si el ultimo caracter de la variable palabra es una vocal
    print(palabra + "!")                          #Si lo es enviamos ese mensaje
else:                                             #Si no lo es, enviamos este otro
    print(palabra)

##8)Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula
nombre = input("Ingrese su nombre: ")                               #Pedimos datos y desplegamos las opciones al usuario
print("1. nombre en mayúsculas.")
print("2. nombre en minúsculas.")
print("3. nombre con la primera letra mayúscula")
opcion = int(input("Ingrese la opcion que desee (1, 2 o 3): ")) 
if opcion == 1:
    print(nombre.upper())                                           #Convertimos el nombre a mayusculas
elif opcion == 2:
    print(nombre.lower())                                           #Convertimos el nombre a minusculas
elif opcion == 3:
    print(nombre.title())                                           #Convertimos el la primer letra del nombre a mayuscula y el resto a minuscula
else:
    print("No ingreso una opcion valida")

##9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las 
# siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
magnitud = int(input("Ingrese la magnitud del terremoto :"))                    #Pedimos la magnitud del terremoto al usuario
if magnitud < 3:                                                                #Hacemos todos los condicionales correspondientes
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

##10)Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para 
# imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
emisferio = input("Ingrese en que emisferio se encuentra (N o S): ") #Pedimos que nos den el emisferio
if emisferio == 'N' or emisferio == 'S':                             #Verificamos que todos los datos sean validos
    mes = int(input("Ingrese el mes: (1 - 12) "))                    #Tome que todos los meses tienen 31 dias porque sino era muy complicado
    if mes >= 1 and mes <= 13:                                       #El mes lo pongo primero, multiplicado por diez y luego le sumo el dia
        dia = int(input("Ingrese el dia (1 - 31): "))                #Es la unica manera que se me ocurrio
        if dia >= 1 and dia <= 31:
            fecha = mes * 100 + dia
            if emisferio == 'N':
                if fecha >= 1221 or fecha <= 320:
                    print("Invierno")
                elif fecha >= 321 and fecha <= 620:
                    print("Primavera")
                elif fecha >= 621 and fecha <= 920:
                    print("Verano")
                elif fecha >= 921 and fecha <= 1220:
                    print("otoño")
            if emisferio == 'S':
                if fecha >= 1221 or fecha <= 320:
                    print("Verano")
                elif fecha >= 321 and fecha <= 620:
                    print("Otoño")
                elif fecha >= 621 and fecha <= 920:
                    print("Invierno")
                elif fecha >= 921 and fecha <= 1220:
                    print("Primavera")  