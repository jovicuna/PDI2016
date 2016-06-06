
#Procesamiento digital de imagenes: Laboratorio 03 - Junio 2016
#Alumnos: Katherine Duguet && Joaquín Vicuña
from SimpleCV import Camera , Image, Display
import os
import sys
import matplotlib.pyplot as plt

#Creamos nuestra base de datos
name = raw_input("Ingrese nombre de paciente: ") #Ingresamos un string con el nombre del paciente
db = R'/home/pi/PDI2016/lab03/Database' #Este es el directorio donde pretendemos guardar la base de datos

print "\n"

path1 = db
path2 = name

#Creamos carpeta con la base de datos
if not os.path.exists(path1):
    os.makedirs(path1)

os.chdir(db) #Ingresamos a nuestra base de datos (en adelante DB)

#Creamos y/o verificamos la carpeta del paciente en nuestra 
if not os.path.exists(os.path.join(path1,path2)):
    os.makedirs(os.path.join(path1,path2))
    print "Paciente: "+name+ " creado correctamente \n"

os.chdir(path2) #Ingresamos al directorio del paciente
print "Accesando de manera correcta a: " +name+"\n"
    

#Ahora capturaremos las imagenes y trabajaremos con ellas

c = Camera()
img = c.getImage()
img.save('Captura.png')
img.show()

#Segmentacion de canales RGB
(red, green, blue) = img.splitChannels(False)
#Histogramas para cada canal RGB

red.save('Captura_rojo.png')
#Rojo
hist_r = red.histogram(255)
plt.plot(hist_r)
plt.show()
#plt.save('histogram_gray.png')
    
green.save('Captura_verde.png')
#Verde
hist_g = green.histogram(255)
plt.plot(hist_g)
plt.show()
#plt.save('histogram_gray.png')
    
blue.save('Captura_azul.png')
#Azul
hist_b = blue.histogram(255)
plt.plot(hist_b)
plt.show()
#plt.save('histogram_gray.png')

#Escala de grises
igr = img.grayscale()
igr.save('Captura_gris.png')

#Histograma para escala de grises
hist_gr = igr.histogram(255)
plt.plot(hist_gr)
plt.show()

#Detectamos los bordes con la implementacion de SimpleCV
#[Recordar que los parametros para la funcion edges de SimpleCV
#los modificamos en funcion de los valores del histograma que tenemos anteriormente para cada canal]

#(...)Para escala de grises
b_gr = igr.edges(t1=3,t2=5)
b_gr.save('Borde_gris.png')

#(...) y para canales RGB
b_r = ir.edges(t1=168,t2=252) #Rojo
b_r.save('Borde_rojo.png')

b_g1 = ig.edges(t1=6,t2=8) #Verde
b_g1.save('Borde_verde_1.png')
b_g2 = ig.edges(t1=174,t2=179)
b_g2.save('Borde_verde_2.png')
b_g = b_g1 + b_g2
b_g.save('Borde_verde_T.png')

b_b1 = ib.edges(t1=7,t2=10) #Azul
b_b1.save('Borde_azul_1.png')
b_b2 = ib.edges(t1=171,t2=235)
b_b2.save('Borde_azul_2.png')
b_b = b_b1 + b_b2
b_b.save('Borde_azul_T.png')
