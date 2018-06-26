menu=int(input("elige un numero (1/2/3/4/5):"))
if menu == 2:
    lista= ["danna,william,carlos,daniela,fernanda"]
    for nombre in lista:
        print(nombre)
elif menu == 3:
    lista=range(1, 101)
    for numero in lista:
        if numero %2==0:
            print("es par")
        else:
            print("es impar")}
elif menu == 4:
    
