def filtro(elem):
    return (elem > 0)
    
l = [1 , -3, 2 , -7 , -8 , -9 , 10]

lr = filter(filtro, l)

print l
print lr
print type(lr)


def filtro(elem):
    return (elem == 'o')

s = 'Hola Mundo'
lr = filter(filtro,s)
print s
print lr
print type(lr)