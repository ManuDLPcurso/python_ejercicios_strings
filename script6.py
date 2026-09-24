recetas = {
    "Pasta a la boloñesa": {"pasta", "tomate", "carne picada", "cebolla", "queso rallado"},
    "Tortilla de patata": {"huevo", "patata", "cebolla", "aceite de oliva", "sal"},
    "Bocadillo de jamón": {"pan", "jamón serrano", "tomate", "aceite de oliva", "ajo"}
}

nevera_lista = [
    "tomate",           
    "huevo",           
    "cebolla",          
    "aceite de oliva", 
    "leche",            
    "mantequilla",      
    "yogur",            
    "lechuga",
    "sal",
    "patata",
    "ajo",
    "pan",
    "jamón serrano"
]

separador = ("=" * 10)
nevera = set(nevera_lista)

print(f"\n{separador} RECETARIO {separador}\n")

for name, receta in recetas.items():
    
    if receta.issubset(nevera):
        print(f"{name}: Puedes hacer esta receta\n")
    else:
        faltantes = receta - nevera
        print(f"{name}: Te faltan los siguientes ingredientes: {list(faltantes)}\n")


