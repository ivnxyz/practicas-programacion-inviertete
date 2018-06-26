print =("")
print =("")
print =("")

intentos = 3
contador = 1
while contador <=3:
    with open('usuarios.txt') as user:
        nombres = user.readlines()
    usuario = {}
    passw = {}
    print("intentos",contador,"de",intentos)
    nombre =(input("usuario"))
    contraseña =(input("contraseña"))
    contador += 1
    for u in nombres:
        u.strip().split("|")
        usuario.append(u)
        
        