#!/usr/bin/env python3

import pygame as pg
from pygame.locals import *
from go import Ball, Sled # игровые объекты


pg.init()
pg.mixer.init() #инициализация звуков

FPS  = 150
SIZE = width, height = 640, 480
BGCOLOR = 236, 238, 235

screen = pg.display.set_mode(SIZE)         # создаём окошко
clock  = pg.time.Clock()                   # создаем таймер

ball1 = Ball("ball.png", (50, 40), [3, 3])   # создаём мяч
ball2 = Ball("ball.png", (50, 20), [-3, 2])  # создаём мяч

sled = Sled("sled.png", (10, 0), [0, 0]) # создаём платформу

balls = pg.sprite.Group()
balls.add(ball1)
balls.add(ball2)


ping_sound = pg.mixer.music.load("ping.mp3") #загрузка звука шарика
score = 0


again = True
while again:
    for event in pg.event.get():
        if event.type == pg.QUIT: again = False
    
    # логика перемещения платформы
    pressed = pg.key.get_pressed() # вернем все зажатые клавиши
    if pressed[pg.K_UP]:
        sled.speed[1] = -2 if sled.rect.top >= 0 else 0
    elif pressed[pg.K_DOWN]:
        sled.speed[1] = 2 if sled.rect.bottom <= height else 0
    else: sled.speed[1] = 0

    # логика столкновения мяча1 с платформой
    if pg.sprite.collide_mask(ball1,sled) != None:
        pg.mixer.music.play()
        ball1.speed[0] = -ball1.speed[0]
        pg.time.delay(10)
        ball1.rect.left = ball1.rect.left+20


    # логика столкновения мяча2 с платформой
    if pg.sprite.collide_mask(ball2,sled) != None:
        pg.mixer.music.play()
        ball2.speed[0] = -ball2.speed[0]
        pg.time.delay(10)
        ball2.rect.left = ball2.rect.left+20

        

    # логика отскока мяча1 от границ экрана
    if ball1.rect.left < 0 or ball1.rect.right > width:
        ball1.speed[0] = -ball1.speed[0]
    if ball1.rect.top < 0 or ball1.rect.bottom > height:
        ball1.speed[1] = -ball1.speed[1]
    
    # логика отскока мяча2 от границ экрана
    if ball2.rect.left < 0 or ball2.rect.right > width:
        ball2.speed[0] = -ball2.speed[0]
    if ball2.rect.top < 0 or ball2.rect.bottom > height:
        ball2.speed[1] = -ball2.speed[1]
    
    sled.rect = sled.rect.move(sled.speed)    # сдвинуть прямоугольник платформы
    ball1.rect = ball1.rect.move(ball1.speed) # сдвинуть прямоугольник мяча
    ball2.rect = ball2.rect.move(ball2.speed) # сдвинуть прямоугольник мяча
    
    # отрисовка изображений
    screen.fill(BGCOLOR)
    screen.blit(sled.img, sled.rect)
    screen.blit(ball1.img, ball1.rect)
    screen.blit(ball2.img, ball2.rect)

    pg.display.update()
    clock.tick(FPS)

# выход из программы
pg.quit()
