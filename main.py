import cv2
import numpy as np
import sys
import faceSwap
import random
import dlib
from cmu_112_graphics import *


#write down all the faces
def appStarted(app):
    app.facesList = ["agermer.jpg", 
                "ahunter2.jpg",
                "alanhsu.jpg", 
                "alexx.jpg", 
                "andrewh1.jpg",
                "koz.png"]

def keyPressed(app, event):
    if event.key == 'c':
        face = random.choice(app.facesList)
        print(face)
        img = cv2.imread(face)
        faceSwap.faceSwap(img)

def redrawAll(app, canvas):
    canvas.create_text(app.width/2, app.height/2, text = "Press C to swap face, ESC to quit.", font = 'Arial 14')

runApp(width = 300, height = 80)
