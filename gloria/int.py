promedio = float(input("Cuál es su promedio escolar:"))
LugarNacimiento= input("Donde nació?:")
Miembro= input("Es miembro de inviertete? (n/s):")
paso_prueba_1= promedio >= 9.0 and LugarNacimiento == "Oaxaca" and Miembro == "s"
    #Segunda prueba
Cantidad_de_tacos=int(input("Cuantos tacos comió?:"))
Tiempo_que_tarda= int(input("Cuanto tardó?:"))
Libros_en_un_año=int(input("cuantos libros lee?:"))
aprobo_prueba_2= (Cantidad_de_tacos >= 10 and Tiempo_que_tarda <= 45) and Libros_en_un_año >= 12
if paso_prueba_1 and aprobo_prueba_2:
     print("puede recibir la beca")
elif paso_prueba_1 == False and aprobo_prueba_2:
    print("No es ganador ya que no pasó la prueba 1")
elif paso_prueba_1  and aprobo_prueba_2 == False:
    print("No es ganador ya que no pasó la prueba 2")
else:
    print("no pasó ni una prueba")