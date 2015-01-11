"""
This module contains all classes relating to the user interface.
"""
import pygame

from seprcph.event import EventManager

class Element(pygame.sprite.Sprite):
    """
    Superclass for the UI elements

    NOTE: pos refers to the top left of the Element's rect - not the center
    (as is the case with renderables)

    An element's update method is to be used for blitting information to its
    own image. Elements are collected into a pygame.sprite.Group and are all
    drawn in one go - using an Element's rect and image to determine how
    they are rendered.
    """
    def __init__(self, size, position, image):
        """
        Args:
            size: a tuple containing the height and width of the UI element
            position: a tuple containing the coordinates of the UI element
            image: A pygame.Surface
        """
        super(Element, self).__init__()
        self.size = size
        self.pos = position
        self.image = image
        self.rect = image.get_rect()
        self.rect.topleft = self.pos

    def __repr__(self):
        return "<size: %s, position: %s>" % (self.size, self.pos)

    def click(self, event):
        """
        A callback that is called when the Element is clicked on.

        Args:
            event: The pygame.event resulting from a mouse click.
        """
        pass

    def update(self):
        """
        Called before the element is drawn.

        This should be used for blitting to an Element's texture.
        """
        pass

    def resize(self, size):
        """
        Called when the window is resized.

        Args:
            A tuple representing the element's new size
        """
        self.size = size


class Clickable(Element):
    """
    A UI element which is clickable by the user
    """
    def __init__(self, size, position, callback, image):
        """
        Args:
            size: a tuple containing the height and width of the UI element
            position: a tuple containing the coordinates of the UI element
            callback: the function to be called when the element is clicked
            image: A pygame surface
        """
        super(Clickable, self).__init__(size, position, image)
        self.cb = callback

    def __repr__(self):
        return "<size: %s, position: %s, callback function: %s>" \
               % (self.size, self.pos, self.cb)

    def click(self, event):
        self.cb(event)


class Label(Element):
    """
    A label UI element, simply contains text to display
    """
    def __init__(self, size, position, text, font, colour, image):
        """
        Args:
            size: a tuple containing the height and width of the UI element
            position: a tuple containing the coordinates of the UI element
            text: text to be displayed in the label
            font: The pygame.font.Font object which describes how the text
                  should look
            colour: A three element tuple in the form RGB
            image: A pygame surface
        """
        super(Label, self).__init__(size, position, image)
        self.text = text
        self.font = font
        self.colour = colour

    def __repr__(self):
        return "<size: %s, position: %s, text: %s>" \
               % (self.size, self.pos, self.text)

    def update(self):
        label = self.font.render(self.text, True, self.colour)
        self.image.blit(label, (0, 0))


class Container(Element):
    """
    A container class which will contain other UI elements
    """
    def __init__(self, size, pos, elems, image=None):
        """
        Args:
            size: a tuple containing the height and width of the UI element
            pos: a tuple containing the coordinates of the UI element
            elems: a list of UI elements contained within the container
            image: A pygame surface (not required)
        """
        if not image:
            image = pygame.Surface(size, pygame.SRCALPHA, 32)
            image = image.convert()
        super(Container, self).__init__(size, pos, image)
        self.elems = pygame.sprite.Group(elems)

    def add(self, element):
        """
        Add an element to the container
        """
        self.elems.add(element)

    def remove(self, element):
        """
        Remove an element from the container
        """
        self.elems.remove(element)

    def click(self, event):
        """
        Creates a list of UI elements clicked and executes their callbacks.

        Args:
            event: The Event resulting from a mouse click.
        """
        for elem in [e for e in self.elems if e.rect.collidepoint(event.pos)]:
            try:
                elem.click(event)
            except AttributeError:
                pass

    def resize(self, size):
        """
        Called when the main Pygame screen is resized

        Args:
            size: The new size of the container
        """
        w_ratio = self.size[0] / size[0]
        h_ratio = self.size[1] / size[1]
        for elem in self.elems:
            elem.resize((elem.size[0] * w_ratio, elem.size[1] * h_ratio))

        self.size = size

    def update(self):
        for elem in self.elems:
            elem.update()
        self.elems.draw(self.image)

class Window(Container):
    """
    The top level of a UI, it manages all elements.

    The Window is reponsible for telling elements that they are to be resized,
    telling elements when they have been clicked as well as rendering elements.
    """
    def __init__(self, size, pos, elems, surface):
        """
        Initialise the entire UI

        Args:
            size: A tuple representing the size of the Window
            pos: A tuple representing the position of the top left corner of the window
            elems: The elements that are to be included in this window
        """
        super(Window, self).__init__(size, pos, elems, surface)
        EventManager.add_listener('ui.clicked', self.click)
