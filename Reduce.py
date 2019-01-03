s = ('H','o','l','a','_','M','u','n','d','o')

def concatenar(a,b):
    return a + b
sr = reduce(concatenar,s)

print sr

s = (1,2,3)
def concatenar(a,b):
    return a + b

sr = reduce(concatenar,s)

print sr