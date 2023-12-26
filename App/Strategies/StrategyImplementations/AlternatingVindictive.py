from App.Strategies.StrategyInterface import StrategyInterface


class AlternatingVindictive(StrategyInterface):
    def execute(self, opponenets_moves: list[bool], own_moves: list[bool]) -> bool:
        """
        Alternate between True and False

        Returning True means not betraying.
        """

        if len(opponenets_moves) == 0:
            return True
        if len(opponenets_moves) == 1:
            return False
        if not own_moves[-1] and not own_moves[-2]:
            return False
        if not opponenets_moves[-1]:
            return False

        return own_moves[-1]

    def __repr__(self):
        return "AlternatingVindictive"
