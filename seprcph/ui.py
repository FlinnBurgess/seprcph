"""
Contains the function that initialises the user interface
"""

import pygame
from seprcph.ui_elements import Window, Container, Label


def initialise_ui(size, surface):
    """
    Initialises the user interface
    
    Args:
        size: The size of the window
        surface: The surface to draw the elements to
        
    Returns:
        The window object
    """
    img = pygame.Surface((10, 10))
    img.fill((100, 100, 100))
    
    c = Container((100, 100), (100, 100))
    l = Label((10, 10), (0, 0), "TEST", pygame.font.SysFont("monospace", 10), image=img)
    
    c.add(l)
    
    win = Window(size, (0, 0), 3, surface)
    win.add(c)
    win.update()

    return win
