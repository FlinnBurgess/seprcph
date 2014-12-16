"""
This module contains all classes relating to the user interface.

Name:
    ui_element

File:
    seprcph/ui_element.py

Classes:
    Element
    Clickable
"""
import pygame

"""
This is the superclass for all of our UI elements.

Name:
    ui_element

File:
    seprcph/ui_element.py

Classes:
    Element, Clickable
"""

class Element(pygame.sprite.Sprite):
    """
    Superclass for the UI elements
    """

    def __init__(self, size, position):
        """
        Args:
            size: a tuple containing the height and width of the UI element
            position: a tuple containing the coordinates of the UI element
        """
        super(Element, self).__init__()
        self.size = size
        self.pos = position

    def __repr__(self):
        return "<size: %s, position: %s>" % (self.size, self.pos)

    def draw(self):
        """
        Tells the game how to draw the UI element
        """
        pass


class Clickable(Element):
    """
    A UI element which is clickable by the user
    """

    def __init__(self, size, position, callback):
        """
        Args:
            size: a tuple containing the height and width of the UI element
            position: a tuple containing the coordinates of the UI element
            callback: the function to be called when the element is clicked
        """
        super(Clickable, self).__init__(size, position)
        self.callback = callback

    def __repr__(self):
        return "<size: %s, position: %s, callback function: %s>" \
               % (self.size, self.pos, self.callback)


class Label(Element):
    """
    A label UI element, simply contains text to display
    """

    def __init__(self, size, position,  text):
        """
        Args:
            size: a tuple containing the height and width of the UI element
            position: a tuple containing the coordinates of the UI element
            text: text to be displayed in the label
        """
        super(Label, self).__init__(size, position)
        self.text = text

    def __repr__(self):
        return "<size: %s, position: %s, text: %s>" \
               % (self.size, self.pos, self.text)