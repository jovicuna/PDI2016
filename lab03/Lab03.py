from SimpleCV import Camera , Image, Display
import os
import sys
name = raw_input("Ingrese nombre de paciente: ")
db = R'/home/pi/PDI2016/lab03/Database'
print "\n"

path1 = db
path2 = name

if not os.path.exists(path1):
    os.makedirs(path1)

os.chdir(db)

if not os.path.exists(os.path.join(path1,path2)):
    os.makedirs(os.path.join(path1,path2))
    print "Paciente: "+name+ " creado correctamente \n"

os.chdir(path2)
print "Accesando de manera correcta a: " +name+"\n"
    

