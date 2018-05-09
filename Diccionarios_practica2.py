#Calcula el valor total del carrito usando operaciones en Python y ambos diccionarios.
carrito = {
    "bananas": 6,
    "manzanas": 0,
    "naranjas": 32,
    "peras": 15
  }

precios = {
    "bananas": 4,
    "manzanas": 2,
    "naranjas": 1.5,
    "peras": 3
  }
  
precioCarrito=carrito["bananas"]*precios["bananas"]+carrito["manzanas"]*precios["manzanas"]+carrito["naranjas"]*precios["naranjas"]+carrito["peras"]*precios["peras"]
  
print("El precio del carrito es $", precioCarrito)