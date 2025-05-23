##1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y 
# mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1) 
#programa principal
num = int(input("ingrese un numero: "))
for i in range(1, num + 1):
    print(f"!{i} = {factorial(i)}")

##2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.
def fibonacci(n): 
    if n == 0 or n == 1: 
        return n 
    else: 
        return fibonacci(n - 1) + fibonacci(n - 2)  
#programa principal
num = int(input("Ingrese un numero: "))
print(f"valor fibonacci: {fibonacci(num)}")
for i in range(1, num + 1):
    print(fibonacci(i), end = " ")

##3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛
# 𝑚 = 𝑛 ∗ 𝑛 (𝑚−1) . Prueba esta función en un algoritmo general.
def potencia(n, e):
    if e == 0:
        return 1
    else:
        return  n * potencia(n, e - 1)
#programa principal
num = int(input("Ingrese un numero: "))
exp = int(input("Ingrese un otro numero: "))
print(potencia(num, exp))

##4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva 
# su representación en binario como una cadena de texto.
def dec_a_bin(n):
    if n == 0:
        return "0"
    elif n == 1: 
        return "1" 
    else:
        return dec_a_bin(n // 2) + str(n % 2)
#programa principal
num = int(input("Ingrese un numero: "))
print(f"el {num} en binario es: {dec_a_bin(num)}")

##5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto 
# sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1: -1])
#programa principal
cadena = input("ingrese una palabra (sin espacios ni tildes): ").lower()
print(es_palindromo(cadena))

##6)Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero
# positivo y devuelva la suma de todos sus dígitos.
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)
#programa principal
num = int(input("Ingrese un número entero positivo: "))
if num < 0:
    print("Debe ser un número positivo.")
else:
    resultado = suma_digitos(num)
    print(f"La suma de los dígitos de {num} es: {resultado}")

##7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, 
# en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con 
# un solo bloque. Escribí una función recursiva contar_bloques(n) que reciba el número de bloques 
# en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        for i in range(n, 0, -1):
            return n + contar_bloques(n - 1)
#programa principal
num = int(input("Ingrese un numero: "))
print(f"Se necesitan {contar_bloques(num)} bloques")

##8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo 
# (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.
def contar_digito(numero, digito):
    if numero == "":
        return 0
    elif numero[0] == digito:
        return 1 + contar_digito(numero[1:], digito)
    else:
        return contar_digito(numero[1:], digito)
# Programa principal
num = input("Ingrese un número: ")
dig = input("Ingrese un dígito: ")
print(f"Aparece {contar_digito(num, dig)} veces")