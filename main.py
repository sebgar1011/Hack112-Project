import cv2
import numpy as np
import sys
import faceSwap
import random
import dlib
from cmu_112_graphics import *


# Initialize TA image files
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

# Swap face
def swap(app):
    img = cv2.imread('photos/' + app.face)
    faceSwap.faceSwap(img)

# Print out the correct staff name
def guessStaff(app):
    staffDict = {"agermer.jpg": 'amy', 
                "ahunter2.jpg": 'allison',
                "alanhsu.jpg": 'alan', 
                "alexx.jpg": 'alex', 
                "andrewh1.jpg": 'andrew',
                "anitama.jpg": 'anita',
                "asadalis.jpg": 'asad',
                "athontak.jpg": 'anjali',
                "bradleyz.jpg": 'bradley',
                "bsidwell.jpg": 'brittney',
                "crystal3.jpg": 'crystal',
                "drazek.jpg": 'dina',
                "dsyou.jpg": 'david',
                "eharllee.jpg": 'elena',
                "ejzhang.jpg": 'emily',
                "eswecker.jpg": 'elena',
                "ezm.jpg": 'eliza',
                "gcui.jpg": 'grace',
                "haeunk.jpg": 'grace',
                "hpnguyen.jpg": 'phi',
                "ijaffer.jpg": 'ishaan',
                "jledon.jpg": 'jason',
                "jritze.jpg": 'joe',
                "jzych.jpg": 'jake',
                "katheriy.jpg": 'katherine',
                "kbalenza.jpg": 'kyra',
                "kecooper.jpg": 'kaitlynn',
                "knassre.jpg": 'kian',
                "lnicolus.jpg": 'leo',
                "lsands.jpg": 'lauren',
                "mbairath.jpg": 'mihika',
                "mdunaevs.jpg": 'max',
                "mling2.jpg": 'michelle',
                "mmookerj.jpg": 'mira',
                "npadmana.jpg": 'namrata',
                "ntedesch.jpg": 'natalie',
                "pbhuang.jpg": 'patrick',
                "pingyac.jpg": 'ping-ya',
                "pokade.jpg": 'prithvi',
                "rjogleka.jpg": 'rahul',
                "rmanley.jpg": 'rebecca',
                "saralian.jpg": 'sara',
                "shivankj.jpg": 'shivank',
                "skylarm.jpg": 'skylar',
                "ssagiraj.jpg": 'sai',
                "stevenl2.jpg": 'steven',
                "tmauzy.jpg": 'tate',
                "tyf.jpg": 'terry',
                "vbeaudoi.jpg": 'vivian',
                "yizes.jpg": 'sean',
                'taylor.jpg': 'taylor',
                'koz.png': 'kosbie'}
    staffName = staffDict[app.face]
    print(staffName)

# Swap face when key pressed
def keyPressed(app, event):

    #TA Swap
    if event.key == 's':
        app.face = random.choice(app.facesList)
        swap(app)
        guessStaff(app)
    
    #Taylor Swap
    elif event.key == 't':
        app.face = 'taylor.jpg'
        swap(app)
        guessStaff(app)
    
    
    #Koz Swap
    elif event.key == 'k':
        app.face = 'koz.png'
        swap(app)
        guessStaff(app)        

# Display instructions
def redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill = "light blue")
    canvas.create_text(app.width/2, app.height/2 - 25, text = "Press S to swap with a random TA's face,", font = 'Arial 20')
    canvas.create_text(app.width/2, app.height/2, text = "K for Prof Kozbie's face,", font = 'Arial 20')
    canvas.create_text(app.width/2, app.height/2 + 25, text = "T for Prof Taylor's face, ESC to quit.", font = 'Arial 20')

runApp(width = 500, height = 200)
