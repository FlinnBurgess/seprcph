"""
Contains the GoalFactory class and any code relating to it
"""

import random
from seprcph.goal import Goal


class GoalFactory(object):
    """
    
    """
    def __init__(self):
        """
        Setup the GoalFactory. used_routes is a list of sets that contains the
        start and end cities of a goal.
        """
        self.used_routes = []

    def build_goals(self, count, player, map_):
        """
        Generate goals with different start and end points.

        Args:
            count: The amount of goals to generate.
            player: The player that the goal will be assigned to.
            map: The map object, so we can work out which cities to use.

        Return:
            goals: A list of Goals.
        """
        goals = []
        
        for _ in xrange(count):
            while True:
                start_city = random.choice(map_._cities.keys())
                end_city = random.choice(map_._cities.keys())
                if start_city == end_city or set([start_city, end_city]) in self.used_routes:
                    continue
                else:
                    break
                    
            # TODO: More sensible use of random to generate gold and score
            # rewards.
            goals.append(Goal(start_city, end_city, random.randint(1, 5),
             random.randint(100, 1000),
             random.randint(100, 1000), player))
             
            self.used_routes.append(set([start_city, end_city]))

        return goals
