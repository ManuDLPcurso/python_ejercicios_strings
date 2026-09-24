""" Create a Python program that identifies all numbers between 100 and 300 (inclusive) 
that are divisible by 7 but not multiples of 5. The identified numbers should be displayed 
in a single line, separated by commas. """

# Mi solución

""" for x in range(100, 300 + 1):
    if x%7 == 0:
        if x%5 != 0:
            print(x, end =", ") """


# Solución de la página
        
""" def find_numbers(start, end):
    result = []
    for i in range(start, end + 1):
        if i % 7 == 0 and i % 5 != 0:
            result.append(str(i))
    return ','.join(result)

# Call the function with specific start and end values
print(find_numbers(100, 200)) """



""" Create a Python function that takes an integer ( n ) as input and generates a dictionary 
containing pairs ( (i, i^2) ) for all integers ( i ) from 1 to ( n ) (inclusive). 
The function should then return this dictionary. """

""" def generate_square_dict(longitud):

    if longitud <= 10000:
        d = dict()

        for i in range(1, longitud + 1):
            d[i] = i*i

        return d
    else:
        print("Solo numeros entre 1 y 10.000")

num = int(input("Número: "))

print(generate_square_dict(num)) """

""" Create a Python function that takes a sequence of comma-separated numbers as input and generates
 both a list and a tuple containing those numbers. """

convert_input_to_list_and_tuple=("3,6,5,3,2,8")

# Mi solucion

""" def convert_list_tuple(cadena : tuple) -> list:
    cadena_split = cadena.split(",")
    cadena_def = ((list(cadena_split), tuple(cadena_split)))
    print(cadena_def) 


print(convert_list_tuple(convert_input_to_list_and_tuple)) """

# Solución de la página

""" def convert_input_to_list_and_tuple(input_string):
    values = input_string.split(",")
    return values, tuple(values)

convert_input_to_list_and_tuple("3,6,5,3,2,8") """

