import cv2
import numpy as np
import sys
import faceSwap
import random
import dlib


#write down all the TA faces
facesList = ["agermer.jpg", 
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

face = random.choice(facesList)
print(face)
img = cv2.imread(face)

faceSwap.faceSwap(img)
