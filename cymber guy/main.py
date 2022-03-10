
from data import *
import pygame as pg
import sys

pg.init()

#
# joystick=[]
# for i in range(pg.joystick.get_count()):
#     joystick.append(pg.joystick.Joystick(i))
#     joystick[-1].init()
#     print('Detected:',joystick[i].get_name())

#
while run:
    win.fill((0, 0, 0))
    userInput = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            pg.joystick.quit()

    if userInput[pg.K_ESCAPE]:
        sys.exit(0)

    if userInput[pg.K_w]:
        if not p1.player.colliderect(border_up):
            p1.player.y-=p1.move_speed
    if userInput[pg.K_s]:
        if not p1.player.colliderect(border_dwn):
            p1.player.y+=p1.move_speed
    if userInput[pg.K_a]:
        if not p1.player.colliderect(border_l):
            p1.player.x-=p1.move_speed
    if userInput[pg.K_d]:
        if not p1.player.colliderect(border_r):
            if not p1.player.colliderect(l1.line):
                p1.player.x+=p1.move_speed

    if userInput[pg.K_UP]:
        if not p2.player.colliderect(border_up):
            p2.player.y-=p2.move_speed
    if userInput[pg.K_DOWN]:
        if not p2.player.colliderect(border_dwn):
            p2.player.y+=p2.move_speed
    if userInput[pg.K_LEFT]:
        if not p2.player.colliderect(border_l):
            if not p2.player.colliderect(l1.line):
                p2.player.x-=p2.move_speed
    if userInput[pg.K_RIGHT]:
        if not p2.player.colliderect(border_r):
                p2.player.x+=p2.move_speed



#collisions
    if ball.ball.colliderect(border_up) or ball.ball.colliderect(border_dwn):
        ball.vel_y*=-1
        ball.ball.x += ball.vel_x
        ball.ball.y += ball.vel_y

    if ball.ball.colliderect(border_l) or ball.ball.colliderect(border_r):
        ball.vel_x*=-1
        ball.ball.x += ball.vel_x
        ball.ball.y += ball.vel_y
    # collide with player 1
    if ball.ball.colliderect(p1.player) and ball.ball.x>p1.player.x:
        ball.vel_x = abs(ball.vel_x)
        ball.vel_x+=ball.speed
        ball.ball.x += ball.vel_x*2
        ball.ball.y += ball.vel_y*2
    if ball.ball.colliderect(p1.player) and ball.ball.x < p1.player.x:
        ball.vel_x = abs(ball.vel_x)*-1
        ball.vel_x += ball.speed
        ball.ball.x += ball.vel_x
        ball.ball.y += ball.vel_y
    if ball.ball.colliderect(p1.player) and ball.ball.y > p1.player.y:
        ball.vel_y = abs(ball.vel_y)
        ball.vel_y += ball.speed
        ball.ball.x += ball.vel_x
        ball.ball.y += ball.vel_y
    if ball.ball.colliderect(p1.player) and ball.ball.y <= p1.player.y:
        ball.vel_y = abs(ball.vel_y)*-1
        ball.vel_y += ball.speed
        ball.ball.x += ball.vel_x
        ball.ball.y += ball.vel_y

    # collide with player 2
    if ball.ball.colliderect(p2.player) and ball.ball.x > p2.player.x:
        ball.vel_x = abs(ball.vel_x)
        ball.vel_x += ball.speed
        ball.ball.x -= ball.vel_x * 2
        ball.ball.y += ball.vel_y * 2
    if ball.ball.colliderect(p2.player) and ball.ball.x < p2.player.x:
        ball.vel_x = abs(ball.vel_x) * -1
        ball.vel_x -= ball.speed
        ball.ball.x += ball.vel_x
        ball.ball.y += ball.vel_y
    if ball.ball.colliderect(p2.player) and ball.ball.y > p2.player.y:
        ball.vel_y = abs(ball.vel_y)
        ball.vel_y += ball.speed
        ball.ball.x += ball.vel_x
        ball.ball.y += ball.vel_y
    if ball.ball.colliderect(p2.player) and ball.ball.y < p2.player.y:
        ball.vel_y = abs(ball.vel_y) * -1
        ball.vel_y += ball.speed
        ball.ball.x += ball.vel_x
        ball.ball.y += ball.vel_y
    if ball.vel_x>=35:
        ball.vel_x-=5
    if ball.vel_y>=35:
        ball.vel_y-=5

    #ball move
    ball.ball.x+=ball.vel_x
    ball.ball.y+=ball.vel_y
    #round end
    if ball.ball.colliderect(b1.border):
        ptk_2+=1
        p1.player.x=screen_x / 4 + (screen_x / 4) * 2 * 0 -p1.player_size/2
        p1.player.y= screen_y / 2 - p1.player_size / 2

        p2.player.x = screen_x / 4 + (screen_x / 4) * 2 * 1 - p1.player_size / 2
        p2.player.y = screen_y / 2 - p1.player_size / 2

        ball.ball.x=screen_x/2-ball.size/2
        ball.ball.y=screen_y/2-ball.size/2
        ball.vel_x=0
        ball.vel_y=0
    if ball.ball.colliderect(b2.border):
        ptk_1+=1
        p1.player.x=screen_x / 4 + (screen_x / 4) * 2 * 0 -p1.player_size/2
        p1.player.y= screen_y / 2 - p1.player_size / 2

        p2.player.x = screen_x / 4 + (screen_x / 4) * 2 * 1 - p1.player_size / 2
        p2.player.y = screen_y / 2 - p1.player_size / 2

        ball.ball.x=screen_x/2-ball.size/2
        ball.ball.y=screen_y/2-ball.size/2
        ball.vel_x=0
        ball.vel_y=0



    #drow
    l1.l_show()
    label_1 = my_font.render(str(ptk_1), False, gray)
    label_2 = my_font.render(str(ptk_2), False, gray)

    win.blit(label_1, (screen_x / 6, screen_y / 4))
    win.blit(label_2, (screen_x / 6 * 4, screen_y / 4))
    pg.draw.rect(win, 'gray', MAP[0])
    pg.draw.rect(win, 'gray', MAP[1])
    pg.draw.rect(win, 'gray', MAP[2])
    pg.draw.rect(win, 'gray', MAP[3])
    ball.ball_show()
    p1.p_show()
    b1.b_show()
    p2.p_show()
    b2.b_show()

    pg.time.delay(30)
    pg.display.update()