from App.Strategies.StrategyInterface import StrategyInterface


class ReverseTitForTat(StrategyInterface):

        def execute(self, opponents_moves: list[bool], own_moves: list[bool]) -> bool:
            """
            Same as TitForTat, but inverse output

            Returning True means not betraying.
            """
            if len(opponents_moves) == 0:
                return True
            return not opponents_moves[-1]

        def __repr__(self):
            return "ReverseTitForTat"
