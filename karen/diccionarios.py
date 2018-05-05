#crear un dicionario de capitales y paises min.5
paises={"austria":"viena","brasil":"brasilia","bolivia":"sucre","camerun":"yaundé","buntán":"thimphu"}
#escribe un enunciado donde lea "la capital x es y"
print("la capital de austria es",paises["austria"])
print("la capital de brasil es",paises["brasil"])
print("la capital de bolivia es",paises["bolivia"])
#crea un diccionario de estados y capitales de mexico min.5
Mexico={"aguascalientes":"aguascalientes","nuevo leon":"monterrey","morelos":"cuernavaca","nayarit":"tepic","yucatan":"merida"}
#crea un diccionario con nombre diccionarios que tenga por llave un numero entero y por valor cada uno de los diccionario creados anteriormente
diccionarios={1:paises,2:Mexico}
#imprimir todos los valore de "diccionarios"
print("la capital de austria es", diccionarios[1]["austria"])
print("la capital de brasil es", diccionarios[1]["brasil"])
print("la capital de bolivia es", diccionarios[1]["bolivia"])
print("la capital de camerun es", diccionarios[1]["camerun"])
print("la capital de buntán es", diccionarios[1]["buntán"])

print("la capital de aguascalientes es",diccionarios[2]["aguascalientes"])
print("la capital de nuevo leon es",diccionarios[2]["nuevo leon"])
print("la capital de morelos es",diccionarios[2]["morelos"])
print("la capital de nayarit es",diccionarios[2]["nayarit"])
print("la capital de yucatan es",diccionarios[2]["yucatan"])



