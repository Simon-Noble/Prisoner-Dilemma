from App.Strategies.StrategyInterface import StrategyInterface


class AlternatingSlightlyVindictive(StrategyInterface):
    def execute(self, opponenets_moves: list[bool], own_moves: list[bool]) -> bool:
        """
        Alternate between True and False

        Returning True means not betraying.
        """

        if len(opponenets_moves) > 1:
            if opponenets_moves[-1] is False and opponenets_moves[-2] is False:
                return False

        return not own_moves[-1] if own_moves else True

    def __repr__(self):
        return "AlternatingSlightlyVindictive"
