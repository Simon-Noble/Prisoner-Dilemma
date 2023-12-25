import random

from App.Strategies.StrategyInterface import StrategyInterface


class TwoThirdsBetray(StrategyInterface):
    def execute(self, opponents_moves: list[bool], own_moves: list[bool]) -> bool:
        """
        2/3 Times betray, 1/3 times cooperate.

        Returning True means not betraying.
        """
        return random.choice([True, False, False])

    def __repr__(self):
        return "TwoThirdsBetray"
