#relacionado con funciones matematicas
#funcion de orden superior

def prueba(f):
    #se retorna el valor de la funcion invocada
    return f()

def porEnviar():
    return 2+2

print prueba(porEnviar)




def seleccion(operacion):
    
    def suma(n,m):
        return n + m

    def multiplicacion(n,m):
        return n * m

    if operacion == 'suma':
        return suma
    elif operacion == 'multi':
        return multiplicacion


#en esta variable queda guardada la funcion de suma rtornada por la seleccion escogida, em este caso nos retorna la funcion de suma
fGuardada = seleccion('suma')

#los parentesis en una funcion se usan solo para ejecutarla, sino se le agregan los parentesis, nunca se ejecutara esa funcion
print fGuardada(1,7)