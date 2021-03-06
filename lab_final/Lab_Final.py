#Procesamiento digital de imagenes: Laboratorio 19 - Agosto 2016
#Alumnos: Katherine Duguet && Joaquín Vicuña

from SimpleCV import Camera, Display, Image
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
import cv2
from scipy import misc

c = Camera()
i = c.getImage()
i.save('Imagen.png')

hist = i.histogram(255)
plt.plot(hist)
plt.show()

dil = i.dilate(200)
dil.save('Dil.png')

prom = (i+dil)/2
prom.save('Prom.png')

suma = (i + dil)
suma.save('Sum.png')


