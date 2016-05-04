from SimpleCV import Camera, Image, Display
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import utils
import cv2
import numpy as np

print("1) Histograma manual")
print("2) K-means clustering")
m = int(input("Seleccione metodo a utilizar: "))

#Obtencion de la imagen
c = Camera()
i = c.getImage()
i.save('imagen_normal.png')
    
#Escala de grises
ig = i.grayscale()
ig.save('imagen_grises.png')
ig.show()

if m==1:
    #Segmentacion por histograma
    
    #Histograma
    hist = ig.histogram(255)
    plt.plot(hist)
    plt.show()
    #Segmentacion de mascaras
    r1 = 117
    r2 = 165
    
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

if m==2:
    #K-means clustering
    n = int(input("Ingrese cantidad de clusters: "))
    igk = cv2.imread("imagen_grises.png") #Lectura de la imagen original en grayscale
    (a,b) = igk.shape[:2]
    igk = igk.reshape((igk.shape[0]*igk.shape[1] , 3))
    clustering = KMeans(n_clusters = n)
    agrup = clustering.fit_predict(igk)
    cnt = clustering.cluster_centers_.astype("uint8")[agrup]
    agrup = cnt.reshape(a,b,3)
    #Muestra imagen
    plt.figure(1)
    plt.axis("off")
    plt.imshow(agrup)
    plt.savefig('imagen_kmeans.png')
    plt.show()
