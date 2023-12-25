from App.Strategies.StrategyInterface import StrategyInterface


class DistrustingTitForTat(StrategyInterface):

    def execute (self, opponenets_moves: list[bool], own_moves: list[bool]) -> bool:
        """
        Same as tit for tat, but starts by betraying

        Returning True means not betraying.
        """
        if len(opponenets_moves) == 0:
            return False
        else:
            return opponenets_moves[-1]

    def __repr__(self):
        return "DistrustingTitForTat"
