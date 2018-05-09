#sección 1
#1.nombre de mis amigos
amigo1="Angel"
amigo2="Keyla"
amigo3="Jonathan"

#2.inserta estas variables a una nueva lista que se llame "amigos"
amigos=[]
amigos.append(amigo1)
amigos.append(amigo2)
amigos.append(amigo3)

#3.imprimir un mensaje que indique cuantos elementos contiene la lista de amigos
print("la lista de amigos tiene",len(amigos),"elementos")

#4. imprime el primer elemento de la lista de amigos
print(amigos[0].upper())

#5. almacena en una variable el valor del tercer caracter del segundo elemento de tu lista de amigos
variable=amigos[1][2]
print("el tercer caracter es la letra",variable)

#6. crea una lista que contenga 5 números aleatorios
numeros=[1,4,7,9,3]

#7. en una sola linea de codigo,imprime el resultado de la suma de estos 5 números
suma_numeros=(1+4+7+9+3)
print(suma_numeros)

#8. agrega tres números nuevos a la lista de números
numeros.append(2)
numeros.append(5)
numeros.append(6)
print(numeros)

#9. en una sola linea de codigo imprime el resultado de la multiplicacion de estos 5 numeros
multiplicacion=(1*4*7*9*3)
print(multiplicacion)

#10. utilizando esta misma lista de números, experimenta con las funciones sort(), reverse(), pop() y count().
numeros.sort()
print(numeros)
numeros.reverse()
print(numeros)
numeros.pop()
print(numeros)
numeros.count(7)
print(numeros)
repeticiones=numeros.count(7)
print("el número 7 se repite",repeticiones,"veces")

#sección 2
#1. crea un diccionario que contenga nombres de paises como llave y capitales de los paises como valor.
paises={"Argentina":"Buenos_Aires","Canadá":"Otawwa","China":"Pekín","México":"México_Distrito_Federal","Italia":"Roma"}
            
#2. imprime un enunciado que lea "la capital de x es y"
print("la capital de Italia es",paises["Italia"])
print("la capital de China es",paises["China"])
print("la capital de Canadá es",paises["Canadá"])

#3. crea un diccionario que contenga nombres de estados de mexico como ,llave y capitales de los estados como valor.
estados={"Michoacán":"Morelia","Chiapas":"Tuxtla_Gutiérrez","Jalisco":"Guadalajara","Yucatán":"Mérida","Veracruz":"Xalapa_Enríquez"}

#4. crea un diccionario con nombre "diccionarios"que tenga por llave un número entero y por valor cada uno de los diccionarios creados en los incisos anteriores
diccionarios={1:paises,2:estados}
print(diccionarios)

#5. imprime todos los valores del diccionario.
print("la capital de Argentina es",paises["Argentina"])
print("la capital de Canadá es",paises["Canadá"])
print("la capital de China es",paises["China"])
print("la capital de México es",paises["México"])
print("la capital de Italia es",paises["Italia"])
print("la capital de Michoacán es",estados["Michoacán"])
print("la capital de Chiapas es",estados["Chiapas"])
print("la capital de Jalisco es",estados["Jalisco"])
print("la capital de Yucatán es",estados["Yucatán"])
print("la capital de Veracruz es",estados["Veracruz"])

      

      


