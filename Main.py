import pygame
from Mediator import *
from Display import *
from TextInput import *
from WordGenerator import *
from ScoreBoard import *

pygame.init()
pygame.display.set_caption('Speed Typer')
running = True


def check_words():
    for element in Mediator.OBJECTS:
        if element.correct:
            score_board.increment_score()
            Mediator.OBJECTS.remove(element)
            return
    score_board.decrease_score()


text_input = TextInput(check_words)
word_generator = WordGenerator()
score_board = ScoreBoard()
clock = pygame.time.Clock()
timer = 0

while running:
    Display.SCREEN.fill((255, 255, 255))
    dt = clock.tick(60)

    for event in pygame.event.get():
        text_input.handle_event(event)
        if event.type == pygame.QUIT:
            running = False

    curr_word = text_input.get_current_word()
    for element in Mediator.OBJECTS:
        element.loop(dt, curr_word)
        element.draw()

        if element.removeable:
            Mediator.OBJECTS.remove(element)
            score_board.decrease_health()

    word_generator.loop()
    text_input.loop(dt)
    text_input.draw()
    score_board.loop()
    score_board.draw()
    pygame.display.update()


pygame.quit()
