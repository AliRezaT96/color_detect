import argparse
import cv2
import pandas as pd
from utils.visualization import draw_function
from model.model import getColorName
import numpy as np

#Creating argument parser to take image path from command line
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']

#Reading csv file with pandas and giving names to each column
index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

#Reading the image with opencv
img = cv2.imread(img_path)


color = ('b','g','r')
cl = []
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    cl.append(np.where(histr == max(histr))[0])
print(cl)

r , g , b = 0 , 0 , 0
#Creating text string to display( Color name and RGB values )
text = getColorName(cl[2],cl[1],cl[0],csv) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
print(text)
