print("**********BIENVENIDOS**********")
print("**** Inicio de sesión****")

with open("usuarios.txt") as usuarios:
    usuarios = usuarios.readlines()
    diccionarioA = {}
    diccionarioB = {}
    lista=[]
    lista2=[]
    print("intento 0 de 3")
    u=input("Usuario: ")
    contador=1
    
for usuario in usuarios:
    diccionarioA[contador]=usuario.split('|')[1].strip()
    diccionarioB[contador]=usuario.split('|')[0]
    contador+=1

usu=diccionarioB.values()
contra=diccionarioA.values()


contador = 0
for u2 in usu:
    lista.append(u2)
    contador += 1
contador = 0
for c2 in contra:
    lista2.append(c2)
    contador += 1

intentos = 0
while intentos < 3: 
    if u in lista:
        c=input("Contraseña: ")
        valor=lista.index(u)
        if c == lista2[valor]:
            with open("peliculas.txt") as peliculas:
                peliculas = peliculas.readlines()
                peli=1
            for pelicula in peliculas:
                print(peli,'.',pelicula)
                peli+=1
        else:
            intentos += 1
            print("Contraseña equivocada")
            c=input("Contraseña: ")
    else:
        intentos += 1
        print ("intento", intentos,"de 3")
        if intentos < 3:
            u=input("Usuario: ")
        else:
            exit()
        

        


           
    
