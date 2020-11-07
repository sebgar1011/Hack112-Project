import cv2
import numpy as np
import sys
import faceSwap
import random
import dlib
from cmu_112_graphics import *


#write down all the TA faces
def appStarted(app):
    app.facesList = ["agermer.jpg", 
                "ahunter2.jpg",
                "alanhsu.jpg", 
                "alexx.jpg", 
                "andrewh1.jpg",
                "anitama.jpg",
                "asadalis.jpg",
                "athontak.jpg",
                "bradleyz.jpg",
                "bsidwell.jpg",
                "crystal3.jpg",
                "drazek.jpg",
                "dsyou.jpg",
                "eharllee.jpg",
                "ejzhang.jpg",
                "eswecker.jpg",
                "ezm.jpg",
                "gcui.jpg",
                "haeunk.jpg",
                "hpnguyen.jpg",
                "ijaffer.jpg",
                "jledon.jpg",
                "jritze.jpg",
                "jzych.jpg",
                "katheriy.jpg",
                "kbalenza.jpg",
                "kecooper.jpg",
                "knassre.jpg",
                "lnicolus.jpg",
                "lsands.jpg",
                "mbairath.jpg",
                "mdunaevs.jpg",
                "mling2.jpg",
                "mmookerj.jpg",
                "npadmana.jpg",
                "ntedesch.jpg",
                "pbhuang.jpg",
                "pingyac.jpg",
                "pokade.jpg",
                "rjogleka.jpg",
                "rmanley.jpg",
                "saralian.jpg",
                "shivankj.jpg",
                "skylarm.jpg",
                "ssagiraj.jpg",
                "stevenl2.jpg",
                "tmauzy.jpg",
                "tyf.jpg",
                "vbeaudoi.jpg",
                "yizes.jpg"
                ]
    app.face = None

def keyPressed(app, event):
    if event.key == 't':
        app.face = random.choice(app.facesList)
        print(app.face)
        img = cv2.imread(app.face)
        faceSwap.faceSwap(img)
            
    elif event.key == 'k':
        app.face = 'koz.png'
        print(app.face)
        img = cv2.imread(app.face)
        faceSwap.faceSwap(img)

def redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "light blue")
    canvas.create_text(app.width/2, app.height/2 - 15, text = "Press T to swap with a random TA's face,", font = 'Arial 20')
    canvas.create_text(app.width/2, app.height/2 + 15, text = "K for Kozbie's face, ESC to quit.", font = 'Arial 20')


runApp(width = 500, height = 200)
