lista = [1, 'dos' ,3]
print lista
lista.append("nueva lista")
print lista
print lista.count(3)

lista.insert(2, "nuevo")
print lista 

iterable = "cadena" #(1,2,3) [1,2,3]
lista.extend(iterable)
print lista

lista.pop(3)
print lista

lista.remove(1)
print lista

lista.reverse()
print lista


buscar = 1

if buscar in lista:
    print lista.index(buscar)
else:
    print 'no esta elemento'