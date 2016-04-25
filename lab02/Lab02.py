#!/usr/bin/env python
from SimpleCV import Camera, Image, Display
import matplotlib.pyplot as plt
c = Camera()
i = c.getImage()
i.save('imagen_normal.png')
ig = i.grayscale()
ig.save('imagen_grises.png')
ig.show()
hist = ig.histogram()
plt.plot(hist)
plt.show()
