import cv2
import numpy
import sys
import faceSwap
import random


#write down all the faces
facesList = ["agermer.jpg", 
             "ahunter2.jpg",
             "alanhsu.jpg", 
             "alexx.jpg", 
             "andrewh1.jpg"]

TAface =  random.choice(facesList)
kozFace = "koz.png"


#if open mouth: distance between point 63 and 67 > threshold,
#change to random TA face
'''
if _________:
    img = cv2.imread(TAface)
'''
