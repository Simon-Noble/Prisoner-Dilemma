from App.Strategies.StrategyImplementations.AllwaysBetray import AllwaysBetray
from App.Strategies.StrategyImplementations.AllwaysCooperate import AllwaysCooperate
from App.Strategies.StrategyImplementations.AverageOfOpponent import AverageOfOpponent
from App.Strategies.StrategyImplementations.CooperateForHalf import CooperateForHalf
from App.Strategies.StrategyImplementations.DistrustingTitForTat import DistrustingTitForTat
from App.Strategies.StrategyImplementations.Exploiter import Exploiter
from App.Strategies.StrategyImplementations.Punisher import Punisher
from App.Strategies.StrategyImplementations.Random import Random
from App.Strategies.StrategyImplementations.ReverseTitForTat import ReverseTitForTat
from App.Strategies.StrategyImplementations.SlightlyLessVindictive import SlightlyLessVindictive
from App.Strategies.StrategyImplementations.ThreeQuartersCooperate import ThreeQuartersCooperate
from App.Strategies.StrategyImplementations.TwoTatsForTit import TwoTatsForTit
from App.Strategies.StrategyInterface import StrategyInterface
from App.Strategies.StrategyImplementations.TitForTat import TitForTat
from App.Strategies.StrategyImplementations.TitForTwoTats import TitForTwoTats
from App.Strategies.StrategyImplementations.TwoThirdsBetray import TwoThirdsBetray
from App.Strategies.StrategyImplementations.TwoThirdsCooperate import TwoThirdsCooperate
from App.Strategies.StrategyImplementations.Vindictive import Vindictive


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
        strategies.append(ThreeQuartersCooperate())
        strategies.append(SlightlyLessVindictive())
        strategies.append(AverageOfOpponent())
        strategies.append(CooperateForHalf())
        strategies.append(TwoTatsForTit())
        strategies.append(Punisher())

        return strategies
