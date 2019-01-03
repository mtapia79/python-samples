class Humano:
    #constructor, en self se guarda la referebcia del objeto que se esta guardando
    def __init__(self, edad):
        self.edad = edad
 
    
    def hablar(self,mensaje):
        print mensaje
        

class IngSistemas(Humano):
    def __init__(self):
        print 'hola self IngSistemas'
        
    def programar(self, lenguaje):
        print 'voy a programar en ' , lenguaje

class LicDerecho(Humano):
    def __init__(self, escuela):
        print 'licenciado de derecho egresado de' , escuela
        
    def estudiarCaso(self, de):
        print 'debo estudiar el caso de ' , de
    

class Estudioso(IngSistemas,LicDerecho): 
    #vete no hay nada que ver aqui
    pass   


pepe = Estudioso()
pepe.hablar('soy de herencia multiple')
pepe.programar('java')
pepe.estudiarCaso('mio')
