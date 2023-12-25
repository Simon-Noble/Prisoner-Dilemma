from App.Strategies.AllwaysBetray import AllwaysBetray
from App.Strategies.AllwaysCooperate import AllwaysCooperate
from App.Strategies.Random import Random
from App.Strategies.StrategyInterface import StrategyInterface
from App.Strategies.TitForTat import TitForTat
from App.Strategies.TitForTwoTats import TitForTwoTats


class StrategyFactory:

    @staticmethod
    def get_strategies() -> list[StrategyInterface]:
        """

        return a list of all the strategies

        More conditions may be added later
        :return:
        """

        strategies = []

        strategies.append(Random())
        strategies.append(TitForTat())
        strategies.append(TitForTwoTats())
        strategies.append(AllwaysBetray())
        strategies.append(AllwaysCooperate())


        return strategies
