""" import re
import hashlib

def hashPassword(password):
    return hashlib.sha256(password.encode()).hexdigest()

def menu():

    while True:

        print('\nSeleccione una opción:\n\n','1- Registro\n','2- Ingresar\n','3- Recuperar contraseña\n','4- Salir\n')
        seleccion = input('--> ').strip()
        if seleccion == '1':
            signIn()
        elif seleccion == '2':
            logIn()
        elif seleccion == '3':
            recoveryPassword()
        elif seleccion == '4':
            print('Hasta luego!\n')
            break
        else:
            print('\033[31mIngrese un número válido.\033[0m\n')

#--------------------------------------------------------------------------

def signIn():

    patronEmail = r'^[a-zA-Z0-9_%+-]+(?:\.[a-zA-Z0-9_%+-]+)*@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}$'
    patronPassword = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,15}$'

    while True:
        registroEmail = input("\033[33mIngrese su correo: \033[0m\n")
        registroPassword = input("\033[33mIngrese su password: \033[0m\n")
        passwordHasheada = hashPassword(registroPassword)
        
        if not re.match(patronEmail, registroEmail):
            print("\033[31mCorreo no valido. Intentelo de nuevo.\033[0m\n") 
            continue

        if not re.match(patronPassword, registroPassword):
                    print("\033[31mFormato de contraseña no valido.\nDebe contener entre 6 y 15 caracteres.\nIntentelo de nuevo.\033[0m\n") 
                    continue

        fileName = f'{registroEmail.replace('@','_')}.txt'
        
        with open(fileName, "wt", encoding="utf-8") as f:
            f.write(f'{registroEmail}\n')
            f.write(f'{passwordHasheada}\n')
        
        print("\033[32mUsuario creado correctamente\033[0m\n")
        
        break

#--------------------------------------------------------------------------

def logIn():
        
    while True:
        loginEmail = input("\033[33mIngrese su correo: \033[0m\n")
        loginPassword = input("\033[33mIngrese su password: \033[0m\n")

        fileName = f'{loginEmail.replace('@','_')}.txt' 
        try:

            with open(fileName, "rt", encoding="utf-8") as f:
                lineasFichero = f.read().splitlines()
                emailFichero = lineasFichero[0]
                passwordFichero = lineasFichero[1]

        except FileNotFoundError:

            print("\033[31mEl correo electrónico no está registrado. Inténtelo de nuevo.\033[0m\n")
            continue
        

        if loginEmail != emailFichero or hashPassword(loginPassword) != passwordFichero:
            print (f'\033[31mCorreo o contraseña incorrectos\033[0m\n')
            continue
        print(f'\033[32mBienvenido, {loginEmail}\033[0m\n') 
        
        break
        
#--------------------------------------------------------------------------

def recoveryPassword():
    emailRecuperacion = input("\033[33mIngrese su correo: \033[0m\n")

    fileName = f'{emailRecuperacion.replace('@','_')}.txt'

    try:

        with open(fileName, "rt", encoding="utf-8") as f:
            lineasFichero = f.read().splitlines()
            print(f'\033[32mSu correo es {lineasFichero[0]}\033[0m')
            print(f'\033[32mSu contraseña es {lineasFichero[1]}\033[0m\n')

    except FileNotFoundError:
        
        print("\033[31mEl correo electrónico no está registrado. Inténtelo de nuevo.\033[0m") """

        

#--------------------------------------------------------------------------



ingredientes = ['Harina', 'Leche', 'Huevo', 'Vino', 'Sal']

ingredientes_mayusculas = list(map(str.upper, ingredientes))

ingredientes_simbolos = [ingrediente.replace("a","@") and ingrediente.replace("e","€") for ingrediente in ingredientes]

print(ingredientes_simbolos)

