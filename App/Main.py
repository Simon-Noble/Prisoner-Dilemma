from App.Game.RewardSimulator import RewardSimulator
from App.Strategies.StrategyFactory import StrategyFactory
from App.RewardMatricies.BasicReward import BasicReward


def main():

    strategies = StrategyFactory.get_strategies()

    matrix = BasicReward()

    rounds = 200

    simulator = RewardSimulator(strategies,matrix,rounds)

    results = simulator.run()

    for result in results:
        print(result)


if __name__ == '__main__':
    main()
