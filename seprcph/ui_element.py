"""
This module contains all classes relating to the user interface.

Name:
    ui_element

File:
    seprcph/ui_element.py

Classes:
    Element
    Clickable
    Label
    Container
"""
import pygame

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

    def click(self, event):
        """
        A callback that is called when the Element is clicked on.

        Args:
            event: The pygame.event resulting from a mouse click.
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
        self.click = callback

    def __repr__(self):
        return "<size: %s, position: %s, callback function: %s>" \
               % (self.size, self.pos, self.callback)


class Label(Element):
    """
    A label UI element, simply contains text to display
    """
    def __init__(self, size, position, text, font):
        """
        Args:
            size: a tuple containing the height and width of the UI element
            position: a tuple containing the coordinates of the UI element
            text: text to be displayed in the label
            font: The pygame.font.Font object which describes how the text
                  should look.
        """
        super(Label, self).__init__(size, position)
        self.text = text
        self.font = font

    def __repr__(self):
        return "<size: %s, position: %s, text: %s>" \
               % (self.size, self.pos, self.text)


class Container(Element):
    """
    A container class which will contain other UI elements
    """
    def __init__(self, size, pos, elems):
        """
        Args:
            size: a tuple containing the height and width of the UI element
            pos: a tuple containing the coordinates of the UI element
            elems: a list of UI elements contained within the container
        """
        super(Container, self).__init__(size, pos)
        self.elems = pygame.sprite.Group(elems)

    def click(self, event):
        """
        Creates a list of UI elements clicked and executes their callbacks.

        Args:
            event: The pygame.event resulting from a mouse click.
        """
        for elem in [e for e in self.elems if e.rect.collidepoint(event.pos)]:
            try:
                elem.click(event)
            except AttributeError:
                pass
