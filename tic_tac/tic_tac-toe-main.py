from time import time
import pygame as py

py.font.init()

#pygame constants
WIDTH,HEIGHT=753,753  #each indivdual box should be 250x250
TEXT_CENTER=(380,300)
BLACK=(0,0,0)
WHITE=(255,255,255)
BLUE=(69, 123, 157)
NAVY_BLUE=(29, 53, 87)
RED=(230, 57, 70)
COLOR1=(150,200,200)

FPS=60
BOX_COLOR1=(168, 218, 220)
BOX_COLOR2=(241, 250, 238)

BORDER_THICKNESS=5
border_rect_1=py.Rect(250, 250, 250, 250)
border_rect_2=py.Rect(250, 250, 250, 250)
POP_UP_RECT=py.Rect(240,240,260,260)

#circle
RADIUS=75

font1=py.font.SysFont('freesanbold.ttf',80)
font2 = py.font.SysFont('freesanbold.ttf', 10)

WIN=py.display.set_mode((WIDTH,HEIGHT))
py.display.set_caption("TIC_TAC_TOE")

#LOGIC CONSTANTS
a1={"STATUS":-1,"x":0,"y":0}
a2={"STATUS":-1,"x":0,"y":250}
a3={"STATUS":-1,"x":0,"y":500}
b1={"STATUS":-1,"x":250,"y":0}
b2={"STATUS":-1,"x":250,"y":250}
b3={"STATUS":-1,"x":250,"y":500}
c1={"STATUS":-1,"x":500,"y":0}
c2={"STATUS":-1,"x":500,"y":250}
c3={"STATUS":-1,"x":500,"y":500}
values=[a1,a2,a3,b1,b2,b3,c1,c2,c3]

X=py.image.load('x.png')
X=py.transform.scale(X,(250,250))
REFRESH_IMG=py.image.load('refresh1.jpg')
REFRESH_IMG=py.transform.scale(REFRESH_IMG,(75,75))

def mini_box(color,x,y):
    LENGTH=250
    rectangle=py.Rect(x,y,LENGTH,LENGTH)
    py.draw.rect(WIN,color,rectangle)
    

def draw_all_boxes():
    ct1=0

    for x in range (0,750,250):
        
        for y in range(0,750,250):
            for i in values:
                if i['STATUS']==-1 and (i['x']==x and i['y']==y): 
                    if ct1%2==0:
                        mini_box(BOX_COLOR1,x,y)
                    else:
                        mini_box(BOX_COLOR2,y,x)
                    
                elif i['STATUS']==1 and (i['x']==x and i['y']==y):
                    WIN.blit(X,(x,y))
                elif i['STATUS']==0 and (i['x']==x and i['y']==y):
                    py.draw.circle(WIN,BLACK,[x+125,y+125],RADIUS,BORDER_THICKNESS+10)
            ct1+=1
    win_draw_popup(win_check())         
    print(values)                          
    py.display.update()
            
def moving_rect(keys_pressed):
    #global border_rect
    #mini_box(BOX_COLOR1,border_rect.x,border_rect.y)
    draw_all_boxes()
    print(border_rect_1.x,border_rect_1.y)
    if keys_pressed[py.K_DOWN]:
        
        border_rect_1.y+=250
        
        if border_rect_1.y>750:
            border_rect_1.y=0
        #border_rect.move(0,250)
        #py.draw.rect(WIN,BLUE ,border_rect,BORDER_THICKNESS )#((rgb),[cordinates],katti)
        
    if keys_pressed[py.K_UP]:
        border_rect_1.y-=250
        if border_rect_1.y<0:
            border_rect_1.y=500
        #py.draw.rect(WIN,BLUE,border_rect,BORDER_THICKNESS )#((rgb),[cordinates],katti)
        
    if keys_pressed[py.K_RIGHT]:
        border_rect_1.x+=250
        if border_rect_1.x>750:
            border_rect_1.x=0
            
        #py.draw.rect(WIN,BLUE,border_rect,BORDER_THICKNESS )#((rgb),[cordinates],katti)
        
    if keys_pressed[py.K_LEFT]:
        border_rect_1.x-=250
        if border_rect_1.x<0:
            border_rect_1.x=500
        #py.draw.rect(WIN,BLUE,border_rect,BORDER_THICKNESS )#((rgb),[cordinates],katti)
    #if keys_pressed[py.K_DOWN] or keys_pressed[py.K_UP] or keys_pressed[py.K_RIGHT] or keys_pressed[py.K_LEFT]:
    py.draw.rect(WIN,BLUE ,border_rect_1,BORDER_THICKNESS )
    
    py.display.update()

def player_1_moves(x,y):
   global a1,a2,a3,b1,b2,b3,c1,c2,c3,values
   if ((x==0) and (y==0)) and (a1["STATUS"]==-1):
       
       a1["STATUS"]=1
   if ((x==0) and (y==250)) and (a2["STATUS"]==-1):       
        a2["STATUS"]=1
       
   if ((x==0) and (y ==500)) and (a3["STATUS"]==-1):
        a3["STATUS"]=1
       
   if ((x==250) and (y==0)) and (b1["STATUS"]==-1):
        b1["STATUS"]=1
       
   if ((x ==250) and (y ==250)) and (b2["STATUS"]==-1):
        b2["STATUS"]=1
        
   if ((x ==250) and (y==500)) and (b3["STATUS"]==-1):
        b3["STATUS"]=1
       
   if ((x==500) and (y ==0)) and (c1["STATUS"]==-1):
        c1["STATUS"]=1
        
   if ((x==500) and (y==250)) and (c2["STATUS"]==-1):
        c2["STATUS"]=1

   if ((x==500) and (y==500)) and (c3["STATUS"]==-1):
        c3["STATUS"]=1
   values=[a1,a2,a3,b1,b2,b3,c1,c2,c3]
   py.display.update()
   
    


def player_2_moves(x,y):
   global a1,a2,a3,b1,b2,b3,c1,c2,c3,values
   if ((x==0) and (y==0)) and (a1["STATUS"]==-1):
       #py.draw.circle(WIN,BLACK,[a1["x"]+125,a1["y"]+125],RADIUS,BORDER_THICKNESS+10)
       a1["STATUS"]=0
   if ((x==0) and (y==250)) and (a2["STATUS"]==-1):       
        a2["STATUS"]=0
        #py.draw.circle(WIN,BLACK,[a2["x"]+125,a2["y"]+125],RADIUS,BORDER_THICKNESS+10)
   if ((x==0) and (y ==500)) and (a3["STATUS"]==-1):
        a3["STATUS"]=0
        #py.draw.circle(WIN,BLACK,[a3["x"]+125,a3["y"]+125],RADIUS,BORDER_THICKNESS+10)
   if ((x==250) and (y==0)) and (b1["STATUS"]==-1):
        b1["STATUS"]=0
        #py.draw.circle(WIN,BLACK,[b1["x"]+125,b1["y"]+125],RADIUS,BORDER_THICKNESS+10)
   if ((x ==250) and (y ==250)) and (b2["STATUS"]==-1):
        b2["STATUS"]=0
        #py.draw.circle(WIN,BLACK,[b2["x"]+125,b2["y"]+125],RADIUS,BORDER_THICKNESS+10)
   if ((x ==250) and (y==500)) and (b3["STATUS"]==-1):
        b3["STATUS"]=0
        #py.draw.circle(WIN,BLACK,[b3["x"]+125,b3["y"]+125],RADIUS,BORDER_THICKNESS+10)
   if ((x==500) and (y ==0)) and (c1["STATUS"]==-1):
        c1["STATUS"]=0
        #py.draw.circle(WIN,BLACK,[c1["x"]+125,c1["y"]+125],RADIUS,BORDER_THICKNESS+10)
   if ((x==500) and (y==250)) and (c2["STATUS"]==-1):
        c2["STATUS"]=0
        #py.draw.circle(WIN,BLACK,[c2["x"]+125,c2["y"]+125],RADIUS,BORDER_THICKNESS+10)
   if ((x==500) and (y==500)) and (c3["STATUS"]==-1):
        c3["STATUS"]=0
        #py.draw.circle(WIN,BLACK,[c3["x"]+125,c3["y"]+125],RADIUS,BORDER_THICKNESS+10)
   values=[a1,a2,a3,b1,b2,b3,c1,c2,c3]
   py.display.update()

def win_check(): #return 1 if X wins, 0 if O wins, 2 if draw, -1 if nothing happens
    win_lose=-1
    #checking if player1 wins by looking all the possibilities of winning(k)
    if (a1['STATUS']==1 and a2['STATUS']==1 and a3['STATUS']==1)  or  (b1['STATUS']==1 and b2["STATUS"]==1 and b3["STATUS"]==1) or (c1['STATUS']==1 and c2['STATUS']==1 and c3["STATUS"]==1) or (a1['STATUS']==1 and b1['STATUS']==1 and c1['STATUS']==1) or (a2['STATUS']==1 and b2["STATUS"]==1 and c2['STATUS']==1) or (a3['STATUS']==1 and c3['STATUS']==1 and b3==1) or (a1['STATUS']==1 and b2["STATUS"]==1 and c3['STATUS']==1) or (a3['STATUS']==1 and b2["STATUS"]==1 and c1['STATUS']==1):
        print("palyer 1 won")
        win_lose=1
        print()
        
    elif (a1['STATUS']==0 and a2['STATUS']==0 and a3['STATUS']==0) or (b1['STATUS']==0 and b2["STATUS"]==0 and b3['STATUS']==0) or (c1['STATUS']==0 and c2['STATUS']==0 and c3['STATUS']==0) or (a1['STATUS']==0 and b1['STATUS']==0 and c1['STATUS']==0) or (a2['STATUS']==0 and b2["STATUS"]==0 and c2['STATUS']==0) or (a3['STATUS']==0 and c3['STATUS']==0 and b3["STATUS"]==0) or (a1['STATUS']==0 and b2["STATUS"]==0 and c3['STATUS']==0) or (a3['STATUS']==0 and b2["STATUS"]==0 and c1['STATUS']==0):
        print ("player 2 won")
        win_lose=0
        print()
          
    elif a1['STATUS']!=-1 and a2['STATUS']!=-1 and a3['STATUS']!=-1 and b1['STATUS']!=-1 and b2['STATUS']!=-1 and b2['STATUS']!=-1 and b3['STATUS']!=-1 and c1['STATUS']!=-1 and c2['STATUS']!=-1 and c3['STATUS']!=-1: 
        win_lose=2
        
    win_draw_popup(win_lose)
    return win_lose
def win_draw_popup(a):

    if a==0 or a==1 or a==2:
        # Render the texts that you want to display
        py.draw.rect(WIN,NAVY_BLUE,POP_UP_RECT)
        if a==0:
            text1 = font1.render('0 WON ', 1, RED)
            textRect1 = text1.get_rect()
            textRect1.center = TEXT_CENTER
            WIN.blit(text1,textRect1)
        elif a==1:
            text1 = font1.render('X WON ', 1, RED)
            textRect1 = text1.get_rect()
            textRect1.center = TEXT_CENTER
            WIN.blit(text1,textRect1)
        elif a==2:
            text1 = font1.render('GAME IS DRAW ',  1, RED)
            textRect1 = text1.get_rect()
            textRect1.center = TEXT_CENTER
            WIN.blit(text1,textRect1)
            

        #WIN.blit(REFRESH_IMG,(350,380))
        if py.MOUSEBUTTONDOWN:
            pos=py.mouse.get_pos()
            if (POP_UP_RECT.x<= pos[0] <=POP_UP_RECT.x+POP_UP_RECT.width) and (POP_UP_RECT.y<=pos[1]<=POP_UP_RECT.y+POP_UP_RECT.height):
                py.time.delay(500)
                new_game()

def new_game():
    global a1,a2,a3,b1,b2,b3,c1,c2,c3,values
    a1["STATUS"],a2["STATUS"],a3["STATUS"],b1["STATUS"],b2["STATUS"],b3["STATUS"],c1["STATUS"],c2["STATUS"],c3["STATUS"]=-1,-1,-1,-1,-1,-1,-1,-1,-1
    values=[a1,a2,a3,b1,b2,b3,c1,c2,c3]


def draw_window():
    WIN.fill(WHITE)       
    draw_all_boxes()
    py.draw.rect(WIN,BLUE ,border_rect_1,BORDER_THICKNESS )#((rgb),[cordinates],katti)
    
    py.display.update()

def main():
    turn=1
    clock = py.time.Clock()
    clock.tick(FPS)
    run=True
    draw_window()
    while run:
        
        for event in py.event.get():
            if event.type==py.QUIT:
                run = False 
             
            if event.type==py.KEYDOWN:
                
                if event.key==py.K_TAB:
                        if turn==1:
                            print()
                            player_1_moves(border_rect_1.x,border_rect_1.y)
                            win_check()
                            turn=0
                        elif turn==0:
                            player_2_moves(border_rect_1.x,border_rect_1.y) 
                            win_check()
                            turn=1
            keys_pressed=py.key.get_pressed()
            moving_rect(keys_pressed)
    py.quit()

if __name__=="__main__":
    main()