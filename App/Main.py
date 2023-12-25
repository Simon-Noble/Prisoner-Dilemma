import random

from App.Game.Dilemma import Dilemma
from App.Game.RewardSimulator import RewardSimulator
from App.Game.StrategyFactory import StrategyFactory
from App.Strategies.AllwaysBetray import AllwaysBetray
from App.Strategies.AllwaysCooperate import AllwaysCooperate
from App.RewardMatricies.BasicReward import BasicReward
from App.Game.Duel import Duel
from App.Strategies.TitForTat import TitForTat
from App.Strategies.TitForTwoTats import TitForTwoTats


def main():

    strategies = StrategyFactory.get_strategies()

    matrix = BasicReward()

    rounds = 100

    simulator = RewardSimulator(strategies,matrix,rounds)

    results = simulator.run()

    sorted_results = [(k, results[k]) for k in sorted(results, key=results.get, reverse=True)]
    print(sorted_results)


if __name__ == '__main__':
    main()
