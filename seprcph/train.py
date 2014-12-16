"""
This module contains all classes relating to the trains.

Name:
    train

Files:
    seprcph/train.py

Classes:
    Train
"""
import pygame
import math
from seprcph.event import Event, EventManager

class Train(pygame.sprite.Sprite):
    """
    Class representing train objects in the game
    """

    def __init__(self, buffs, debuffs, speed, capacity, city):
        """
        Args:
            buffs: list of buffs currently affecting the train
            debuffs: list of debuffs currently affecting the train
            speed: the speed of the train
            capacity: the capacity of the train
            city: the city the train is created at
        """
        super(Train, self).__init__()
        self.buffs = buffs
        self.debuffs = debuffs
        self.speed = speed
        self.capacity = capacity
        self.city = city

        #The following are for dealing with train movement
        self.track = None
        self.rotation = None
        self.distance = None
        self.pos = None
        self.counter = 0

    ## TODO apply_effects NEEDS REWORKING - this is a placeholder and does not
    ## TODO fit with the way the cards and decks currently work.
    def apply_effects(self):
        for effect in self.buffs:
            effect.apply()
        for effect in self.debuffs:
            effect.apply()

    def depart(self, track):
        """
        Method to be called when a train departs from a city

        Args:
            track: a track object which the train should travel along.
        """
        assert track.start_city == self.city
        self.track = track
        self.rotation = track.rotation()
        self.distance = track.length()
        self.pos = self.city.pos

        e = Event('train_departure')
        EventManager.notify_listeners(e)

    def arrive(self, city):
        """
        Method to be called when a train arrived at a city

        Args:
            city: the city that the train is arriving in
        """
        self.city = city
        self.track = None
        self.rotation = None
        self.distance = None
        self.pos = None

        e = Event('train_arrival')
        EventManager.notify_listeners(e)

    def update(self):
        move_distance = (
            math.fabs((self.track.end_city.pos[0] - self.track.start_city.pos[0]) / self.distance) * self.speed,
            math.fabs((self.track.end_city.pos[1] - self.track.start_city.pos[1]) / self.distance) * self.speed
        )

        self.counter += self.speed

        if self.counter > self.track.length:
            self.arrive(self.track.end_city)
        else:
            self.pos[0] += move_distance[0]
            self.pos[1] += move_distance[1]