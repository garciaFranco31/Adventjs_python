"""
La fábrica de Santa ha empezado a recibir la lista de producción de juguetes.
Cada línea indica qué juguete hay que fabricar y cuántas unidades.

Los elfos, como siempre, han metido la pata: han apuntado algunos juguetes con cantidades que no tienen sentido.

Tienes una lista de objetos con esta forma:

toy: el nombre del juguete (string)
quantity: cuántas unidades hay que fabricar (number)
Tu tarea es escribir una función que reciba esta lista y devuelva un array de strings con:

Cada juguete repetido tantas veces como indique quantity
En el mismo orden en el que aparecen en la lista original
Ignorando los juguetes con cantidades no válidas (menores o iguales a 0, o que no sean número)


"""

production1 = [
  { "toy": 'car', "quantity": 3 },
  { "toy": 'doll', "quantity": 1 },
  { "toy": 'ball', "quantity": 2 }
]

#print(production1[1]["toy"])

final_list = []
for toy in production1:
    quantity  = toy["quantity"]
    if quantity > 0:
        for i in range(quantity):
            final_list.append(toy["toy"])

print(final_list)