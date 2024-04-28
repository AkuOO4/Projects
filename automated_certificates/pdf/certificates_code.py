from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

form_name = pd.read_excel('name.xlsx') #import the name file
i=0
for name in form_name.values:
    im = Image.open("download.jpg") #open the certificate file
    d = ImageDraw.Draw(im)
    location = (100, 100) #set location of the text
    text_color = (0, 0, 0) #set text color
    font = ImageFont.truetype("arial.ttf", 25) #set font + size
    d.text(location, name[0], fill=text_color,font=font) #write text
    im.save("certificates/certificate_"+str(name[0])+".png") #save as pdf
    
    i+=1