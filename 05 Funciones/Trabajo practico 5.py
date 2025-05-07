##1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
lista = list(range(4, 101, 4))
print(lista)

##2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. 
#¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
lista = [1, 2, 3, 4, 5]
print("el peunltimo elemento es:", lista[3])

##3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.
lista = []
lista.append("queso")
lista.append("tapete")
lista.append("cereal")
print(lista)

##4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
#respectivamente. Imprimir la lista resultante por pantalla.
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[3] = "oso"
print(animales)

##5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
#lo que hace este codigo es eliminar el numero mas grande de la lista, en este caso el 22.

##6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
#pantalla los dos primeros.
lista = list(range(10, 31, 5))
print("los dos primeros elementos son:", lista[0], "y", lista[1])

##Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualquiera.
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = 505
autos[2] = 408
print(autos)

##8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. 
#Imprimir la lista resultante por pantalla.
dobles = [ ]
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

##9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
    #a) Agregar "jugo" a la lista del tercer cliente usando append.
    #b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
    #c) Eliminar "pan" de la lista del primer cliente.
    #d) Imprimir la lista resultante por pantalla
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
#a) 
compras[2].append("jugo") #agrego jugo a la lista del cliente 3
#b)
compras[1][1] = "tallarines" #cambio los fideos por tallarines en el cliente 2
#c)
compras[0].remove("pan") #saco el pan de la lista del cliente 1
#d)
print(compras)

##10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
    #● Posición lista_anidada[0]: 15
    #● Posición lista_anidada[1]: True
    #● Posición lista_anidada[2][0]: 25.5
    #● Posición lista_anidada[2][1]: 57.9
    #● Posición lista_anidada[2][2]: 30.6
    #● Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla.
lista_anidada = [15, True, [25.5, 57.9, 30.6], [False]]
print(lista_anidada)