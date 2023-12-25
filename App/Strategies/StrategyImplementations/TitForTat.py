from App.Strategies.StrategyInterface import StrategyInterface


class TitForTat(StrategyInterface):
    def execute(self, opponenets_moves: list[bool], own_moves: list[bool]) -> bool:
        """
        Don't betray unless the opponent has betrayed.
        Forgive if forgiven

        Returning True means not betraying.
        """
        if len(opponenets_moves) == 0:
            return True
        return opponenets_moves[-1]

    def __repr__(self):
        return "TitForTat"