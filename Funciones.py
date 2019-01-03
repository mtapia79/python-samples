def my_funcion(num1=0, num2=0):
    print num1 + num2

my_funcion(3,4)
my_funcion(3)

#se guarda en una tupla los parametros algomas
def my_funcion(cad , v=2,*algomas):
    print cad * v
    for cadena in algomas:
        print cadena

my_funcion("Python",5, 'hola','adios','N','Cadenas')


#se guarda en un diccionario los parametros algomas representado por 2 **
def my_funcion(cad , v=2,**algomas):
    print cad * v
    print algomas['cadenaextra']
    print algomas['cadenamas']

my_funcion("Python",5, cadenaextra='hola', cadenamas='adios')


#retornar un valor
def my_funcion(num1=0, num2=0):
    return num1 + num2

resultado_suma = my_funcion(3,4)
print resultado_suma