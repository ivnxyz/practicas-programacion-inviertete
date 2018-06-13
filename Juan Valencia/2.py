frase = input("")
pal = frase.replace(" ", "")
if pal == pal[::-1]:
    print("La frase que ingresaste SÍ es un palíndromo.")
else:
    print("La frase que ingresaste NO es un palíndromo.")