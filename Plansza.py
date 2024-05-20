import pygame as pg


class Plansza:
    def __init__(self, szerokosc, wysokosc, rozmiar):
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.rozmiar = rozmiar

    def rysuj(self, ekran):
        for x in range(0, self.szerokosc):
            for y in range(0, self.wysokosc):
                pg.draw.rect(ekran, (255, 255, 255),
                             pg.Rect(x * self.rozmiar, y * self.rozmiar, self.rozmiar, self.rozmiar))
