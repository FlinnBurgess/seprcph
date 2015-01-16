import pygame
from seprcph.ui_elements import Window, Container, Label, Clickable

def initialise_ui(size, surface):
    img = pygame.Surface((10, 10))
    img.fill((100, 100, 100))
    c2 = Container((10, 10), (10, 10), img)
    c = Container((100, 100), (100, 100))
    win = Window(size, (0, 0), 3, surface)
    win.add(c)
    c.add(c2)
    win.update()
    return win
