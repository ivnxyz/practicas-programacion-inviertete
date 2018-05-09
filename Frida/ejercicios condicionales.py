nombre = input("como te llamas?")
sexo = input("cual es tu sexo?")
añoDeNacimiento = int(input("en que año naciste?"))

if añoDeNacimiento <= 2000:  
    print("puedes votar")
else:
    print("no puedes votar")