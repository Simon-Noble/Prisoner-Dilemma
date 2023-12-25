from App.Strategies.StrategyInterface import StrategyInterface


class TitForTwoTats(StrategyInterface):
    def execute(self, opponenets_moves: list[bool], own_moves: list[bool]) -> bool:
        """
        If the opponent has betrayed in the last 2 moves, betray.

        Equivilent to betraying 2x for each betrayal

        Returning True means not betraying.
        """
        if len(opponenets_moves) < 2:
            return True
        return opponenets_moves[-1] and opponenets_moves[-2]

    def __repr__(self):
        return "TitForTwoTats"