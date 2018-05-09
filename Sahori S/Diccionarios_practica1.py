inventario = {
    'oro' : 500,
    'bolsa' : ['mechero', 'hilo', 'gema'],
    'mochila' : ['xilófono','daga','pieza de pan']
  }

#Agrega una llave llamada ´bolsillo´al inventario
inventario["bolsillo"]=[]

#Haz que el valor de 'bolsillo' sea una lista que contanga las Strings 'fresa' y 'linterna'.
inventario["bolsillo"].append("fresa")
inventario["bolsillo"].append("linterna")

#Ordena los elementos de la lista en la llave 'mochila'.
inventario["mochila"].sort()

#Remueve 'daga' de la lista de elementos en la llave 'mochila'.
inventario["mochila"].pop(0)

#Suma 50 al valor almacenado en la llave 'oro'.
inventario["oro"]=inventario["oro"]+50
