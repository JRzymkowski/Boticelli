import cv2
import numpy as np
import random
import matplotlib.pyplot as plt

img = cv2.imread('b.jpg')
cv2.imshow("img",img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img,100,200)
edges = (255-edges)
ed2 = cv2.adaptiveThreshold(edges,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

def get_dark_point(im, threshold = 50):
    while True:
        x, y = random.randint(0, im.shape[0]), random.randint(0, im.shape[1])
        if im[x,y] < threshold:
            return (x,y)

def get_dp_within(im, p, threshold = 50, dist2 = 900):
    while True:
        x, y = random.randint(0, im.shape[0]), random.randint(0, im.shape[1])
        if (x-p[0])*(x-p[0]) + (y-p[1])*(y-p[1]) < dist2:
            if im[x,y] < threshold:
                return (x,y)


blank_image = np.fill((img.shape), 255)
for i in range(4):
    ps = []
    ps.append(get_dark_point(ed2))
    for j in range(3):
        ps.append(get_dp_within(ed2, ps[0]))
        cv2.line(blank_image, ps[j], ps[j+1], 0, 2)

cv2.imshow("edges",ed2)
cv2.imshow("lines",blank_image)
cv2.waitKey()

    

    

