estaciones = ['primavera', 'verano', 'otoño', 'invierno']
for estacion in estaciones: 
    print(estacion)

estaciones = ['primavera', 'verano', 'otoño', 'invierno']
for estacion in estaciones: 
    print(estacion)    

estaciones = ['primavera', 'verano', 'otoño', 'invierno']
lista = [estacion.upper()[:5] for estacion in estaciones]

print(lista)


numeros = tuple('1')
print(numeros)

for numero in numeros:
    print(numero*2)

lista_dobles = [n*n for n in numeros if n>2]
print(lista_dobles)