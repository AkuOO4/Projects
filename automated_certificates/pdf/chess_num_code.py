from PIL import Image, ImageDraw, ImageFont
import pandas as pd
# import os
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
merger = PdfFileWriter()

# form_name = pd.read_excel('name.xlsx') #import the name file
i=0
file1 = PdfFileReader(open('chess.pdf', "rb"))
cordinate=(500,500)
for x in range (2):
    for y in range (2):
        i+=i
        im = Image.open("chess.jpg") #open the certificate file
        d = ImageDraw.Draw(im)
        location = (100*x, 100*y) #set location of the text
        text_color = (0, 0, 0) #set text color
        font = ImageFont.truetype("arial.ttf", 35) #set font + size

        d.text(cordinate, i, fill=text_color,font=font) #write text
        merger.addPage(im)
        outputStream = file("document-output.pdf", "wb")
        merger.write(outputStream)
        outputStream.close()
        # im.save("certificates/certificate_"+str(name[0])+".png") #save as pdf
        #merger.append()
        i+=1
        