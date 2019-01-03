l = [2, "tres" , True , ["uno",10]]
print l

l2 = l[0]

print l2

l3 = l[3][0]
print  l3

l[1] = 4

l4 = l[1]

print l4

# copia una lista con los elementos del 0 al 3
l5 = l[0:3]
print l5

#copia de forma alternada cada 2 espacios , uno si otro no
l6 = l[0:3:2]
print l6

#cambiar valores dentro de la lista
l[0:2] = [4,3]
print l

#imprime lista de atras hacia adelante
l2 = l[-1]
print l2


