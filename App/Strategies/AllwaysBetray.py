from App.Strategies.StrategyInterface import StrategyInterface


class AllwaysBetray(StrategyInterface):

    def execute(self, opponenets_moves: list[bool], own_moves: list[bool])->bool:
        """
        Always betray

        Returning True means not betraying.
        """
        return False
