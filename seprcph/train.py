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
from seprcph.renderable import Renderable

class Train(Renderable):
    """
    Class representing train objects in the game
    """
    def __init__(self, effects, speed, capacity, city, current_load, image):
        """
        Args:
            effects: A list of buffs and debuffs
            speed: The speed of the train
            capacity: The capacity of the train
            city: The city the train is created at
            current_load: The amount of cargo the train is carrying
            image: The pygame surface associated with this train
        """
        super(Train, self).__init__(city.pos, image)
        self.effects = effects
        self.speed = speed
        self.capacity = capacity
        self.current_load = current_load
        self.city = city

        #The following are for dealing with train movement
        self.track = None
        self.rotation = None
        self.distance = None
        self.counter = 0

        EventManager.add_listener('goal.completed', self.unload)
        EventManager.add_listener('goal.started', self.load)

    ## TODO apply_effects NEEDS REWORKING - this is a placeholder and does not
    ## TODO fit with the way the cards and decks currently work.
    def apply_effects(self):
        for effect in self.effects:
            effect()

    def depart(self, track):
        """
        Method to be called when a train departs from a city

        Args:
            track: a track object which the train should travel along.
        """
        assert self.city in track.cities
        self.track = track
        self.rotation = track.rotation()
        self.distance = track.length()
        self.pos = self.city.pos

        #XXX: Need to set self.city correctly.
        e = Event('train.departure', train=self, city=self.city)
        EventManager.notify_listeners(e)

    def arrive(self, city):
        """
        Method to be called when a train arrived at a city

        Args:
            city: the city that the train is arriving in
        """
        self.city = city
        self.track = None
        self.rotation = 0
        self.distance = 0

        e = Event('train.arrival', train=self, city=self.city)
        EventManager.notify_listeners(e)

    def update(self):
        move_distance = (
            math.fabs((self.track.cities[0].pos[0] - self.track.cities[1].pos[0]) / self.distance) * self.speed,
            math.fabs((self.track.cities[0].pos[1] - self.track.cities[1].pos[1]) / self.distance) * self.speed
        )

        self.counter += self.speed

        if self.counter > self.track.length:
            self.arrive(self.track.cities[0])
        else:
            self.pos[0] += move_distance[0]
            self.pos[1] += move_distance[1]

    def unload(self, event):
        """
        The handler for when a goal is completed.
        """
        if self.city not in event.data['goal'].end_cities:
            return
        self.current_load = 0

    def load(self, event):
        """
        The handler for when a goal is started.
        """
        if self.city != event.data['goal'].start_city:
            return
        # Just fill the train up completely.
        self.current_load = self.capacity
