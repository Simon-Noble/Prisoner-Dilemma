from App.Strategies.StrategyInterface import StrategyInterface


class Punisher(StrategyInterface):
    def execute(self, opponents_moves: list[bool], own_moves: list[bool]) -> bool:
        """
        If the opponent cooperates twice, betray.
        If they continue to cooperate, continue to betray,
        Otherwise cooperate. If they betray, betray.

        Returning True means not betraying.
        """

        if len(opponents_moves) < 2:
            return True
        if not opponents_moves[-1] and not opponents_moves[-2]:
            return False
        if not opponents_moves[-1] and own_moves[-1]:
            return False
        if not own_moves[-1] and opponents_moves[-1]:
            return False
        if not own_moves[-1] and not opponents_moves[-1]:
            return True
        if opponents_moves[-1] and opponents_moves[-2]:
            return False

    def __repr__(self):
        return "Punisher"
