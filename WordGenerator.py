import pygame
import random
from Mediator import *
from Display import *
from Word import *


class WordGenerator:

    OFF_SET = 128
    DELAY1 = 30
    DELAY2 = 60

    def __init__(self):
        self.timer = 0
        self.wait_for_spawn = random.randint(
            WordGenerator.DELAY1, WordGenerator.DELAY2)
        self.words = []
        self.words_spawned = 0
        self.difficulty_scalar = 0

        with open('Resources/words.txt') as f:
            lines = f.readlines()
            for string in lines:
                self.words.append(string.strip())

    def loop(self):
        self.timer += 1

        if self.timer > self.wait_for_spawn:
            self.timer = 0
            self.words_spawned += 1
            if self.words_spawned % 10 == 0:
                self.difficulty_scalar += 1

            self.wait_for_spawn = random.randint(
                WordGenerator.DELAY1 - self.difficulty_scalar, WordGenerator.DELAY2 - self.difficulty_scalar)
            word = self.words[random.randint(0, len(self.words))]

            pos = [random.randint(WordGenerator.OFF_SET, Display.WINDOW_SIZE[0] -
                                  WordGenerator.OFF_SET - len(word)*24), Display.WINDOW_SIZE[1] + WordGenerator.OFF_SET*random.randint(0, 2)]
            print(pos)
            Mediator.OBJECTS.append(
                Word(pos, word))
