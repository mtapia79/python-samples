#regresa el valor que el usuario ingfreso en el teclado


try:
    valor = raw_input("Introduce un numero:")
    valor = int(valor)
except:
    print 'eso no es un numero'
else:
    print valor