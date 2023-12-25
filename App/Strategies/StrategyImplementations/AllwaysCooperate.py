from App.Strategies.StrategyInterface import StrategyInterface


class AllwaysCooperate(StrategyInterface):

    def execute(self, opponents_moves: list[bool], own_moves: list[bool]) -> bool:
        """
        Always return not betraying

        Returning True means not betraying.
        """
        return True

    def __repr__(self):
        return "AllwaysCooperate"