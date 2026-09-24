ingredientes = ['Harina', 'Leche', 'Huevo', 'Vino', 'Sal']

ingredientes_mayusculas = list(map(str.upper, ingredientes))

ingredientes_simbolos = [ingrediente.replace("a","@").replace("e","€") for ingrediente in ingredientes]

ingredientes_tuplas = [(ingredientes[0], ingredientes[1]), (ingredientes[2], ingredientes[3])]

ingredientes_formatos = [(ingrediente.upper(), ingrediente.lower(), ingrediente.upper()[0:3], len(ingrediente)) for ingrediente in ingredientes]

peliculas = [('El Resplandor','Kubrick',3_000_000), ('Alien','Scott',1_000_000), ('Blade Runner', 'Scott', 4_000_000)]

peliculas_transform = [(pelicula[0].upper(), pelicula[1].upper(), float(pelicula[2]*0.87)) for pelicula in peliculas]


# Lista de países con (Nombre, Población, PIB en €, Superficie en km²)

paises_eur = [
    ("España", 48000000, 1472000000000, 505990),
    ("México", 128500000, 1343200000000, 1964375),
    ("Estados Unidos", 335000000, 25760000000000, 9833520),
    ("China", 1410000000, 16560000000000, 9596961),
    ("Japón", 124500000, 3864000000000, 377975),
    ("Brasil", 215000000, 1978000000000, 8515767),
    ("Alemania", 84400000, 4048000000000, 357022),
    ("India", 1430000000, 3496000000000, 3287263),
    ("Francia", 68000000, 2760000000000, 551695),
    ("Argentina", 46200000, 588800000000, 2780400)
]

""" paises_transform = [
                    (pais[0], 
                    f'{float(round(pais[1]/pais[3], 2))} habitantes por KM2',
                    f'{float(round(pais[2]/pais[1], 2))}€ de renta per capita', 
                    f'{int(pais[3])} KM2') 
                    
                    if float(round(pais[1]/pais[3], 2)) > 100 
                    else "DESPOBLADO"

                    for pais in paises_eur                                     
] """


def paises_superficie(paises_eur):
    return paises_eur[3]

def paises_densidad_poblacion(paises_eur):
    return round(paises_eur[1]/paises_eur[3], 2)

""" paises_ordenados = sorted(paises_eur, key=paises_superficie,reverse=True) """    
""" paises_eur.sort(key=paises_superficie,reverse=True) """
paises_eur.sort(key=paises_densidad_poblacion)


print(paises_eur)