from enum import Enum


class GameState(Enum):
    STATE_MENU = 1
    STATE_GAME = 2
    STATE_SCORE_BOARD = 3
    STATE_DONE = 4
    STATE_HI_SCORE = 5
    DIFFICULTY_EASY = 6
    DIFFICULTY_MEDIUM = 7
    DIFFICULTY_HARD = 8
