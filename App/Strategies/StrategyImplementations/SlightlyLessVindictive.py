from App.Strategies.StrategyInterface import StrategyInterface


class SlightlyLessVindictive(StrategyInterface):

    def execute(self, opponents_moves: list[bool], own_moves: list[bool]) -> bool:
        """
        Take the opponenets and own previous moves and decide if
        the strategy should betray or work together

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