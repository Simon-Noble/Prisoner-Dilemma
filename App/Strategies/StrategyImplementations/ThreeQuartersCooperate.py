import random

from App.Strategies.StrategyInterface import StrategyInterface


class ThreeQuartersCooperate(StrategyInterface):

    def execute(self, opponents_moves: list[bool], own_moves: list[bool]) -> bool:
        """
        3/4 Chance of cooperating, 1/4 chance of betraying

        Returning True means not betraying.
        """
        return random.choice([True, True, True, False])

    def __repr__(self):
        return "ThreeQuartersCooperate"
