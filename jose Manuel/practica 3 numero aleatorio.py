#prototipo del juego ADIVINADOR
import random

print("**BIENVENIDO AL ADIVINADOR**")

limite = (int(input("por favor indica el limite superior: ")))
print("jugando con numeros entre 1 y", limite)

print("***********************************************")

num = random.randint(1,limite)
contador = 1
while contador <= limite :
    num1 = int(input("dame un numero entre 1 y el numero que me diste "))
    if num1 == num:
        print("adivinaste")
        break
    else:
        print("intentalo de nuevo")
    contador += 1
   