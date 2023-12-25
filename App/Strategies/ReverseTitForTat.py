from App.Strategies.StrategyInterface import StrategyInterface


class ReverseTitForTat(StrategyInterface):

        def execute(self, opponenets_moves: list[bool], own_moves: list[bool]) -> bool:
            """
            Same as TitForTat, but inverse output

            Returning True means not betraying.
            """
            if len(opponenets_moves) == 0:
                return True
            return not opponenets_moves[-1]

        def __repr__(self):
            return "ReverseTitForTat"
