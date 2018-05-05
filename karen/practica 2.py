#recrea un programa que calcule tu peso en otro planeta y guadalo en una variable
gravedad_en_planeta_elegido={"luna":1.62,"mercurio":2.78 ,"venus":8.87,"marte":3.72,"jupiter":22.88,"saturno":9.05,"urano":7.77,"neptuno":11}
peso_usuario= input("dame tu peso")
nombre_usuario= input("como te llamas?")
planeta:usuario=input("en que planeta te gustaria saber tu peso?"[])
gravedad_de_la_tierra=9.81
masa=peso_usuario/gravedad_de_la_tierra
peso_en_otro_planeta= masa * gravedad_en_planeta_elegido["luna"]
print(peso_en_otro_planeta)
#agregar la intrseccion con python en los usuarios

#imprimir el mensaje
print("hola", nombre,"tu peso en el planeta:", planeta_usuario,"es de",peso_usuario= input("dame tu peso:"))