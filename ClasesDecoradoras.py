class Decorador(object):
    """ mi clase decoradora """
    def __init__(self,funcion):
        self.funcion = funcion
    def __call__(self,*args, **kwargs):
         print 'funcion ejecutada' , self.funcion.__name__
         self.funcion(*args, **kwargs)



@Decorador
def resta(n,m):
    print n-m
resta(5, 3)
