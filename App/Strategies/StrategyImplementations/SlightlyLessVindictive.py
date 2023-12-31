from App.Strategies.StrategyInterface import StrategyInterface


class SlightlyLessVindictive(StrategyInterface):

    def execute(self, opponents_moves: list[bool], own_moves: list[bool]) -> bool:
        """
        Same as vindictive, but only betray if opponent has betrayed twice in a row

        Returning True means not betraying.
        """
        if len(opponents_moves) <2:
            return True
        if not own_moves[-1]:
            return False
        if not opponents_moves[-1] and not opponents_moves[-2]:
            return False

    def __repr__(self):
        return "SlightlyLessVindictive"