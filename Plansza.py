import pygame as pg
import sys
from pygame import Vector2

from Fruit import Fruit
from GG import main_game, SCREEN_UPDATE


class Plansza:
    clock = pg.time.Clock()
    screen = pg.display.set_mode((1024, 1024))
    fruit = Fruit(100,100)



    def __init__(self, rozmiar, ilosc):
        self.ilosc = ilosc
        self.rozmiar = rozmiar

    def draw(self, ekran):



        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    main_game.game_over()
                if event.type == SCREEN_UPDATE:
                    main_game.update()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        main_game.snake.direction = Vector2(0, -1)

                    if event.key == pg.K_DOWN:
                        main_game.snake.direction = Vector2(0, 1)

                    if event.key == pg.K_RIGHT:
                        main_game.snake.direction = Vector2(1, 0)

                    if event.key == pg.K_LEFT:
                        main_game.snake.direction = Vector2(-1, 0)
    screen.fill((175, 215, 70))
    fruit.draw(screen)
    pg.display.update()
    clock.tick(60)
    