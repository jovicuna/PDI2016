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
max = np.max(hist)
#Segmentacion
ibin = ig.binarize(max)
ibin.save('imagen_binaria.png')
ibin.show()
#Muestra del histograma
plt.show()
