## 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(0, 101):
    print(i)

##2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
#Declaramos las variables y pedimos datos
num = int(input("Ingrese un numero entero: "))
num1 = 0
cont = 0
#condicional por si el numero es 1
if num == 1:
    cont += 1
#Bucle while que cuenta los digitos
while num > 1:
    num1 = num / 10
    num = num1
    cont += 1
#Imprimimos los resultados (cantidad de digitos)
print("El numero ingresado tiene ", cont, "digitos")

##3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores
#Declaramos las variables
num1 = int(input("Ingrese un numero entero: "))
num2 = int(input("Ingrese otro entero: "))
suma = 0
#Si los numeros son distintos
if num1 != num2:
    # Encontramos los extremos correctamente
    menor = min(num1, num2)
    mayor = max(num1, num2)
    #Realizamos la suma de los numeros 
    for x in range(menor + 1, mayor):
        suma += x
#si los numeros son iguales
else:
    print("No hay numeros entre", num1, "y", num2)
#Imprimimos el resultado
print("La suma de todos los numeros entre ", num1, " y ", num2, " es: ", suma)

##4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
#Declaramos las variables
num = 1     #Le ponemmos como valor inicial 1 para que pueda entrar al bucle
suma = 0
#mientras el numero no sea cero 
while num != 0:
    #Pide un numeros y los suma 
    num = int(input("Ingrese un numero: "))
    suma = suma + num
#Imprime el resultado
print("La suma de todos esos numeros es: ", suma)    
    
##5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random  
#Asignamos las variables
num = random.randint(0, 9) ##Para generar n entero random se escribe la instruccion sai, sin corchetes. con corchetes es para una lista
cont = 0
num1 = -1
#Comparamos el numero ingresado con el numero a adivinar
while num1 != num:
    num1 = int(input("Ingrese un numero entre el 0 y el 9: "))
#Por cada intento sumamos 1 al contador
    cont += 1    
#Imprimimos el resultado
print("Te tomó ", cont, " intentos adivinar")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
#aprovechamos que podemos usar el paso -2 para hacerlo mas sencillo
for i in range(100, -1, -2):
    print(i)
print("/////////////////////////")
#Aca esta hecho con division por 2
for x in range(100, -1, -1):
    if x % 2 == 0:
        print(x)

##7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
#Declaramos las variables
suma = 0
suma2 = 0
num = int(input("ingrese un numero entero positivo: "))
#Hacemos la suma de todos los numeros entre cero y el ingresado por el usuario incluyendo este ultimo
for i in range(0, num + 1):
    suma = suma + i
    print(suma)
print("///////////////////////////")
#bucle por si no se quiere incluir el numero ingresado
for i in range(0, num):
    suma2 = suma2 + i
    print(suma2)
    
#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, 
# cuántos son impares, cuántos son negativos y cuántos son positivos.
#Declaramos las variables
par = 0
impar = 0
negativo = 0
positivo = 0
#Bucle para que el usuario ingrese los numeros
for x in range(1, 101):
    num = int(input("ingrese un numero entero: "))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
    if num < 0:
        negativo += 1
    elif num == 0:
        print("El cero es un elemento neutro")
    else:
        positivo += 1
#imprimimos los resultados
print(f"par: {par}, impar: {impar}, positivo: {positivo}, negativo: {negativo}")

##9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores
#Declaramos las variables
suma = 0
#bucle para que el usuario ingrese los cien numeros
for x in range(1, 101):
    num = int(input("ingrese un numero entero: "))
    suma = suma + x
#Calculamos e imprimimos la media
promedio = suma / 10
print("El promedio de los numeros ingresados es: ", promedio)

##10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario
#Creamos las variables
num2 = input("ingrese un numero: ") #Almacenamos el dato como str para que nos sea mas facil darlo vuelta
num = int(num2)                     #y aca en otra variable lo convertimos a int para calcular las cifras
cont = 0
limon = ""                          #para almacenar y sumar cada caracter
#Bucle while para contar cuantos digitos tiene el numero
while num > 1:
    num1 = num / 10
    num = num1
    cont += 1
#Con este bucle for, recorremos num2, la cadena que ingreso el usuario de izq. a der
for x in range(cont -1, -1, -1):
   limon += num2[x]                 #Aca almacenamos cada caracter

limon = int(limon)                  #aca convertimos el string a un int, por si necesitamos sumar el numero invertido
print(limon)                        #imprimimos el resultado en pantalla