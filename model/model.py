import cv2
import numpy as np
import pandas as pd

#function to calculate minimum distance from all colors and get the most matching color
def getColorName(R,G,B,csv):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname

def color_detection(img_path,bbox):
    img = cv2.imread(img_path)
    cropped_image = img[bbox[0]:bbox[1], bbox[2]:bbox[3]]
    colors = ('b','g','r')
    out = []
    for i,col in enumerate(colors):
        histr = cv2.calcHist([cropped_image],[i],None,[256],[0,256])
        out.append(np.where(histr == max(histr))[0])
    return out


