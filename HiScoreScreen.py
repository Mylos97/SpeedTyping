import pygame
import json
from operator import itemgetter

from Display import *
from StateHandler import *


class HiScoreScreen:

    def __init__(self):
        self.font = pygame.font.Font("Resources/Quinquefive-Ea6d4.ttf", 48)
        self.score_font = pygame.font.Font(
            "Resources/Quinquefive-Ea6d4.ttf", 32)

        f = open('hi_scores.json')
        scores = json.load(f)
        self.hi_scores = sorted(
            scores['scores'], key=itemgetter('score'), reverse=True)
        self.hi_scores_draw = []
        self.hi_scores_pos = []
        self.score_name = ['A', 'A', 'A']
        self.score_name_pos = 0
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.alphabet_pos = 0

        self.current_score_render = self.score_font.render(
            ('AAA' + "   " + str(StateHandler.SCORE)), False, (0, 0, 0))
        self.hiscore_title = self.font.render('HI SCORES', False, (0, 0, 0))

        f.close()

    def update_score(self, score):
        pass

    def draw(self):
        Display.SCREEN.blit(
            self.hiscore_title, (Display.WINDOW_SIZE[0]/6, Display.WINDOW_SIZE[1]*0.1))
        j = 0
        for score in self.hi_scores_draw:
            Display.SCREEN.blit(
                score, (Display.WINDOW_SIZE[0]/6, Display.WINDOW_SIZE[1]*self.hi_scores_pos[j]))
            j += 1
        Display.SCREEN.blit(self.current_score_render, (
            Display.WINDOW_SIZE[0]/6, Display.WINDOW_SIZE[1]*0.8))

    def loop(self, event):
        i = 0.3
        temp_str = ''

        for score in self.hi_scores:
            self.hi_scores_draw.append(
                self.score_font.render(
                    score['name'] + "   " + str(score['score']), False, (0, 0, 0)))
            self.hi_scores_pos.append(i)

            i += 0.1

        if event.type == pygame.KEYDOWN:
            if event.scancode == 79:  # Right
                self.score_name_pos += 1
                self.alphabet_pos = 0
            if event.scancode == 82:  # Up
                self.alphabet_pos += 1
                if self.alphabet_pos > len(self.alphabet) - 1:
                    self.alphabet_pos = 0
                self.score_name[self.score_name_pos] = self.alphabet[self.alphabet_pos]
            if event.scancode == 81:  # Down
                self.alphabet_pos -= 1
                if self.alphabet_pos < 0:
                    self.alphabet_pos = len(self.alphabet) - 1
                self.score_name[self.score_name_pos] = self.alphabet[self.alphabet_pos]
            if event.scancode == 40:  # Enter

                self.update_score(
                    {'name': temp_str.join(self.score_name), 'score': 10})
                StateHandler.STATE = GameState.STATE_MENU

            self.current_score_render = self.score_font.render(
                temp_str.join(self.score_name) + "   " + str(StateHandler.SCORE), False, (0, 0, 0))
