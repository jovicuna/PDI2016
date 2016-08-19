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

ig = i.grayscale()
ig.save('Imagen_Gris.png')

bord = ig.edges()
bord.save('Bordes.png')




