diccionario = {
    'redes sociales' : ['Twiter', 'Facebook' , 'LinkedIn'],
    3: 'Tres',
    'Hola' : 'Mundo'
}

print diccionario.has_key('Hola')
print diccionario.items()
print diccionario.keys()
print diccionario.values()
print diccionario.pop(3)
del diccionario['Hola']
print diccionario
print diccionario.clear()
diccionario['clave_nueva'] = "valor"
print diccionario

diccionario2 = diccionario.copy()
print diccionario2