##1. Crear una función llamada imprimir_hola_mundo que imprima porpantalla el mensaje: “Hola Mundo!”. 
# Llamar a esta función desde el programa principal.
def imprimir_hola_mundo():
    print("Hola Mundo!")
#programa principal
imprimir_hola_mundo()

##2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.
def saludar_usuario(a):
    print(f"Hola {nombre}!")
#programa principal
nombre = input("ingrese su nombre: ")
saludar_usuario(nombre) 

##3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
def  informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
#programa principal
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

##4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados
def  calcular_area_circulo(a):
    area = 3.14 * (radio * radio)
    return area 
def calcular_perimetro_circulo(a):
    perimetro = 3.14 * radio * 2
    return perimetro
#programa principal
radio = int(input("Ingrese el radio del circulo: "))
print(f"area: {calcular_area_circulo(radio)}")
print(f"perimetro: {calcular_perimetro_circulo(radio)}")

##5 Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
def  segundos_a_horas(seg):
    horas = segundos / 3600
    return horas
#programa principal
segundos = int(input("Ingrese los segundos: "))
print(segundos_a_horas(segundos))

##6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.
def  tabla_multiplicar(num):
    for i in range(1, 11):
        print(f"{numero} * {i} = {i * numero}")
#programa principal
numero = int(input("Ingrese un numero: "))
tabla_multiplicar(numero)

##7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de: 
# sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
def  operaciones_basicas(a, b):
    print(f"\nsuma: {a + b}\n")
    print(f"resta_1: {a - b}\n")
    print(f"resta_2: {b - a}\n")
    print(f"multiplicacion: {a * b}\n")
    print(f"division_1: {round(a / b, 2)}\n")
    print(f"division_2: {round(b / a, 2)}\n")
#programa principal
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
operaciones_basicas(num1, num2)

##8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva 
# el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
def  calcular_imc(p, a):
    IMC = peso / (altura ** 2)
    return IMC
#programa principal
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
print(f"IMC: {round(calcular_imc(peso, altura), 2)}")

##9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.
def  celsius_a_fahrenheit(C):
    fahrenheit = (temp * (9 / 5)) + 32
    return fahrenheit
#programa principal
temp = float(input("Ingrese la temperatura en grados Celsius: "))
print(f"{temp} grados celsius pasados a fahrenheit son {round(celsius_a_fahrenheit(temp), 2)}")

##10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta función.
def  calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio
#programa principal
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
num3 = int(input("Ingrese un ultimo numero: "))
print(f"el promedio entre {num1}, {num2} y {num3} es: {round(calcular_promedio(num1 , num2, num3), 2)}")