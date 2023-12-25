from App.Strategies.StrategyInterface import StrategyInterface


class TwoTatsForTit(StrategyInterface):
    def execute(self, opponents_moves: list[bool], own_moves: list[bool]) -> bool:
        """
        If the opponent has betrayed twice in a row, betray.
        Otherwise, cooperate.
        """
        if len(opponents_moves) < 2:
            return True
        if not opponents_moves[-1] and not opponents_moves[-2]:
            return False
        return True

    def __repr__(self):
        return "TwoTatsForTit"
