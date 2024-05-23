import pygame as pg


class Plansza:
    clock = pg.time.Clock()
    screen = pg.display.set_mode((1024, 1024))

    def __init__(self, rozmiar, ilosc):
        self.ilosc = ilosc
        self.rozmiar = rozmiar

    def draw(self, ekran):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
    