# Funcion a utilizar con map y reduce
def suma(n,m):
    return n + m

#funcion a utilizar con filter
def filtrar(n):
    return (n == 'o')

li = [1, -2 , 1 , -4]
lo = [5,3,6,7]
s = "Hoola Mundo"

print map(suma,li,lo)
print filter(filtrar,s)
print reduce(suma, lo)

#lambda son funciones anonimas y siempre regresa algo, tiene que ser una sola linea y sir ve para usar la en map, filter y reduce
#sirve para reducir lineas de codigo. aqui vamos a reemplazar las funciones de suma y filtrar por funciones lambda

ss = lambda n,m : n+m

print map(ss,li,lo)
print filter(lambda n : n == 'o' ,s)
print reduce(ss, lo)

print ss(3,4)