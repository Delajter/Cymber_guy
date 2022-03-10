
import pygame as pg

#colors
gray=(90,90,90)
green=(0,255,0)
red=(255,0,0)
blue=(0,0,255)

#data
ptk_1=0
ptk_2=0
screen_x,screen_y=1920,1080
win = pg.display.set_mode((screen_x, screen_y))
run=True
pg.font.init()
my_font = pg.font.SysFont(pg.font.get_default_font(),1000)
MAP=[]

label_1 = my_font.render(str(ptk_1),False,gray)
label_2 = my_font.render(str(ptk_2),False,gray)
border_up = pg.Rect(0,0,screen_x,10)
border_dwn = pg.Rect(0,screen_y-10,screen_x,10)
border_l = pg.Rect(0,0,10,screen_y)
border_r = pg.Rect(screen_x-10,0,10,screen_y-10)
MAP.append(border_up)
MAP.append(border_dwn)
MAP.append(border_l)
MAP.append(border_r)

class User:
    def __init__(self,color_d,lp):

        self.color=color_d
        self.move_speed=35
        self.player_size=120
        pos_x = screen_x / 4 + (screen_x / 4) * 2 * lp -self.player_size/2
        pos_y = screen_y / 2-self.player_size/2
        self.player=pg.Rect((pos_x,pos_y),(self.player_size,self.player_size))

    def p_show(self):
        pg.draw.rect(win,self.color,self.player,self.player_size,self.player_size)

class ShotPlace:
    def __init__(self,place_x,color_d):
        self.color=color_d
        self.w_size=10
        self.h_size=screen_y/4
        self.border=pg.Rect((place_x-self.w_size),(screen_y/2-self.h_size/2),self.w_size,self.h_size)
    def b_show(self):
        pg.draw.rect(win,self.color,self.border)


class ShotLine:
    def __init__(self,color_d):
        self.color=color_d
        self.pos_y = 0
        self.w = 20
        self.pos_x=int(screen_x/2-self.w/2)
        self.h=screen_y
        self.line=pg.Rect(self.pos_x,self.pos_y,self.w,self.h)

    def l_show(self):
        pg.draw.rect(win, self.color, self.line)


class Ball:
    def __init__(self,color_d):
        self.color=color_d
        self.size=60
        self.speed=5
        self.vel_y=0
        self.vel_x=0
        self.ball=pg.Rect(screen_x/2-self.size/2,screen_y/2-self.size/2,self.size,self.size)
    def ball_show(self):
        pg.draw.rect(win,self.color,self.ball,self.size,self.size)



#declarate
l1=ShotLine(red)
ball=Ball(blue)
p1=User(green,0)
b1=ShotPlace(10,green)
p2=User(blue,1)
b2=ShotPlace(screen_x,blue)
