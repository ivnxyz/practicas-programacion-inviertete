import random
# PRIMERA PARTE
# Crea cuantas variables quieras de tipo strig y asigna el nombre de un amigo tuyo a cada variable.
amigo1="Forti"
amigo2="Maed"
amigo3="Hugo"
amigo4="Alexis"
amigo5="Amaury"

# Inserta o adjunta estas variabres en una nueva lista que se llame amigos.
amigos=([amigo1, amigo2, amigo3, amigo4, amigo5] )
print("1._ Amigos:", amigos)

# Imprime un mensaje que indeique al usuario cuatos elemtos comntiene la lista amigos.
print("2._ Numero de amigos:", len(amigos))

# Imprime el primer elemento de la lista de amigos todo en mayusculas, utilizando sunciones de strings de python.
print("3._ Nombre en Mayusculas:",[amigo1.upper()])

# Almacena en una variable el valor del tercer caracter del segundo elmento de tu lista de amigos.
print("4._ Tercer caracter:", [amigos[1][2]])

# Crea una lista que contenga cinco numeros aleatorios.
lista=[random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)]
print("5._ Numeros aleatorios:",lista)

# En una sola linea de codigo imprime el resultado de la suma de estos cinco numeros.
print("6._ Suma:", [lista[0]+lista[1]+lista[2]+lista[3]+lista[4]])

# Agrega tres numeros nuevos a la lista de numeros.
lista.append(1)
lista.append(2)
lista.append(3)
print('7._ Agrega numeros:', lista)

# En una sola linea de codigo imprime el resultado de la multiplicacio de estos cinco numeros.
print("8._ Multiplicacion:", [lista[0]*lista[1]*lista[2]*lista[3]*lista[4]*lista[5]*lista[6]*lista[7]])

# Utilizando esta misma lista de numeros, esperimenta con las funciones sort(), reverse(), pop() y count(). En algunos casos tendras que pasar parametros de las funciones, si tienes dudas busca soluciones en internet
lista.sort()
print('sort:', lista)

lista.reverse()
print('reverse:', lista)

# (POP) en esta funcion nos extrae un numero pero sin parametro extrae el ultimo
lista.pop()
print('popsp:', lista)
# Ahora con un parametro
print('pop:',lista.pop(3) )
  
# (COUNT)
# para esta funcion agregaremos numeros para que nos arroje resultado
lista.append(1)
lista.append(1)
lista.append(12)
lista.append(20)
lista.append(1)
print('Nueva lista:',lista)

print('count:',lista.count(1))

# SEGUNDA PARTE
# Crea un diccionario que contenga nombres de paises como llave y capitales de los paises como valor.
paises= {"México":"CDMX", "Perú":"Lima", "Colombia":"Bogotá", "Cuba":"La Habana", "Argentina":"Buenos Aires"}
print('14._ Paises:',paises)
        
# Imprime un enunciado que lea "LA CAPITAL DE X ES Y" donde x es la llave de tu diccionario y Y su valor. hazlo para tres valores de tu diccionario.
enp= "La capital de Perú es: "
print(enp+ paises["Perú"])
enm= "La capital de México es: "
print(enm+ paises["México"])
ena= "La capital de Argentina es: "
print(ena+ paises["Argentina"])

# Crea un diccionario que contenga nombres de estados de Mexico como llave y capitales de los estados como valor. minimo 5
estados={'Oaxaca':'Oaxaca', 'Veracruz':"Jalapa", "Jalisco":"Guadalajara", "México": "Toluca", "Quintana Roo":"Chetumal", "Campeche":"Campeche"}
print('15._ Estados de la republica:',estados)

# Crea un diccionario con nombre diccionarios" que tenga por llave un numero entero y por valor cada uno de los dos diccionarios creados en los incisos anteriores
diccionarios= {1:paises, 2: estados}
print('16._ Diccionarios:',diccionarios)

# Imprime todos los valores del diccionario "diccionarios" como lo iciste en el punto 2
print("La capital de Perú es", diccionarios[1]["Perú"])
print("La capital de México es", diccionarios[1]["México"])
print("La capital de Argentina es", diccionarios[1]["Argentina"])
print("La capital de Colombia es", diccionarios[1]["Colombia"])
print("La capital de Cuba es", diccionarios[1]["Cuba"])

print("La capital de Oaxaca es", diccionarios[2]["Oaxaca"])
print("La capital de Jalisco es", diccionarios[2]["Jalisco"])
print("La capital de Quintana Roo es", diccionarios[2]["Quintana Roo"])


