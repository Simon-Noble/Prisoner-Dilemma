from App.Strategies.StrategyInterface import StrategyInterface


class AverageOfOpponent(StrategyInterface):
    def execute(self, opponents_moves: list[bool], own_moves: list[bool]) -> bool:
        """
        If the opponent has betrayed more than 50% of the time, betray.

        Returning True means not betraying.
        """
        if len(opponents_moves) == 0:
            return True
        opponent_cooperation = 0

        for action in opponents_moves:
            if action:
                opponent_cooperation += 1
        return opponent_cooperation / len(opponents_moves) > 0.5

    def __repr__(self):
        return "AverageOfOpponent"
