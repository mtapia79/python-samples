print 'Bienvenido'

try:
    print 1/0
except TypeError:
    print 'error de tipo de dato'
except NameError:
    print 'variable no existe'
except ZeroDivisionError:
    print 'no se puede dividir entre cero'
else:
    print 'no hubo error'
finally:
    print 'me ejcuto pase lo que pase'

print 'Adios'


#geberar errores propios

class UnoError(Exception):
    def __init__(self,valor):
        self.valorError=valor
    def __str__(self):
        print 'no se puede dividir entre 1 el numero ', self.valorError

print 'Bienvenido'

d = 5
n = 1

if n==1:
    raise UnoError(d)

    
print 'Adios'