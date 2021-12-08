import pygame
from Display import *


class ScoreBoard:

    def __init__(self):
        self.font = pygame.font.Font("Resources/Quinquefive-Ea6d4.ttf", 32)
        self.score = 0
        self.words_per_minute = []
        self.update_timer = 0
        self.seconds = 0
        self.words_per_minute_scalar = 10
        self.words_per_minute_title = self.font.render(
            'WPM:', False, (0, 0, 0))
        self.words_per_minute_render = self.font.render(
            '0', False, (0, 0, 0))
        self.score_render = self.font.render(str(self.score), False, (0, 0, 0))
        self.score_title = self.font.render('Score:', False, (0, 0, 0))
        self.health = 1
        self.health_green_img = pygame.Surface((
            Display.WINDOW_SIZE[0], 6))
        self.health_green_img.fill((0, 255, 0))

    def increment_score(self):
        self.score += 1
        self.score_render = self.font.render(str(self.score), False, (0, 0, 0))
        self.words_per_minute.append({'seconds': self.seconds})

    def decrease_score(self):
        if self.score > 0:
            self.score -= 1
        self.score_render = self.font.render(str(self.score), False, (0, 0, 0))

    def decrease_health(self):
        self.health -= 0.1
        self.health_green_img = pygame.Surface((
            Display.WINDOW_SIZE[0]*self.health, 6))
        color = ((0, 255, 0))
        if self.health < 0.4:
            color = (255, 255, 0)
        if self.health < 0.2:
            color = (255, 0, 0)

        self.health_green_img.fill(color)

    def draw(self):
        Display.SCREEN.blit(self.words_per_minute_title,
                            (Display.WINDOW_SIZE[0]/44, Display.WINDOW_SIZE[1]/6))
        Display.SCREEN.blit(self.words_per_minute_render,
                            (Display.WINDOW_SIZE[0]/6, Display.WINDOW_SIZE[1]/6))
        Display.SCREEN.blit(
            self.score_render, (Display.WINDOW_SIZE[0]*0.92, Display.WINDOW_SIZE[1]/6))
        Display.SCREEN.blit(
            self.score_title, (Display.WINDOW_SIZE[0]*0.70, Display.WINDOW_SIZE[1]/6))
        Display.SCREEN.blit(self.health_green_img,
                            (0, Display.WINDOW_SIZE[1]/6.5))

    def loop(self):
        self.update_timer += 1

        if self.update_timer > 60:
            self.update_timer = 0
            self.seconds += 1

            for sec in self.words_per_minute:
                if sec['seconds'] < self.seconds - self.words_per_minute_scalar:
                    self.words_per_minute.remove(sec)
            self.words_per_minute_render = self.font.render(
                str(len(self.words_per_minute * 6)), False, (0, 0, 0))
