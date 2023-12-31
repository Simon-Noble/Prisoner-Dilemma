from App.Strategies.StrategyInterface import StrategyInterface


class Vindictive(StrategyInterface):

    def execute(self, opponents_moves: list[bool], own_moves: list[bool]) -> bool:
        """
        If the opponent has betrayed, betray.

        Returning True means not betraying.
        """
        if len(opponents_moves) == 0:
            return True
        if not own_moves[-1]:
            return False
        if not opponents_moves[-1]:
            return False
        return True

    def __repr__(self):
        return "Vindictive"
