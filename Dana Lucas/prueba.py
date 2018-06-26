frase = input("Ingrese una frase:")
palíndromo = frase.lower()
temp = palíndromo.replace(' ','')

if temp == temp[::-1]:
    print("La frase que ingresaste SÍ es un palíndromo") 
else:
    print("La frase que ingresaste NO es un palíndromo")


