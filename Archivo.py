#escritura
try:
    f = open('ejemplo.txt','w')
except:
    exit()
    f = 'archivo mo existe'
    

f.write("creando mi primer archivo")

f.seek(-2,2)

print f.tell()

f.write('intruso   ')
print f


agregar = ['hola','mundo','programadores ']
f.writelines(agregar)

agregar2 = ['\nhola mundo\n','\tprogramadores']
f.writelines(agregar2)

f.close()

agregar3 = ['1','3']
#valida si el archivo esta cerrado
if not f.closed:
    f.writelines(agregar2)
    
 
 #lectura
try:
    f = open('ejemplo.txt','r')
except:
    exit()
    f = 'archivo mo existe'
       
print f.read(10)
print f.readline()


while True:
    print f.readline()
    if f.readline() == "" :
        break;
    
    

lineas = f.readlines()

for l in lineas:
    print "=> ", l , '\n\n'