from seprcph.ui_elements import Window, Container, Label, Clickable
import pygame

def initialise_ui(size, surface):
    test_image = pygame.Surface((2160, 1024))
    test_image.fill((0, 0, 0))

    card_container = Container((2160, 1024), (0, 1024), [], test_image)

    win = Window(size, (0, 0), [card_container], surface)
    win.update()

    return win
