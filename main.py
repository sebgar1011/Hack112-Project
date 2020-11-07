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

def keyPressed(app, event):
    if event.key == 'c':
        face = random.choice(app.facesList)
        print(face)
        img = cv2.imread(face)
        faceSwap.faceSwap(img)

def redrawAll(app, canvas):
    canvas.create_text(app.width/2, app.height/2, text = "Press C to swap face, ESC to quit.", font = 'Arial 14')

runApp(width = 300, height = 80)
