class Humano:
    #constructor, en self se guarda la referebcia del objeto que se esta guardando
    def __init__(self, edad):
        self.edad = edad
        print 'soy un nuevo objeto'
    
    def hablar(self,mensaje):
        print self.edad
        print mensaje

pedro = Humano(25)
pedro.hablar('hola pedro')
print 'soy pedro y tengo' , pedro.edad
raul = Humano(21)
raul.hablar('hola raul')
print 'soy raul y tengo' , raul.edad