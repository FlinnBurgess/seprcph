"""
This module contains all classes relating to the goals of the game.

Name:
    goals

File:
    seprcph/city.py

Classes:
    Goal
"""
from seprcph import event


class Goal(object):
    """
    Class that describes the player's goals
    """
    def __init__(self, start_city, end_cities, turns, gold_reward, points_reward, player, desc=""):
        """
        Initialise a goal.

        The EventManager is also made aware of the topics that Goal wants
        to listen for.

        Args:
            start_city: The city that the player's train must first visit to
            start the goal.
            end_cities: A list of cities that the player's train must visit
            (one of) to complete the goal.
            turns: The amount of turns that the player has to complete the goal.
            gold_reward: The amount of gold that the player will receive.
            points_reward: The number of points that the player will receive.
            desc: An optional description about the goal.
        """

        assert turns > 0
        assert points_reward > 0
        assert gold_reward > 0

        self.start_city = start_city
        self.end_cities = end_cities
        self.turns = turns
        self.gold_reward = gold_reward
        self.points_reward = points_reward
        self.player = player
        self.desc = desc

        self._start_reached = False
        event.EventManager.add_listener('train.arrive', self.handle_train_arrive)


    def __repr__(self):
        return "<start-city: %s, end-cities: %s, turns remaining: %d" \
               "gold-reward: %d, points-reward: %d, assigned player: %s" \
               "description: %s>" \
            % (str(self.start_city), str(self.end_cities), self.turns, self.gold_reward,
               self.points_reward, str(self.player), str(self.desc))


    def handle_train_arrive(self, ev):
        """
        The callback sent to the EventManager to be called when a train arrives
        at a city.

        Args:
            ev: The event that is passed to the EventManager. We expect this
            to contain a 'city' section within its data.
        """
        assert 'city' in ev.data

        if ev.data['city'] == self.start_city:
            self._start_reached = True
        elif ev.data['city'] in self.end_cities and self._start_reached:
            self.player.gold += self.gold_reward
            self.player.score += self.points_reward
            event.EventManager.notify_listeners(event.Event('goal.completed',
                                                            goal=self))

    def update(self):
        """
        Called each turn.

        Handles the amount of turns a player has to complete a goal and
        notifies the EventManager of goal failures.
        """
        # TODO: Do we want progress? If so, should it show the amount of turns
        # left or the distance the train has travelled?

        # TODO: Do we want goal turns to be reduced on another player's turn?
        self.turns -= 1
        if self.turns <= 0:
            event.EventManager.notify_listeners(event.Event('goal.failed', goal=self))
