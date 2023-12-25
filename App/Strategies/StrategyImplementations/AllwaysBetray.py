from App.Strategies.StrategyInterface import StrategyInterface


class AllwaysBetray(StrategyInterface):

    def execute(self, opponents_moves: list[bool], own_moves: list[bool])->bool:
        """
        Always betray

        Returning True means not betraying.
        """
        return False

    def __repr__(self):
        return "AllwaysBetray"
