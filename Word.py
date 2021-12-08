import pygame
from Display import *


class Word:

    def __init__(self, pos, word):
        self.font = pygame.font.Font("Resources/Quinquefive-Ea6d4.ttf", 24)
        self.font_small = pygame.font.Font(
            "Resources/Quinquefive-Ea6d4.ttf", 12)
        self.pos = pos
        self.speed = [0, 0]
        self.accel = [0, -0.0001]
        self.word = word
        self.render_word = self.font.render(self.word, False, (0, 0, 0))
        self.correct = False
        self.removeable = False

    def loop(self, dt, curr_word):
        self.speed[0] += self.accel[0]
        self.speed[1] += self.accel[1]
        self.pos[0] += self.speed[0] * dt
        self.pos[1] += self.speed[1] * dt

        if self.word.upper() == curr_word.upper():
            self.correct = True
            self.render_word = self.font.render(self.word, False, (0, 255, 0))
        else:
            self.render_word = self.font.render(self.word, False, (0, 0, 0))

        if self.pos[1] < 32:
            self.removeable = True

    def draw(self):
        Display.SCREEN.blit(self.render_word, self.pos)
