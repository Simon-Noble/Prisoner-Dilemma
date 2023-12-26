import random

from App.Strategies.StrategyInterface import StrategyInterface


class MatchingPercentage(StrategyInterface):

    def execute(self, opponents_moves: list[bool], own_moves: list[bool]) -> bool:
        """
        Randomly chose true or false, manage the percentage of true and false
        to match the percentage of the opponents moves


        Returning True means not betraying.
        """

        if len(opponents_moves) == 0:
            return random.choice([True, False])

        opp_true_percentage = opponents_moves.count(True) / len(opponents_moves)

        return random.randint(0, 100) <= opp_true_percentage * 100

    def __repr__(self):
        return "MatchingPercentage"