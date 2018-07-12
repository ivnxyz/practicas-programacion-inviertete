FRASE = input("Ingrese una frase:")
PALÍNDROMO = FRASE.lower()
PALÍNDROMO = FRASE.upper()
temp = PALÍNDROMO.replace('','')

if temp == temp[::-1]:
    print("La frase que ingresaste SÍ es un palíndromo") 
else:
    print("La frase que ingresaste NO es un palíndromo")

