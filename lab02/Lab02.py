#!/usr/bin/env python
from SimpleCV import Camera, Image, Display
import matplotlib.pyplot as plt
import numpy as np
c = Camera()
#Obtencion de la imagen
i = c.getImage()
i.save('imagen_normal.png')
#Escala de grises
ig = i.grayscale()
ig.save('imagen_grises.png')
ig.show()
#Histograma
hist = ig.histogram(255)
plt.plot(hist)
plt.show()
#Segmentacion de mascaras
r1 = 117
r2 = 165
r3 = 170

#Mascara 1
ibin1 = ig.binarize(r1)
ibin1.save('imagen_mascara_1.png')
ibin1.show()

#Mascara 2
ibin2 = ig.binarize(r2)
ibin2.save('imagen_mascara_2.png')
ibin2.show()

#sin texto
i3= ibin2 - ibin1
i3.save('imagen_diferencia.png')
i3.show()
 
#Mascara 3
ibin = ig.binarize(r3)
ibin.save('imagen_mascara_3.png')
ibin.show()




