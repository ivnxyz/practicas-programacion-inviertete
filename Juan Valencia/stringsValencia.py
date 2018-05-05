#1. Crea un progama que imprima 100 veces una palabra
palabra= "juan"
print(palabra*100)
#2. Crea un programa que tenga variables como verbos, adjetivos y nombres con los que genere un mensaje.
saludo= "me llamo:"
nombreCompleto= "Juan Emmanuel Valencia Toledo."
gusto1= " tocar la guitarra,"
gusto2= "jugar futbol"
gusto3= "y escuchar música."
despedida="Los veo luego, adiós"
print("hola", saludo, nombreCompleto, "Y me gusta", gusto1, gusto2, gusto3, despedida)

#3. Obtén una letra en un índice.
letra= "gfytfjfytdt"
print(letra[3])

#4.Transforma una String a mayúsculas.
letra2= "hola como estas"
print(letra2.upper())

#5. Transforma una String a minúsculas.
letra3= "HOLA COMO ESTAS"
print(letra3.lower())

#6. Obtén la primera y última letra de un String incluso si su tamaño cambia.
str= "Hola_como_estassssssssssss"
print(str[0],str[14])

#7.Escribe un programa que contenga tu nombre y apellido y los imprima al revés con un espacio en medio
nombre= "Juan Emmanuel"
apellido= "Valencia"
print(apellido ,nombre)

#8. Forma la frase "Hola mundo!" con las siguientes Strings.Sólo usa las Strings disponibles.Agrega los espacios correctamente.
str1 = "jfjdHvbcxyz"
str2 = "ofjvcv!ldba"
str3 = "mgbunfbd "
print(str1[4],str2[0],str2[7],str2[10],"","",str3[0],str3[3],str3[4],str3[7],str2[0],str2[6])

#9. Encuentra cuántas veces aparece la letra 'a' en la siguiente String.
lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin pretium nisl nec ullamcorper dignissim. Aliquam facilisis efficitur turpis at sagittis. Suspendisse sed tristique augue, luctus sagittis urna. Ut nec porttitor tellus, vel feugiat ipsum. Nam maximus faucibus ipsum id ullamcorper. Duis leo ligula, congue sed blandit a, dictum nec metus. Duis lobortis libero eu convallis placerat. Donec felis lacus, faucibus sed massa non, tincidunt hendrerit odio. Ut efficitur sapien in nibh elementum bibendum. Phasellus vulputate tempor pretium. Proin viverra ante eu mi commodo rhoncus. Nullam vulputate tempus gravida. Fusce auctor massa eu suscipit porta. Aenean non elit convallis lacus eleifend lacinia non ac tortor. Nam efficitur dolor ac dolor fringilla venenatis. Fusce nec eros dictum, congue massa a, ornare nibh. Sed id tristique magna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nam sit amet ligula ac dui viverra vestibulum. Nunc faucibus cursus felis, et lacinia ex lobortis non. Vestibulum lobortis vel ligula vitae mattis. In sed velit sed purus imperdiet elementum et et tellus. Morbi ut metus sed urna dictum porttitor nec non tortor. Proin luctus massa laoreet lectus lacinia congue. Donec consectetur sollicitudin sollicitudin. Sed nec efficitur eros, eget semper ligula. Suspendisse sodales risus ex, id blandit elit tincidunt id. Proin vestibulum posuere enim, sed molestie nibh dapibus sed. Curabitur feugiat nibh non leo eleifend, non tempor lorem semper. Curabitur auctor ligula id velit lacinia, sit amet blandit augue eleifend. Donec ut tortor dui. Etiam maximus velit sed aliquet pretium. Suspendisse purus nibh, ultricies nec velit in, malesuada scelerisque est. Etiam pharetra dolor facilisis, porttitor felis sit amet, lobortis orci. Quisque massa elit, aliquet et aliquam non, egestas quis neque. Sed pulvinar lacus in tellus pretium, sit amet vestibulum felis malesuada. Proin porta libero mauris, id porttitor velit consequat sed. Suspendisse potenti. Suspendisse dapibus ligula non nibh mattis vestibulum. Aliquam erat volutpat. Aliquam rutrum ex dictum nunc ullamcorper, ac mollis tortor feugiat. Aenean a nunc bibendum, porttitor dolor in, pulvinar lorem. Interdum et malesuada fames ac ante ipsum primis in faucibus. Cras tempus elementum ipsum, vitae porta metus elementum quis. Proin et convallis risus. Vestibulum fringilla lectus id velit mattis sodales. Donec viverra ligula id malesuada commodo. Pellentesque ac dignissim mauris. Curabitur ut nunc vitae dolor pharetra iaculis in sit amet justo."
lorem_ipsum.count("a")
contar=lorem_ipsum.count("a")
print(contar)

#10.Separa la siguiente String por comas.
lista_de_compras = "Manzanas,zanahorias,cereal,leche,ramen"
print(lista_de_compras.split(","))

#11.Imprime tu nombre completo con un espacio.
apellido="Valencia Toledo"
nombres="Juan Emmanuel"
print(apellido, " ", nombres)

#12.Imprime la siguientes Strings separadas por comas.
ramen = "Manzanas,", "zanahorias,", "cereal,", "leche,", "ramen"
print(ramen)

#13.Escribe un programa que cree una lista con 100 elementos.
lo=["cd,"*100]
print(lo)

#14.Inserta todos los elementos de una lista en una String.
lista = ["H","o","l","a",", ", "m","e"," ","ll","a","m","o"," ","J","u","a","n"," ","E","m","m","a","n","u","e","l"," ","V","a""l","e","n","c","i","a",".","Y"," ","t","e","n","g","o"," ","1","5"," ","a","ñ","o","s"]
print(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7],lista[8],lista[9],lista[10],lista[11],lista[12],lista[13],lista[14],lista[15],lista[16],lista[17],lista[18],lista[19],lista[20],lista[21],lista[22],lista[23],lista[24],lista[25],lista[26],lista[27],lista[28],lista[29],lista[30],lista[31],lista[32],lista[33],lista[34],lista[35],lista[36],lista[37],lista[38],lista[39],lista[40],lista[41],lista[42],lista[43],lista[44],lista[45],lista[46],lista[47],lista[48],lista[49])

