import argparse
import cv2
import pandas as pd
from utils.visualization import draw_function
from model.model import getColorName, color_detection
import numpy as np

#Creating argument parser to take image path from command line
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']

#Reading csv file with pandas and giving names to each column
index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

out = color_detection(img_path,[130,160,100,400])

r , g , b = 0 , 0 , 0
#Creating text string to display( Color name and RGB values )
text = getColorName(out[2],out[1],out[0],csv) + ' R='+ str(out[2]) +  ' G='+ str(out[1]) +  ' B='+ str(out[0])
print(text)
