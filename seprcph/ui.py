import pygame
from seprcph.ui_elements import Window, Container, Label, Clickable

def initialise_ui(size, surface):
    img = pygame.Surface((10, 10))
    img.fill((100, 100, 100))
    c = Container((100, 100), (100, 100))
    l = Label((10, 10), (0, 0), "TEST", pygame.font.SysFont("monospace", 10), image=img)
    c.add(l)
    win = Window(size, (0, 0), 3, surface)
    win.add(c)
    win.update()
    return win
