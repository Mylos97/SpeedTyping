import pygame
import math

from pygame.constants import KEYDOWN
from Display import *


class TextInput:
    OFFSET = 8

    def __init__(self, check_words):
        self.font = pygame.font.Font("Resources/Quinquefive-Ea6d4.ttf", 64)
        self.rect = pygame.Rect(0, 0, 840, 20)
        self.outer_box = pygame.Surface(
            (Display.WINDOW_SIZE[0], Display.WINDOW_SIZE[1]/6.5))
        self.outer_box.fill((0, 0, 0))
        self.inner_box = pygame.Surface(
            (Display.WINDOW_SIZE[0] - TextInput.OFFSET*2, (Display.WINDOW_SIZE[1]/6.5) - TextInput.OFFSET*2))
        self.inner_box.fill((255, 255, 255))
        self.current_word = ''
        self.check_words = check_words
        self.alphabet = 'abcdefghijklmnopqrstuvwxyzæøå'

    def loop(self, dt):
        self.render_word = self.font.render(
            self.current_word, False, (0, 0, 0))

    def handle_event(self, event):

        if event.type == pygame.KEYDOWN:
            if event.unicode == '\x08':
                self.current_word = self.current_word[:-1]
            elif event.unicode == '\r':
                self.check_words()
                self.current_word = ''
            elif event.unicode == ' ':
                self.check_words()
                self.current_word = ''
            elif event.unicode in self.alphabet:
                self.current_word += event.unicode
            print(event)

    def draw(self):
        Display.SCREEN.blit(self.outer_box, (0, 0))
        Display.SCREEN.blit(
            self.inner_box, (TextInput.OFFSET, TextInput.OFFSET))
        Display.SCREEN.blit(
            self.render_word, ((TextInput.OFFSET*2, TextInput.OFFSET*2)))

    def get_current_word(self):
        return self.current_word.upper()
