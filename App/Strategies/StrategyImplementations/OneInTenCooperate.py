import random

from App.Strategies.StrategyInterface import StrategyInterface


class OneInTenCooperate(StrategyInterface):

        def execute(self, opponents_moves: list[bool], own_moves: list[bool]) -> bool:
            """
            Cooperate 10% of the time

            Returning True means not betraying.
            """
            return random.randint(0, 9) == 0

        def __repr__(self):
            return "OneInTenCooperate"