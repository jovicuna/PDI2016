#Procesamiento digital de imagenes: Laboratorio 03 - Junio 2016
#Alumnos: Katherine Duguet && Joaquín Vicuña
from SimpleCV import Camera , Image, Display
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
import cv2
from scipy import misc

#Creamos nuestra base de datos
name = raw_input("Ingrese nombre de paciente: ") #Ingresamos un string con el nombre del paciente
db = R'/home/pi/PDI2016/lab03/Database' #Este es el directorio donde pretendemos guardar la base de datos

print "\n"

path1 = db
path2 = name
path3 = 'Conjunto_Imagenes'
#Creamos carpeta con la base de datos
if not os.path.exists(path1):
    os.makedirs(path1)

os.chdir(db) #Ingresamos a nuestra base de datos (en adelante DB)

#Creamos y/o verificamos la carpeta del paciente en nuestra 
if not os.path.exists(os.path.join(path1,path2)):
    os.makedirs(os.path.join(path1,path2))
    print "Paciente: "+name+ " creado correctamente \n"

os.chdir(path2) #Ingresamos al directorio del paciente
print "Accesando de manera correcta a los datos de: " +name+"\n"
#Creamos carpeta para el conjunto de imagenes para el caso de elegir el metodo 2
if not os.path.exists(path3):
    os.makedirs(path3)

    

#Ahora capturaremos las imagenes y trabajaremos con ellas

c = Camera()
img = c.getImage()
img.save('Captura.png')
img.show()

#Segmentacion de canales RGB
(red, green, blue) = img.splitChannels(False)
#Histogramas para cada canal RGB
print("1) Implementacion SimpleCV")
print("2) Model-Based Edge Detector")
m = int(input("Ingrese metodo a utilizar: "))

if m==1:
    red.save('Captura_rojo.png')
    #Rojo
    hist_r = red.histogram(255)
    plt.plot(hist_r)
    plt.show()
    r1 = int(input("Ingrese parametro t1 (inicial) a utilizar: "))
    r2 = int(input("Ingrese parametro t2 (final) a utilizar: "))
    r3 = int(input("Ingrese parametro t3 (inicial) a utilizar: "))
    r4 = int(input("Ingrese parametro t4 (final)a utilizar: "))
        
    green.save('Captura_verde.png')
    #Verde
    hist_g = green.histogram(255)
    plt.plot(hist_g)
    plt.show()
    
    g1 = int(input("Ingrese parametro (inicial) t1 a utilizar: "))
    g2 = int(input("Ingrese parametro (final) t2 a utilizar: "))
    g3 = int(input("Ingrese parametro (inicial) t3 a utilizar: "))
    g4 = int(input("Ingrese parametro (final) t4 a utilizar: "))
    
    blue.save('Captura_azul.png')
    #Azul
    hist_b = blue.histogram(255)
    plt.plot(hist_b)
    plt.show()
    b1 = int(input("Ingrese parametro t1 (inicial) a utilizar: "))
    b2 = int(input("Ingrese parametro t2 (final) a utilizar: "))
    b3 = int(input("Ingrese parametro t3 (inicial) a utilizar: "))
    b4 = int(input("Ingrese parametro t4 (final) a utilizar: "))
    
    #Escala de grises
    igr = img.grayscale()
    igr.save('Captura_gris.png')
    
    #Histograma para escala de grises
    hist_gr = igr.histogram(255)
    plt.plot(hist_gr)
    plt.show()
    gr1 = int(input("Ingrese parametro t1 (inicial) a utilizar: "))
    gr2 = int(input("Ingrese parametro t2 (final) a utilizar: "))
    gr3 = int(input("Ingrese parametro t3 (inicial) a utilizar: "))
    gr4 = int(input("Ingrese parametro t4 (final) a utilizar: "))
    #Detectamos los bordes con la implementacion de SimpleCV
    #[Recordar que los parametros para la funcion edges de SimpleCV
    #los modificamos en funcion de los valores del histograma que tenemos anteriormente para cada canal]
    
    ir = Image('Captura_rojo.png')
    ig = Image('Captura_verde.png')
    ib = Image('Captura_azul.png')
    
    #(...)Para escala de grises
    b_gr = igr.edges(gr1,gr2)
    b_gr.save('Borde_gris.png')
    
    #(...) y para canales RGB
    b_r = ir.edges(r1,r2) #Rojo
    b_r.save('Borde_rojo.png')
    
    b_g1 = ig.edges(g1,g2) #Verde
    b_g1.save('Borde_verde_1.png')
    b_g2 = ig.edges(g3,g4)
    b_g2.save('Borde_verde_2.png')
    b_g = b_g1 + b_g2
    b_g.save('Borde_verde_T.png')
    
    b_b1 = ib.edges(b1,b2) #Azul
    b_b1.save('Borde_azul_1.png')
    b_b2 = ib.edges(b3,b4)
    b_b2.save('Borde_azul_2.png')
    b_b = b_b1 + b_b2
    b_b.save('Borde_azul_T.png')
if m == 2:
    os.chdir(path3)

    c = Camera()

    img1 = c.getImage()
    img1.save('C1.png')

    img2 = c.getImage()
    img2.save('C2.png')

    img3 = c.getImage()
    img3.save('C3.png')
    
    #I1 = misc.I1()
    #I2 = misc.I2()
    #I3 = misc.I3()

    misc.imsave('C1.png',I1)
    misc.imsave('C2.png',I2)
    misc.imsave('C3.png',I3)

    I1 = misc.imread('C1.png')
    I2 = misc.imread('C2.png')
    I3 = misc.imread('C3.png')

    (red1,green1,blue1) = I1.splitChannels(False)
    (red2,green2,blue2) = I2.splitChannels(False)
    (red3,green3,blue3) = I3.splitChannels(False)

    I1.shape(480,640,3) , I1.dtype('unit8')
    I2.shape(480,640,3) , I2.dtype('unit8')
    I3.shape(480,640,3) , I3.dtype('unit8')

    cnt = 0
    cnt_p = 0
    ceros = np.zeros((480,640))
