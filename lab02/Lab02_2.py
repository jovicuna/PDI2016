from SimpleCV import Camera, Image, Display
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import utils
import cv2
import numpy as np

n = int(input("Ingrese cantidad de clusters: "))
igk = cv2.imread("imagen_grises.png") #Lectura de la imagen original en grayscale
(a,b) = igk.shape[:2]
igk = igk.reshape((igk.shape[0]*igk.shape[1] , 3))
clustering = KMeans(n_clusters = n)
agrup = clustering.fit_predict(igk)
cnt = clustering.cluster_centers_.astype("uint8")[agrup]
agrup = cnt.reshape(a,b,3)

plt.figure(1)
plt.axis("off")
plt.imshow(agrup)
plt.savefig('imagen_kmeans.png')
plt.show()



