import random
print("*****BIENVENIDO AL ADIVINADOR******")
num=int(input("Indica el límite superior:"))
x=random.randint(1,num)
contador= 1
print("Jugando con números entre 1 y", num)
while contador <= num:
    a=(int(input("Dame un número:")))
    if a == x:
        print("Adivinaste en", contador, "intentos")
        break
    else:
        print("Vuelve a intentarlo")
    contador += 1
        
    
    


