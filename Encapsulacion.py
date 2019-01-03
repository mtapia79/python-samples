# metodos y atributos inicados con __ son privados

class Prueba(object):
    def __init__(self):
        self.__privado = 'soy atributo privado'
        self.privado = 'soy atributo publico'
    
    def __metodoPrivado(self):
        print 'soy metodo privado'
    
    def metodoPublico(self):
        print 'soy metodo publico'

    def getPrivado(self):
        return self.__privado
    
    def setPrivado(self,valor):
        self.__privado = valor

prueba = Prueba()

print prueba.privado
# da error porque no se puede invocar a atributo privado
#print prueba.__privado

print prueba.metodoPublico()
#da error porque no se puede invocar a metodo privado
#print prueba.__metodoPrivado()

print prueba.setPrivado("me estan cambiando el privado")
print prueba.getPrivado()