import random

from App.Strategies.StrategyInterface import StrategyInterface


class Random(StrategyInterface):

        def execute(self, opponenets_moves: list[bool], own_moves: list[bool]) -> bool:
            """
            Randomly Pick True or False

            Returning True means not betraying.
            """
            return random.choice([True, False])

        def __repr__(self):
            return "Random"