import pygame
import random
from Mediator import *
from Display import *
from Word import *


class WordGenerator:

    OFF_SET = 128
    DELAY1 = 1*60
    DELAY2 = 2*60

    def __init__(self):
        self.timer = 0
        self.wait_for_spawn = random.randint(
            WordGenerator.DELAY1, WordGenerator.DELAY2)
        self.words = []

        with open('Resources/words.txt') as f:
            lines = f.readlines()
            for string in lines:
                self.words.append(string.strip())

    def loop(self):
        self.timer += 1

        if self.timer > self.wait_for_spawn:
            self.wait_for_spawn = random.randint(
                WordGenerator.DELAY1, WordGenerator.DELAY2)
            self.timer = 0
            pos = [random.randint(WordGenerator.OFF_SET, Display.WINDOW_SIZE[0] -
                                  WordGenerator.OFF_SET), Display.WINDOW_SIZE[1] + WordGenerator.OFF_SET*random.randint(0, 2)]
            Mediator.OBJECTS.append(
                Word(pos, self.words[random.randint(0, len(self.words))]))
