import pygame
from Display import *
from StateHandler import *
from GameState import *


class Menu:

    def __init__(self):
        self.big_font = pygame.font.Font("Resources/Quinquefive-Ea6d4.ttf", 64)
        self.small_font = pygame.font.Font(
            "Resources/Quinquefive-Ea6d4.ttf", 48)
        self.diff_font = pygame.font.Font(
            "Resources/Quinquefive-Ea6d4.ttf", 32)

        self.title = self.big_font.render('SPEED TYPER', False, (0, 0, 0))
        self.start_text = self.small_font.render('START', False, (0, 0, 0))
        self.difficulty_text = self.small_font.render(
            'DIFFICULTY', False, (0, 0, 0))
        self.difficulties = ['EASY', 'MEDIUM', 'HARD']
        self.selected_difficulty = self.diff_font.render(
            'EASY', False, (0, 0, 0))
        self.quit_text = self.small_font.render('QUIT', False, (0, 0, 0))
        self.selected = 0
        self.diff_select = 0

    def draw(self):
        Display.SCREEN.blit(
            self.title, [Display.WINDOW_SIZE[0]/10, Display.WINDOW_SIZE[1]*0.1])
        Display.SCREEN.blit(
            self.start_text, [Display.WINDOW_SIZE[0]/10, Display.WINDOW_SIZE[1]*0.4])
        Display.SCREEN.blit(self.difficulty_text, [
                            Display.WINDOW_SIZE[0]/10, Display.WINDOW_SIZE[1]*0.6])
        Display.SCREEN.blit(self.quit_text, [
                            Display.WINDOW_SIZE[0]/10, Display.WINDOW_SIZE[1]*0.8])
        Display.SCREEN.blit(self.selected_difficulty, [
                            Display.WINDOW_SIZE[0]*0.75, Display.WINDOW_SIZE[1]*0.6])

    def loop(self, event):
        if event.type == pygame.KEYDOWN:
            if event.scancode == 79:
                if self.selected == 1:
                    self.diff_select += 1
                    if self.diff_select > len(self.difficulties) - 1:
                        self.diff_select = 0

            if event.scancode == 82:
                self.selected -= 1
                if self.selected < 0:
                    self.selected = 2

            if event.scancode == 80:
                if self.selected == 1:
                    self.diff_select -= 1
                    if self.diff_select < 0:
                        self.diff_select = len(self.difficulties) - 1

            if event.scancode == 81:
                self.selected += 1
                if self.selected > 2:
                    self.selected = 0
            if event.scancode == 40:
                if self.selected == 0:
                    StateHandler.STATE = GameState.STATE_GAME
                    if self.diff_select == 0:
                        StateHandler.DIFFICULTY = GameState.DIFFICULTY_EASY
                    elif self.diff_select == 1:
                        StateHandler.DIFFICULTY = GameState.DIFFICULTY_MEDIUM
                    else:
                        StateHandler.DIFFICULTY = GameState.DIFFICULTY_HARD

                if self.selected == 2:
                    StateHandler.STATE = GameState.STATE_DONE

        if self.selected == 0:
            self.start_text = self.small_font.render(
                'START', False, (100, 100, 100))
        else:
            self.start_text = self.small_font.render('START', False, (0, 0, 0))
        if self.selected == 1:
            self.difficulty_text = self.small_font.render(
                'DIFFICULTY', False, (100, 100, 100))
        else:
            self.difficulty_text = self.small_font.render(
                'DIFFICULTY', False, (0, 0, 0))
        if self.selected == 2:
            self.quit_text = self.small_font.render(
                'QUIT', False, (100, 100, 100))
        else:
            self.quit_text = self.small_font.render(
                'QUIT', False, (0, 0, 0))

        self.selected_difficulty = self.diff_font.render(
            self.difficulties[self.diff_select], False, (0, 0, 0))
