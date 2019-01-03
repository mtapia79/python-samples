#similar a comprension de listas, pero no regresan una lista, regresan valores de uno en uno para iterar
#para hacer esto hay que reemplazar los corchetes cuadrados de las iteraciones por parentesis

l = [1,2,3, -1 ,4]
s = ['H','o','l','a']
l2 = (c * num for c in s
                for num in l
                     if num > 0)

print l2
print l2.next()
print l2.next()

for letra in l2:
    print letra
    

def factorial(n):
    i = 1
    while n > 1:
        i = n*i
        yield i # palabra reservada se confierte la funcion a objeto generador, que hace la misma pega de la linea 6
        n -= 1 

for e in factorial(5):
    print e