#Procesamiento digital de imagenes: Laboratorio 19 - Agosto 2016
#Alumnos: Katherine Duguet && Joaquín Vicuña

from SimpleCV import Camera, Display, Image
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
import cv2
from scipy import misc

i = Image('Imagen.png')

hist = i.histogram(255)
plt.plot(hist)
plt.show()



