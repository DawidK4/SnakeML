# import pygame, sys, random
# from pygame.math import Vector2
# class Fruit:
#
#     def __init__(self):
#        self.randomize()
#     def draw_fruit(self):
#         fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
#         #pygame.draw.rect(screen,(126,166,114),fruit_rect)
#         screen.blit(apple, fruit_rect)
#     def randomize(self):
#         self.x = random.randint(0, cell_number - 1)
#         self.y = random.randint(0, cell_number - 1)
#         self.pos = Vector2(self.x, self.y)
# class Main:
#     def __init__(self):
#         self.snake = Snake()
#         self.fruit = Fruit()
#     def update(self):
#         self.snake.move_snake()
#         self.check_collision()
#         self.check_fail()
#     def draw_elements(self):
#         self.fruit.draw_fruit()
#         self.snake.draw_snake()
#     def check_collision(self):
#         if self.snake.body[0] == self.fruit.pos:
#             self.fruit.randomize()
#             self.snake.add_block()
#     def check_fail(self):
#         if not 0 <= self.snake.body[0].x < cell_size:
#             self.game_over()
#         if not 0 <= self.snake.body[0].y < cell_size:
#             self.game_over()
#         for block in self.snake.body[1:]:
#             if block == self.snake.body[0]:
#                 self.game_over()
#     def game_over(self):
#         sys.exit()
#         pygame.quit()
#
#
# class Snake:
#
#     def __init__(self):
#         self.body = [Vector2(5, 10),Vector2(4, 10),Vector2(3, 10)]
#         self.direction = Vector2(1, 0)
#         self.new_block = False
#     def draw_snake(self):
#         for block in self.body:
#             block_react = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
#             pygame.draw.rect(screen, (183, 111, 122), block_react)
#
#     def move_snake(self):
#         if self.new_block:
#             body_copy = self.body[:]
#             body_copy.insert(0, body_copy[0] + self.direction)
#             self.body = body_copy[:]
#             self.new_block = False
#         else:
#             body_copy = self.body[:-1]
#             body_copy.insert(0, body_copy[0]+self.direction)
#             self.body = body_copy[:]
#
#     def add_block(self):
#         self.new_block = True
#
#
#
#
#
# pygame.init()
# cell_number = 16
# cell_size = 20
# screen = pygame.display.set_mode((cell_size*cell_size, cell_size*cell_size))
# clock = pygame.time.Clock()
# apple = pygame.image.load('Photos/apple.png').convert_alpha()
#
# SCREEN_UPDATE = pygame.USEREVENT
# pygame.time.set_timer(SCREEN_UPDATE, 150)
#
# main_game = Main()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             main_game.game_over()
#         if event.type == SCREEN_UPDATE:
#             main_game.update()
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP:
#                 main_game.snake.direction = Vector2(0, -1)
#
#             if event.key == pygame.K_DOWN:
#                 main_game.snake.direction = Vector2(0, 1)
#
#             if event.key == pygame.K_RIGHT:
#                 main_game.snake.direction = Vector2(1, 0)
#
#             if event.key == pygame.K_LEFT:
#                 main_game.snake.direction = Vector2(-1, 0)
#
#     screen.fill((175, 215, 70))
#     main_game.draw_elements()
#     pygame.display.update()
#     clock.tick(60)
#
import pygame
import sys
import random
from pygame.math import Vector2

class Fruit:
    def __init__(self, game):
        self.game = game
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * self.game.cell_size, self.pos.y * self.game.cell_size, self.game.cell_size, self.game.cell_size)
        self.game.screen.blit(self.game.apple, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, self.game.cell_number - 1)
        self.y = random.randint(0, self.game.cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class Snake:
    def __init__(self, game):
        self.game = game
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            block_rect = pygame.Rect(block.x * self.game.cell_size, block.y * self.game.cell_size, self.game.cell_size, self.game.cell_size)
            pygame.draw.rect(self.game.screen, (183, 111, 122), block_rect)

    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

class Main:
    def __init__(self, game):
        self.game = game
        self.snake = Snake(game)
        self.fruit = Fruit(game)

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.snake.body[0] == self.fruit.pos:
            self.fruit.randomize()
            self.snake.add_block()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < self.game.cell_number:
            self.game_over()
        if not 0 <= self.snake.body[0].y < self.game.cell_number:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()

class Gamee:
    def __init__(self):
        pygame.init()
        self.cell_number = 16
        self.cell_size = 20
        self.screen = pygame.display.set_mode((self.cell_size * self.cell_number, self.cell_size * self.cell_number))
        self.clock = pygame.time.Clock()
        self.apple = pygame.image.load('Photos/apple.png').convert_alpha()
        self.main_game = Main(self)

        self.SCREEN_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(self.SCREEN_UPDATE, 150)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.main_game.game_over()
                if event.type == self.SCREEN_UPDATE:
                    self.main_game.update()
                if event.type == pygame.KEYDOWN:
                    self.handle_key(event)

            self.screen.fill((175, 215, 70))
            self.main_game.draw_elements()
            pygame.display.update()
            self.clock.tick(60)

    def handle_key(self, event):
        if event.key == pygame.K_UP and self.main_game.snake.direction != Vector2(0, 1):
            self.main_game.snake.direction = Vector2(0, -1)
        if event.key == pygame.K_DOWN and self.main_game.snake.direction != Vector2(0, -1):
            self.main_game.snake.direction = Vector2(0, 1)
        if event.key == pygame.K_RIGHT and self.main_game.snake.direction != Vector2(-1, 0):
            self.main_game.snake.direction = Vector2(1, 0)
        if event.key == pygame.K_LEFT and self.main_game.snake.direction != Vector2(1, 0):
            self.main_game.snake.direction = Vector2(-1, 0)


gamee = Gamee()
gamee.run()

