import pygame


class Renderable(pygame.sprite.Sprite):

    def __init__(self, image, pos):
        super(Renderable, self).__init__()

        # We can't use convert_alpha without a screen being set up, so test
        # if a screen is set up.
        try:
            image = image.convert_alpha()
        except pygame.error:
            pass
        finally:
            self.image = image

        self.pos = pos

    @property
    def rect(self):
        """
        Calculate the rect based upon the image size and
        object's position.
        """
        rect = self.image.get_rect()
        rect.centerx = self.pos[0]
        rect.centery = self.pos[1]
        return rect

    def update(self):
        pass

    def click(self):
        pass
