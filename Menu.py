import pygame
from Display import *
from StateHandler import *
from GameState import *


class Menu:

    def __init__(self):
        self.font = pygame.font.Font("Resources/Quinquefive-Ea6d4.ttf", 64)

        self.title = self.font.render('SPEED TYPER', False, (0, 0, 0))
        self.start_text = self.font.render('START', False, (0, 0, 0))
        self.difficulty_text = self.font.render('DIFFICULTY', False, (0, 0, 0))
        self.difficulties = ['EASY', 'MEDIUM', 'HARD']
        self.quit_text = self.font.render('QUIT', False, (0, 0, 0))
        self.selected = 0

    def draw(self):
        Display.SCREEN.blit(
            self.title, [Display.WINDOW_SIZE[0]/10, Display.WINDOW_SIZE[1]*0.1])
        Display.SCREEN.blit(
            self.start_text, [Display.WINDOW_SIZE[0]/10, Display.WINDOW_SIZE[1]*0.4])
        Display.SCREEN.blit(self.difficulty_text, [
                            Display.WINDOW_SIZE[0]/10, Display.WINDOW_SIZE[1]*0.6])
        Display.SCREEN.blit(self.quit_text, [
                            Display.WINDOW_SIZE[0]/10, Display.WINDOW_SIZE[1]*0.8])

    def loop(self, event):
        if event.type == pygame.KEYDOWN:
            print(event)
            if event.scancode == 79:
                print('rigjt')
            if event.scancode == 82:
                self.selected -= 1
                if self.selected < 0:
                    self.selected = 2
            if event.scancode == 80:
                print('left')
            if event.scancode == 81:
                self.selected += 1
                if self.selected > 2:
                    self.selected = 0
            if event.scancode == 40:
                if self.selected == 0:
                    StateHandler.STATE = GameState.STATE_GAME

                if self.selected == 2:
                    pygame.quit()

        if self.selected == 0:
            self.start_text = self.font.render(
                'START', False, (100, 100, 100))
        else:
            self.start_text = self.font.render('START', False, (0, 0, 0))
        if self.selected == 1:
            self.difficulty_text = self.font.render(
                'DIFFICULTY', False, (100, 100, 100))
        else:
            self.difficulty_text = self.font.render(
                'DIFFICULTY', False, (0, 0, 0))
        if self.selected == 2:
            self.quit_text = self.font.render(
                'QUIT', False, (100, 100, 100))
        else:
            self.quit_text = self.font.render(
                'QUIT', False, (0, 0, 0))
