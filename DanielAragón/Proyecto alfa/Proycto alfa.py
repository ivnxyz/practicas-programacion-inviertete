print("**********BIENVENIDOS**********")
print("**** Inicio de sesión****")

with open("usuarios.txt") as usuarios:
    usuarios = usuarios.readlines()
    diccionarioA = {}
    diccionarioB = {}
    print("intento 0 de 3")
    u=input("Usuario: ")
    contador=1
    
for usuario in usuarios:
    diccionarioA[contador]=usuario.split('|')[1].strip()
    diccionarioB[contador]=usuario.split('|')[0]
    contador+=1
    
usu=diccionarioB.values()
contra=diccionarioA.values()   
intentos = 0
for u2 in usu:
    if  u == u2:
        c=input("Contraseña: ")
        for c2 in contra:
            if c == c2:
                with open("peliculas.txt") as peliculas:
                    peliculas = peliculas.readlines()
                    peli=1
                for pelicula in peliculas:
                    print(peli,'.',pelicula)
                    peli+=1
            else:
                print("Usuario o contraseña erronea")
                intentos += 1
                print("intento ", intentos,"de 3")
print(usu)


           
    
