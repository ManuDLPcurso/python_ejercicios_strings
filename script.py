'''
texto = "— ¡Eres un completo Gilipollas!—gritó Carlos, tirando el plato sobre la mesa.Marta lo miró sin inmutarse, cruzada de brazos.— El único idiota aquí eres tú, que te pones a gritar por un poco de brócoli.— ¡No es un poco de brócoli, pedazo de idiota! ¡Es que llevamos tres días cenando brócoli! ¿Te crees que tengo cara de maldito conejo o qué te pasa? —exclamó él, rojo de la rabia.— Escúchame bien, gilipollas —respondió Marta, dando un golpe en la mesa—. Si no te gusta el brócoli, te cocinas tú. Pero claro, como eres un idiota integral que no sabe ni freír un huevo, pretendes que yo te haga un banquete cada noche.Carlos resopló, mirando con desprecio el árbol verde atrapado en su tenedor.— Un gilipollas no se comería esto. Un idiota quizá sí. Así que quédate con tu brócoli, porque yo me voy a pedir una pizza.— Pues vete, idiota. A ver si la masa de la pizza te despierta las dos neuronas que te quedan, gilipollas. Y ni se te ocurra pedir la mía con brócoli, que te conozco.¿Te gustaría que cambie el tono de la historia (hacerla más cómica, absurda o dramática) o prefieres que añada más palabras repetitivas a la escena?"

marca_censura = "***"

reemplazos = {
    "gilipollas": marca_censura,
    "brocoli": marca_censura,
    "idiota": marca_censura
}

texto_modificado = texto
for original, censurado in reemplazos.items():
    texto_modificado = texto_modificado.replace(original, censurado)

print(f"{texto_modificado}\n -----------------------------------")
print(f"{texto_modificado}\n -----------------------------------")

texto_modificado = texto.replace("gilipollas", "********").replace("brocoli","++++++++").replace("idiota","-------")
print(f"{texto_modificado}\n -----------------------------------")



ticket = '2026091705-Type 01-Client 3420a-no me funciona la internet'
ticket_normalized = ticket.replace('-',' * ').replace('Type','Tipo').replace('Client','Cliente').replace('34','Spain-').upper()
id, tipo, cliente, issue = ticket_normalized.split('*')
print(f'\n ID: {id} \n Type: {tipo} \n Client: {cliente} \n Issue: {issue} \n')


with open("el_quijote.txt", "rt", encoding="utf-8") as f:
    texto = f.read().lower()
    
texto_modificado = texto.replace('Quijote','Manuel')

cuenta = texto.count("DULCINEA".lower())
print(cuenta)
'''
import re

entradaDni = input("Ingrese su DNI: ")
patronDni = r'^\d{8}[A-Z]{1}$'
entradaIban = input("Ingrese su IBAN: ")
patronIban = r'^ES\d{22}$'
entradaPass = input("Ingrese su Password: ")
patronPass = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
entradaEmail = input("Ingrese su Email: ")
patronEmail = r'^[a-zA-Z0-9_%+-]+(?:\.[a-zA-Z0-9_%+-]+)*@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}$'


#DNI
if re.match(patronDni, entradaDni):
    print(f"- Su DNI nº {entradaDni} es correcto, continue\n")
else:
    print(f"- Su DNI nº {entradaDni} es incrorrecto, retroceda\n")

#PASSWORD
if re.match(patronPass, entradaPass):
    print(f"- Su Password {entradaPass} es correcto, continue\n")
else:
    print(f"- Su Password {entradaPass} es incrorrecto, retroceda\n")

#EMAIL
if re.match(patronEmail, entradaEmail):
    print(f"- Su Email {entradaEmail} es correcto, continue\n")
else:
    print(f"- Su Email {entradaEmail} es incrorrecto, retroceda\n")

#IBAN
if re.match(patronIban, entradaIban):
    print(f"- Su IBAN nº {entradaIban} es correcto, continue\n")
else:
    print(f"- Su IBAN nº {entradaIban} es incrorrecto, retroceda\n")        



