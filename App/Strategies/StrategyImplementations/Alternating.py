from App.Strategies.StrategyInterface import StrategyInterface


class Alternating(StrategyInterface):

    def execute(self,opponents_moves: list[bool], own_moves: list[bool]) -> bool:
        """
            Alternate between True and False

            Returning True means not betraying.
            """
        return not own_moves[-1] if own_moves else True

    def __repr__(self):
        return "Alternating"
