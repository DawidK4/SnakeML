import pygame as pg

import Plansza


class Button:
    def __init__(self, color, x, y, text='', path=''):
        self.color = color
        self.x = x
        self.y = y
        self.text = text
        self.width = 200
        self.height = 50
        self.image = pg.image.load(path)

    def draw(self, screen, ):
        screen.blit(self.image, (self.x, self.y))

    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False


class ScoreBoard:
    exit_button = Button((0, 255, 0), 800, 100, 'Exit', 'Photos/Buttons/ExitButton.png')
    working = True
    scroll = 0
    image = pg.image.load('Photos/scoreBoardImage.jpg')
    def __init__(self, screen):
        self.scores = []
        self.screen = screen
        pg.font.init()
        self.font = pg.font.SysFont('arial', 40)

    def add_score(self, score):
        self.scores.append(score)

    def display(self):
        self.working = True
        self.screen.blit(self.image, (0, 0))
        for i, score in enumerate(self.scores):
            text = self.font.render(f'Score {i + 1}: {score}', True, (255, 255, 255))
            textHS = self.font.render(f'Generation: {self.scores.__len__()}', True, (255, 255, 255))
            self.screen.blit(textHS, (800, 50))
            self.screen.blit(text, (50, 50 + i * 30 - self.scroll))
        self.exit_button.draw(self.screen)
        pg.display.flip()
        self.scoreboard()

    def scoreboard(self):
        while self.working:
            for event in pg.event.get():
                pos = pg.mouse.get_pos()
                if event.type == pg.QUIT:
                    self.working = False
                    Menu().display()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.exit_button.is_over(pos):
                        print('clicked the exit button')
                        self.working = False
                        Menu().display()
                if event.type == pg.MOUSEWHEEL:
                    self.scroll += event.y * 30
                    self.display()
            pg.display.update()


class Menu:
    pg.display.set_caption('Snake AI')
    screen = pg.display.set_mode((1024, 1024))
    working = True
    clock = pg.time.Clock()
    image = pg.image.load('Photos/menuImage.jpg')
    start_button = Button((255, 5, 5), 450, 950, 'Start', 'Photos/Buttons/StartButton.png')
    exit_button = Button((0, 255, 0), 10, 950, 'Exit', 'Photos/Buttons/ExitButton.png')
    scoreboard_button = Button((0, 255, 0), 800, 950, 'Score Board', 'Photos/Buttons/ScoreBoardButton.png')
    scoreboard = ScoreBoard(screen)

    def __init__(self):
        pg.init()
        self.screen.blit(self.image, (0, 0))
        self.start_button.draw(self.screen)
        self.exit_button.draw(self.screen)
        self.scoreboard_button.draw(self.screen)
        pg.display.flip()

    def menu(self):
        while self.working:
            for event in pg.event.get():
                pos = pg.mouse.get_pos()
                if event.type == pg.QUIT:
                    self.working = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.start_button.is_over(pos):
                        Plansza.Plansza(20, 20, 60).draw(self.screen)
                        print('clicked the start button')
                    if self.exit_button.is_over(pos):
                        print('clicked the exit button')
                        self.working = False
                    if self.scoreboard_button.is_over(pos):
                        self.scoreboard.add_score(100)
                        self.scoreboard.add_score(200)
                        self.scoreboard.add_score(300)
                        print('clicked the scoreboard button')
                        self.scoreboard.display()
            pg.display.update()

    def display(self):
        self.screen.blit(self.image, (0, 0))
        self.start_button.draw(self.screen)
        self.exit_button.draw(self.screen)
        self.scoreboard_button.draw(self.screen)
        pg.display.flip()
