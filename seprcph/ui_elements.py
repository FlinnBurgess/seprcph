"""
This module contains all classes relating to the user interface.
"""
import pygame

from seprcph.event import EventManager


class OutsideContainerError(Exception):
    """
    The element that is going to be added to the container is outside of the
    container.
    """
    pass


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
        self.layer = 0
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

    @property
    def rect(self):
        """
        Calculate the rect based upon the image size and
        object's position.
        """
        rect = self.image.get_rect()
        rect.topleft = self.pos
        return rect


class Clickable(Element):
    """
    A UI element which is clickable by the user
    """
    def __init__(self, size, position, callback, image, **kwargs):
        """
        Args:
            size: a tuple containing the height and width of the UI element
            position: a tuple containing the coordinates of the UI element
            callback: the function to be called when the element is clicked
            image: A pygame surface
        """
        super(Clickable, self).__init__(size, position, image)
        self.cb = callback
        self.__dict__.update(kwargs)

    def __repr__(self):
        return "<size: %s, position: %s, callback function: %s>" \
               % (self.size, self.pos, self.cb)

    def click(self, event):
        self.cb(event)


class Label(Element):
    """
    A label UI element, simply contains text to display
    """
    def __init__(self, size, position, text, font, colour=(255, 255, 255), image=None):
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
        if not image:
            if size[0] < font.size(text)[0] or size[1] < font.size(text)[1]:
                self.image = pygame.Surface(font.size(text))
                self.size = font.size(text)
            else:
                self.image = pygame.Surface(size)
                self.size = size
        super(Label, self).__init__(self.size, position, self.image)
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
    def __init__(self, size, pos, image=None):
        """
        Args:
            size: a tuple containing the height and width of the UI element
            pos: a tuple containing the coordinates of the UI element
            image: A pygame surface (not required)
        """
        if not image:
            image = pygame.Surface(size, pygame.SRCALPHA, 32)
            image = image.convert()
        super(Container, self).__init__(size, pos, image)
        self.elems = pygame.sprite.LayeredUpdates()

    def add(self, element):
        """
        Add an element to the container
        """
        element.pos = (element.pos[0] + self.pos[0],
                        element.pos[1] + self.pos[1])
        if not pygame.sprite.collide_rect(self, element) \
                or element.rect.topleft < self.rect.topleft \
                or element.rect.bottomright > self.rect.bottomright:
            raise OutsideContainerError("element %s is outside of container %s",
                                        str(element), str(self))

        element.layer = self.layer + 1
        self.elems.add(element, layer=element.layer)

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
        w_ratio = float(size[0]) / float(self.size[0])
        h_ratio = float(size[1]) / float(self.size[1])
        for elem in self.elems:
            elem.resize((int(elem.size[0] * w_ratio), int(elem.size[1] * h_ratio)))

        self.size = (int(self.size[0] * w_ratio), int(self.size[1] * h_ratio))

    def update(self):
        for elem in self.elems:
            elem.update()

class Window(Container):
    """
    The top level of a UI, it manages all elements.

    The Window is reponsible for telling elements that they are to be resized,
    telling elements when they have been clicked as well as rendering elements.
    """
    def __init__(self, size, pos, layer, surface):
        """
        Initialise the entire UI

        Args:
            size: A tuple representing the size of the Window
            pos: A tuple representing the position of the top left corner of the window
        """
        super(Window, self).__init__(size, pos, surface)
        self.layer = layer

        EventManager.add_listener('ui.clicked', self.click)
        EventManager.add_listener('window.resize', self.resize)

    def resize(self, event):
        """
        Called when the main Pygame screen is resized

        Args:
            event: Contains the field 'size' and 'old_size'
        """
        w_ratio = float(event.size[0]) / float(event.old_size[0])
        h_ratio = float(event.size[1]) / float(event.old_size[1])
        for elem in self.elems:
            elem.resize((int(elem.size[0] * w_ratio), int(elem.size[1] * h_ratio)))

        self.size = (int(self.size[0] * w_ratio), int(self.size[1] * h_ratio))

    def draw(self, surface):
        self.update()
        self.elems.draw(surface)
