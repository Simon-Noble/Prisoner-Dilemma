class StrategyInterface:

    def execute(self, opponents_moves: list[bool], own_moves: list[bool]) -> bool:
        """
        Take the opponents and own previous moves and decide if
        the strategy should betray or work together

        Returning True means not betraying.
        """
        raise NotImplementedError("Strategy.execute() not implemented")
