import pygame as pg
import Kierunek
import Plansza


class Snake:
    headUp = pg.image.load('Photos/Snake_Head/Head_Up.png').convert_alpha()
    headLeft = pg.image.load('Photos/Snake_Head/Head_Left.png').convert_alpha()
    headRight = pg.image.load('Photos/Snake_Head/Head_Right.png').convert_alpha()
    headDown = pg.image.load('Photos/Snake_Head/Head_Down.png').convert_alpha()
    middleHorizontal = pg.image.load('Photos/Snake_Body/Body_Horizontal.png').convert_alpha()
    middleVertical = pg.image.load('Photos/Snake_Body/Body_Vertical.png').convert_alpha()
    tailUp = pg.image.load('Photos/Snake_Tail/Tail_Up.png').convert_alpha()
    tailDown = pg.image.load('Photos/Snake_Tail/Tail_Down.png').convert_alpha()
    tailLeft = pg.image.load('Photos/Snake_Tail/Tail_Left.png').convert_alpha()
    tailRight = pg.image.load('Photos/Snake_Tail/Tail_Right.png').convert_alpha()

    # tego nie ruszać benkarty
    def draw(self, plansza):
        self.updateHeadGraphics()
        self.updateTailGraphics()
        for index, block in enumerate(self.cialo):
            x = block.x * Plansza.rozmiar
            y = block.y * Plansza.rozmiar
            rect = pg.Rect(x, y, Plansza.rozmiar, Plansza.rozmiar)
            if index == 0:
                screen.blit(self.head, rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, rect)
            else:
                prevoiusBlock = self.body[index + 1] - block
                nextBlock = self.body[index - 1] - block
                if prevoiusBlock.x == nextBlock.x:
                    screen.blit(Snake.middleVertical, rect)
                elif prevoiusBlock.y == nextBlock.y:
                    screen.blit(Snake.middleHorizontal, rect)
                else:
                    if prevoiusBlock.x == -1 and nextBlock.y == -1 or prevoiusBlock.y == -1 and nextBlock.x == -1:
                        screen.blit(Snake.turnRightDown, rect)
                    elif prevoiusBlock.x == -1 and nextBlock.y == 1 or prevoiusBlock.y == 1 and nextBlock.x == -1:
                        screen.blit(Snake.turnRightUp, rect)
                    elif prevoiusBlock.x == 1 and nextBlock.y == -1 or prevoiusBlock.y == -1 and nextBlock.x == 1:
                        screen.blit(Snake.turnLeftDown, rect)
                    elif prevoiusBlock.x == 1 and nextBlock.y == 1 or prevoiusBlock.y == 1 and nextBlock.x == 1:
                        screen.blit(Snake.turnLeftUp, rect)

    def updateHeadGraphics(self):
        head = self.cialo[1] - self.cialo[0]
        if head == punkt(1, 0):
            self.head = Snake.headRight
        elif head == punkt(-1, 0):
            self.head = Snake.headLeft
        elif head == punkt(0, 1):
            self.head = Snake.headDown
        elif head == punkt(0, -1):
            self.head = Snake.headUp

    def updateTailGraphics(self):
        tail = self.cialo[-2] - self.cialo[-1]
        if tail == punkt(1, 0):
            self.tail = Snake.tailLeft
        elif tail == punkt(-1, 0):
            self.tail = Snake.tailRight
        elif tail == punkt(0, 1):
            self.tail = Snake.tailUp
        elif tail == punkt(0, -1):
            self.tail = Snake.tailDown
    # do tego miejsca
