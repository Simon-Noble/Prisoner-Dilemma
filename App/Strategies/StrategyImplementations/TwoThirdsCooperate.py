import random

from App.Strategies.StrategyInterface import StrategyInterface


class TwoThirdsCooperate(StrategyInterface):
    def execute(self, opponents_moves: list[bool], own_moves: list[bool]) -> bool:
        """
        Betray 1/3 of the time, cooperate 2/3 of the time

        Returning True means not betraying.
        """
        return random.choice([True, True, False])

    def __repr__(self):
        return "TwoThirdsCooperate"
