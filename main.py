import cv2
import numpy as np
import sys
import faceSwap
import random
import dlib


#write down all the faces
facesList = ["agermer.jpg", 
             "ahunter2.jpg",
             "alanhsu.jpg", 
             "alexx.jpg", 
             "andrewh1.jpg",
             "koz.png"]

face = random.choice(facesList)
print(face)
img = cv2.imread(face)

faceSwap.faceSwap(img)