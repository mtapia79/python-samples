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
    
    def estudiarCaso(self, de):
        print self.edad
        print 'debo estudiar el caso de ' , de
        
pedro = IngSistemas()
pedro.hablar('hola pedro')
pedro.programar('python')

raul = LicDerecho(21)
raul.hablar('hola pedro')
raul.estudiarCaso('casas')