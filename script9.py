""" class IBANException(ValueError):
    def escribir_log(self, mensaje):
            print(mensaje)

class DNIException(ValueError):
    def __init__(self, *args):
        super().__init__(*args)
    def escribir_log(self, mensaje):
        print(mensaje)



try:
    dni = 'dkfjsdksd'
    if dni!='ABC':
        raise DNIException('TIENES EL DNI MAL')
     except DNIException as ex:
    ex.escribir_log('Ha ocurrido algo') 




try:
    edad_input = int(input("Ingrese su edad: "))
    print("OK")

except BaseException as be:
    print(f"Error: {be}") """


""" n1, n2 = input("Ingrese numero 1: "), input("Ingrese numero 2: ")

def calculadora(n1 , n2):
    suma =  n1 + n2
    resta = n1 - n2
    division = n1 / n2

    return suma, resta, division

try: 
    n1 = int(n1)
    n2 = int(n2)

    r_suma, r_resta, r_division = calculadora(n1, n2)
    print(f"Suma: {r_suma}", f"Resta: {r_resta}", f"Division: {r_division}")

except ValueError:
    print("Debes introducir numeros")

except ZeroDivisionError:
    if n2 == 0:
        print("No se puede dividir entre 0") """


edad = -5
if edad < 0:
    raise ValueError("La edad no puede ser un número negativo.")
