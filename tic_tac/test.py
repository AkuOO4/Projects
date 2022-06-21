import pygame as py
WIDTH,HEIGHT=753,753
BLACK=(0,0,0)
WHITE=(255,255,255)
BLUE=(22,14,99)
RED=(254,39,18)
COLOR1=(150,200,200)

FPS=60
BOX_COLOR1=(0,128,128)
BOX_COLOR2=(0,179,179)

BORDER_THICKNESS=5
border_rect_1=py.Rect(250, 250, 250, 250)
border_rect_2=py.Rect(250, 250, 250, 250)

#circle
RADIUS=25
a1={"STATUS":-1,"x":0,"y":0}
WIN=py.display.set_mode((WIDTH,HEIGHT))
run=True
while run:
    py.draw.line(WIN,RED,[a1["x"]+150,a1["y"]+150],[a1["x"]+50+150,a1["y"]+50],BORDER_THICKNESS)
    py.draw.line(WIN,WHITE,[a1["x"]+50+50,a1["y"]+50+50],[a1["x"]+150,a1["y"]+50+250],BORDER_THICKNESS)
    py.draw.circle(WIN,WHITE,[300,300],RADIUS,BORDER_THICKNESS)
    py.display.update()
    for event in py.event.get():
            if event.type==py.QUIT:
                run = False

py.qiut()