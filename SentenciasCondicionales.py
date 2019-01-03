edad = 17
m_edad = 18

if edad >= m_edad: 
    print 'eres mayor de edad'
    if True:
        print 'esto se ejecuta siempre que sea mayor de edad'
    else:
        print 'cualquier cosa'
else:
    print 'no eres mayor de edad'
print 'hola esto se ejecuta siempre'


edad = 60
#encoding: utf-8

if edad >= 0 and edad < 18:
    print 'eres un nino'
elif edad >= 18 and edad < 27:
    print 'eres un joven'
elif edad >= 27 and edad < 60:
    print 'eres un adulto'
else:
    print 'eres de la tercera edad'
    