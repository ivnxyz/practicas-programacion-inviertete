with open("nombres.txt") as archivo:
    usuarios = archivo.readlines()
    
dic={}
contador = 0
for nombres in usuarios:
    dic = nombres.split("|"), nombres.split("|")[1],
    print(dic[1])