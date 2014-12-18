"""
This module contains the main game loop as well as the system for setting up the file logger.
"""

import logging
import os.path
import platform
import pygame
from seprcph.config import Config
from seprcph.map import Map


def main():
    """
    The game loop and glue code.
    """
    if platform.system() == 'Windows':
        Config.load_config(os.path.join(os.path.expanduser('~'), 'seprcph',
                                            'config.cfg'))
    else:
        Config.load_config(os.path.join(os.path.expanduser('~'), '.config',
                                            'seprcph', 'config.cfg'))

    logger = setup_file_logger(Config.logging['file'],
                            (Config.logging['format'],
                            Config.logging['date_format']),
                            Config.logging['level'])
    logging.info(str(Config))

    screen, clock = initialise_pygame()
    FPS = Config.graphics['fps']

    game_map = Map(pygame.image.load(os.path.join(Config.general['image_dir'], 'map.png')))
    game_map.image = pygame.transform.scale(game_map.image, screen.get_size())
    sprites = pygame.sprite.Group(game_map._cities.keys() + game_map._tracks)

    sprites.draw(game_map.image)
    screen.blit(game_map.image, (0, 0))
    pygame.display.flip()

    while True:
        # This will block if there isn't an event.
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            return
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode(event.dict['size'], pygame.RESIZABLE)
            screen.blit(pygame.transform.scale(game_map.image, event.dict['size']), (0, 0))
            pygame.display.flip()

        clock.tick(FPS)
        sprites.draw(game_map.image)
        pygame.display.flip()


def initialise_pygame():
    """
    Intialise pygame modules, then the screen and finally the clock.
    """
    pygame.init()
    if Config.general['fullscreen']:
        screen = pygame.display.set_mode((Config.general['screen_width'],
                                        Config.general['screen_height']),
                                        pygame.FULLSCREEN | pygame.RESIZABLE)
    else:
        screen = pygame.display.set_mode((Config.general['screen_width'],
                                        Config.general['screen_height']), pygame.RESIZABLE)

    pygame.display.set_caption('Trains across Europe')
    clock = pygame.time.Clock()
    logging.debug("%s", pygame.display.Info())
    return screen, clock


def setup_file_logger(filename, formatting, log_level):
    """
    A helper function for creating a file logger.

    Args:
        filename: The file that shall be logged to.
        formatting: A tuple containing the log format and then the date format.
        log_level: The level of logging to be reported.

    Returns:
        logger: A complete logger object.
    """
    logger = logging.getLogger()
    # If a stream handler has been attached, remove it.
    if logger.handlers:
        logger.removeHandler(logger.handlers[0])
    handler = logging.FileHandler(filename)
    logger.addHandler(handler)
    formatter = logging.Formatter(*formatting)
    handler.setFormatter(formatter)
    logger.setLevel(log_level)
    handler.setLevel(log_level)
    return logger

if __name__ == '__main__':
    main()
