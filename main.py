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

TAface =  random.choice(facesList)
kozFace = "koz.png"


#if open mouth: distance between point 63 and 67 > threshold,
#change to random TA face
'''
if _________:
    img = cv2.imread(TAface)
'''
