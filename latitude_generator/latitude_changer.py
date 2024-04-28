#from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
import random as rand

X=[]
Y=[]
SOURCE=[10.023286, 76.311371]

sheet = pd.ExcelWriter('cordinates.xlsx') #import the name file

for i in range(500):
    if i//rand.randint(3)==0:
        x=SOURCE[0]+float(rand.randrange(1000)/10000)
        y=SOURCE[1]-float(rand.randrange(1000)/10000)
        X.append(x)
        Y.append(y)

    else:
        x=SOURCE[0]+float(rand.randrange(0,100)/100000)
        y=SOURCE[1]-float(rand.randint(0,100)/10000)
        X.append(x)
        Y.append(y)

df = pd.DataFrame({'x':X,'y':Y})
df.to_csv('cordinates.csv',index=False)
df.to_excel(sheet,'Sheet1',index=False)
sheet.save()

