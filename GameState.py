from enum import Enum


class GameState(Enum):
    STATE_MENU = 1
    STATE_GAME = 2
    STATE_SCORE_BOARD = 3
    STATE_DONE = 4
    DIFFICULTY_EASY = 5
    DIFFICULTY_MEDIUM = 6
    DIFFICULTY_HARD = 7
