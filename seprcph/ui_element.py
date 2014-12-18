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

    def draw(self, surface):
        """
        Tells the game how to draw the UI element

        Args:
            surface: The surface to be drawn to.
        """
        pass

    def click(self, event):
        """
        A callback that is called when the Element is clicked on.

        Args:
            event: The pygame.event resulting from a mouse click.
        """
        pass

    def resize(self, w_ratio, h_ratio):
        """
        Called when the window is resized.

        Args:
            w_ratio: The ratio by which the width has changed.
            h_ratio: The ratio by which the height has changed.
        """
        self.size[0] *= w_ratio
        self.size[1] *= h_ratio


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

    def draw(self, surface):
        for elem in self.elems:
            elem.draw(surface)

        # TODO: Container needs to render itself.

class Window(Container):
    """
    The top level of a UI, it manages everything from click processing to
    organising redrawing.
    """
    def __init__(self, size, pos, elems, surface):
        """
        Initialise the entire UI

        Args:
            size: A tuple representing the size of the Window
            pos: A tuple representing the position of the top left corner of
            the window
            elems: The elements that are to be included in this window
            surface: A pygame.Surface that shall be rendered to
        """
        super(Window, self).__init__(size, pos, elems)
        self.surface = surface

    def resize(self, size):
        """
        Called when the main Pygame screen is resized

        Args:
            size: The new size of the screen
        """
        w_ratio = size[0] / self.size[0]
        h_ratio = size[1] / self.size[1]
        for elem in self.elems:
            elem.resize(w_ratio, h_ratio)

        self.size = size

    def draw_elems(self):
        """
        Call all of the element's draw methods
        """
        for elem in self.elems:
            elem.draw(self.surface)
