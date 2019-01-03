#recibe una funcion y retorna otra funcion decorada

def decorador(funcion):
    #*args n cantidad de atributos , **kwargs diccionario con clave valor
    def funcionDecorada(*args, **kwargs):
        print 'funcion ejecutada' , funcion.__name__
        funcion(*args, **kwargs)
    
    return funcionDecorada

def resta(n,m):
    print n-m

#decorando
decorada = decorador(resta)

decorada(5,3)



# este tag es lo mismo que decir decorador(resta)(5,3)
@decorador
def resta(n,m):
    print n-m
    
resta(5, 3)


logeado = False
usuario = 'mtapia'

def admin(f):
    def comprobar(*args, **kwargs):
        if logeado:
           f (*args, **kwargs)
        else:
            print 'no tiene permisos de ejecutar ' , f.__name__ 
    return comprobar

@admin
@decorador
def resta(n,m):
    print n-m

resta(5, 3)
