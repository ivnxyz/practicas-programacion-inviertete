#:escribe un programaque cree una lista con 100 elementos
elemento=["ABC"]
print(elemento*100)

#.inserta todos los elementos de una lista en una strings
lista=["h", "o", "l", "a"]
s = " ".join(lista)
print(s)

#.agrega un elemento a una lista
cancion_favorita1="un_angel_como_el_sol_tu_eres"
cancion_favorita2="demons"
cancion_favorita3="it_will_rain"
canciones = [cancion_favorita1, cancion_favorita2, cancion_favorita3]
canciones.append("Never Gonna Give You Up")
print(canciones)

# Crea una lista con listas dentro.
frase1 = "of course"
frase2 = "i still"
frase3 = "love"
frase4 = "you"
frases = [frase1, frase2, [frase3, [frase4]]]
print(frases)

# Agrega un elemento a la lista sin usar append.()
comidaFavorita1 = "polloRelleno"
comidaFavorita2 = "lasagna"
comidaFavorita3 = "tacos"
comidaFavorita4 = "pizza"
comidasFavoritas = [comidaFavorita1, comidaFavorita2, comidaFavorita3, comidaFavorita4]
comidasFavoritas += ["Sushi"]
print(comidasFavoritas)

# Agrega una lista a otra lista con una función
artistaFavorito1 = "Bruno Mars"
artistaFavorito2 = "Eros Ramazzotti"
artistaFavorito3 = "The weeknd"
artistasFavoritos = [artistaFavorito1, artistaFavorito2, artistaFavorito3]
paísFavorito1 = "Italia"
paísFavorito2 = "Francia"
paísesFavoritos = [paísFavorito1, paísFavorito2]
artistasFavoritos.append(paísesFavoritos)
print(artistasFavoritos)


       