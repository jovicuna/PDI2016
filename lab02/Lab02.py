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
r2 = 132
r3 = 173

#Mascara 1
ibin = ig.binarize(r1)
ibin.save('imagen_mascara_1.png')
ibin.show()

#Mascara 2
ibin = ig.binarize(r2)
ibin.save('imagen_mascara_2.png')
ibin.show()

#Mascara 3
ibin = ig.binarize(r3)
ibin.save('imagen_mascara_3.png')
ibin.show()




