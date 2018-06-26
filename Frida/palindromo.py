palabra=input("")
pal= palabra.replace(' ', '')
pal=pal.lower()
palindromo= pal[::-1]
if pal == palindromo:
    print("La frase que ingresaste SÍ es un palíndromo.")
else:
    print("La frase que ingresaste NO es un palíndromo.")
    