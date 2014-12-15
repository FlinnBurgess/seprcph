"""
This module contains the main game loop as well as the system for setting up the file logger.

Name:
    main

File:
    seprcph/main.py

Functions:
    main
    setup_file_logger
"""

import logging
import os.path
import pygame
from pygame.locals import *
from seprcph.config import Config
from seprcph.map import Map


def main():
    """
    The game loop and glue code.
    """
    Config.load_config()
    logger = setup_file_logger(Config.logging['file'],
                            (Config.logging['format'],
                            Config.logging['date_format']),
                            Config.logging['level'])
    logging.info("Config.general is " + str(Config.general))
    logging.info("Config.logging is " + str(Config.logging))

    screen, clock = initialise_pygame()

    game_map = Map(pygame.image.load(os.path.join(Config.general['image_dir'], 'map.png')))
    game_map.image = pygame.transform.scale(game_map.image, screen.get_size())
    sprites = pygame.sprite.Group(game_map._cities + game_map._tracks)

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

        clock.tick()
        print clock.get_fps()
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
