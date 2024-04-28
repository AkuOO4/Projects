from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

i=0
location=(500,500)
# form_name = pd.read_excel('name.xlsx') #import the name file
for x in range(1,3):
    for y in range(1,3):
        i+=1
        im = Image.open("chess.jpg") #open the certificate file
        d = ImageDraw.Draw(im)
        # location = (100*x, 100*y) #set location of the text
        text_color = (0, 0, 0) #set text color
        font = ImageFont.truetype("arial.ttf", 250) #set font + size

        d.text(location, str(i), fill=text_color,font=font) #write text
        im.save("chess/chessnumwer"+str(i)+".png") #save as pdf
        
       