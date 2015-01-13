import random
from seprcph.goal import Goal


class GoalFactory(object):

    def __init__(self):
        self.used_routes = []

    def build_goals(self, count, player, map):
        goals = []
        for _ in xrange(count):
            while True:
                start_city = random.choice(map._cities.keys())
                end_city = random.choice(map._cities.keys())
                if start_city == end_city or set(start_city, end_city) in self.used_routes:
                    continue
                else:
                    break
            # TODO: More sensible use of random to generate gold and score
            # rewards.
            goals.append(Goal(start_city, end_city, random.randint(1, 5),
                                    random.randint(100, 1000),
                                    random.randint(100, 1000), player))
