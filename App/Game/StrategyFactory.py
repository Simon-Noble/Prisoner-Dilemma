from App.Strategies.AllwaysBetray import AllwaysBetray
from App.Strategies.AllwaysCooperate import AllwaysCooperate
from App.Strategies.DistrustingTitForTat import DistrustingTitForTat
from App.Strategies.Exploiter import Exploiter
from App.Strategies.Random import Random
from App.Strategies.ReverseTitForTat import ReverseTitForTat
from App.Strategies.StrategyInterface import StrategyInterface
from App.Strategies.TitForTat import TitForTat
from App.Strategies.TitForTwoTats import TitForTwoTats
from App.Strategies.TwoThirdsBetray import TwoThirdsBetray
from App.Strategies.TwoThirdsCooperate import TwoThirdsCooperate
from App.Strategies.Vindictive import Vindictive


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
        strategies.append(DistrustingTitForTat())
        strategies.append(ReverseTitForTat())
        strategies.append(TwoThirdsBetray())
        strategies.append(TwoThirdsCooperate())
        strategies.append(Vindictive())
        strategies.append(Exploiter())

        return strategies
