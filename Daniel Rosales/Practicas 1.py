#NUMEROS
#1. Encuentra el area de un circulo
radio= 1.1
pi= 3.1416
formula= pi*(radio*radio)

#2. Devuelve el valor absoluto

#3. Calculador de propinas
subtotal= 44.50
propina=.10
propinaTotal=44.50*.10
total=subtotal+propinaTotal

#4. Calcular peso en otro planeta
peso=70
gravedadTierra=9.78
gravedadMarte=3.72
formulaDespejadaMasa=peso/gravedadTierra
pesoMarte=formulaDespejadaMasa*gravedadMarte

#S T R I N G S
#1. Multiplicar una palabra
palabra= "hola"
multPalabra= palabra * 100
#print(multPalabra)

#2. Crear un mensaje con distintas variables
nombre= "Daniel"
apellidos= "Rosales Cortés"
gustos="escuchar musica y ver videos en youtube"
estancia="me la paso toda la tarde en mi casa"
#print("Mi nombre es", nombre, apellidos,",", "me gusta", gustos,",", "siempre", estancia)

#3. Obtener una letra en un string
string="abcdefghijk"
#print(string.count("h"))

#4. Transformar una string a mayusculas
stringMay= "hola soy daniel y me gusta mucho programar"
#print(stringMay.upper())

#5. Transformar una string a minusculas
strinMin="HOLA SOY DANIEL Y ME GUSTAN LAS PELICULAS DE SUPERHEROES"
#print(strinMin.lower())

#6. Obtener la ultima letra de un string
firstnlast= "Hola mundo"
#print(len(firstnlast))
#print(firstnlast[0])
#print(firstnlast[9])

#7. Invertir un nombre
nombre1= "Daniel"
apellido1= "Rosales"
nombrecompleto= [nombre1+apellido1]

#8. Formar una frase
str1="jfjdHvbcxyz"
str2 = "ofjvcv!ldba"
str3 = "mgbunfbd "
frase1=str1[4]+str2[0]+str2[7]+str2[10]
frase2=str3[0]+str3[3]+str3[4]+str3[7]+str2[0]+str2[6]
#print(frase1,frase2)

#9. Encontrar la cantidad de ocurrencias de la letra A
lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin pretium nisl nec ullamcorper dignissim. Aliquam facilisis efficitur turpis at sagittis. Suspendisse sed tristique augue, luctus sagittis urna. Ut nec porttitor tellus, vel feugiat ipsum. Nam maximus faucibus ipsum id ullamcorper. Duis leo ligula, congue sed blandit a, dictum nec metus. Duis lobortis libero eu convallis placerat. Donec felis lacus, faucibus sed massa non, tincidunt hendrerit odio. Ut efficitur sapien in nibh elementum bibendum. Phasellus vulputate tempor pretium. Proin viverra ante eu mi commodo rhoncus. Nullam vulputate tempus gravida. Fusce auctor massa eu suscipit porta. Aenean non elit convallis lacus eleifend lacinia non ac tortor. Nam efficitur dolor ac dolor fringilla venenatis. Fusce nec eros dictum, congue massa a, ornare nibh. Sed id tristique magna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nam sit amet ligula ac dui viverra vestibulum. Nunc faucibus cursus felis, et lacinia ex lobortis non. Vestibulum lobortis vel ligula vitae mattis. In sed velit sed purus imperdiet elementum et et tellus. Morbi ut metus sed urna dictum porttitor nec non tortor. Proin luctus massa laoreet lectus lacinia congue. Donec consectetur sollicitudin sollicitudin. Sed nec efficitur eros, eget semper ligula. Suspendisse sodales risus ex, id blandit elit tincidunt id. Proin vestibulum posuere enim, sed molestie nibh dapibus sed. Curabitur feugiat nibh non leo eleifend, non tempor lorem semper. Curabitur auctor ligula id velit lacinia, sit amet blandit augue eleifend. Donec ut tortor dui. Etiam maximus velit sed aliquet pretium. Suspendisse purus nibh, ultricies nec velit in, malesuada scelerisque est. Etiam pharetra dolor facilisis, porttitor felis sit amet, lobortis orci. Quisque massa elit, aliquet et aliquam non, egestas quis neque. Sed pulvinar lacus in tellus pretium, sit amet vestibulum felis malesuada. Proin porta libero mauris, id porttitor velit consequat sed. Suspendisse potenti. Suspendisse dapibus ligula non nibh mattis vestibulum. Aliquam erat volutpat. Aliquam rutrum ex dictum nunc ullamcorper, ac mollis tortor feugiat. Aenean a nunc bibendum, porttitor dolor in, pulvinar lorem. Interdum et malesuada fames ac ante ipsum primis in faucibus. Cras tempus elementum ipsum, vitae porta metus elementum quis. Proin et convallis risus. Vestibulum fringilla lectus id velit mattis sodales. Donec viverra ligula id malesuada commodo. Pellentesque ac dignissim mauris. Curabitur ut nunc vitae dolor pharetra iaculis in sit amet justo."
#print(lorem_ipsum.count("a"))

#10. Separar una lista por comas
lista_de_compras = ["Manzanas,zanahorias,cereal,leche,ramen"]
#print(lista_de_compras)

#I M P R E S I O N  E N  P A N T A L L A
#1. Imprimir un nombre}
minombre= "Daniel"
miapellido="Rosales"
#print(minombre, miapellido)

#2. Imprime las siguientes strings separadas por comas
listacompras= "Manzanas", "zanahorias", "cereal", "leche", "ramen"
#print(listacompras)

#L I S T A S
#1 . Lista con 100 elementos
bfr= ["BFR"]
bfr.append("BFR,"*99)
#print(bfr)

#2, Lista a String
listaLorem = ['L', 'o', 'r', 'e', 'm', ' ', 'i', 'p', 's', 'u', 'm', ' ', 'd', 'o', 'l', 'o', 'r', ' ', 's', 'i', 't', ' ', 'a', 'm', 'e', 't', ',', ' ', 'c', 'o', 'n', 's', 'e', 'c', 't', 'e', 't', 'u', 'r', ' ', 'a', 'd', 'i', 'p', 'i', 's', 'c', 'i', 'n', 'g', ' ', 'e', 'l', 'i', 't', '.', ' ', 'P', 'r', 'o', 'i', 'n', ' ', 'p', 'r', 'e', 't', 'i', 'u', 'm', ' ', 'n', 'i', 's', 'l', ' ', 'n', 'e', 'c', ' ', 'u', 'l', 'l', 'a', 'm', 'c', 'o', 'r', 'p', 'e', 'r', ' ', 'd', 'i', 'g', 'n', 'i', 's', 's', 'i', 'm', '.', ' ', 'A', 'l', 'i', 'q', 'u', 'a', 'm', ' ', 'f', 'a', 'c', 'i', 'l', 'i', 's', 'i', 's', ' ', 'e', 'f', 'f', 'i', 'c', 'i', 't', 'u', 'r', ' ', 't', 'u', 'r', 'p', 'i', 's', ' ', 'a', 't', ' ', 's', 'a', 'g', 'i', 't', 't', 'i', 's']
#print("".join(listaLorem))

#3. Mis canciones favoritas
listaCanciones=["Violet","Summertime"]
listaCanciones.append("Never gonna give you up")
#print(listaCanciones)

#4.Crear una lista con lista dentro
fRase1="of course "
fRase2="i still "
fRase3="love "
fRase4="you"

print(fRase1.split(","))
frasecompleta=fRase1+fRase2+fRase3+fRase4
print(frasecompleta)



#4. Crear una lista con elemmentos dentro
