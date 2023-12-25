from App.Strategies.StrategyInterface import StrategyInterface


class CooperateForHalf(StrategyInterface):
    def execute(self, opponents_moves: list[bool], own_moves: list[bool]) -> bool:
        """
        Cooperate for half the game, then betray for the rest.

        Returning True means not betraying.
        """
        if len(opponents_moves) < 100:
            return True
        return False

    def __repr__(self):
        return "CooperateForHalf"
