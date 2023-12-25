import random

from App.Game.Dilemma import Dilemma
from App.Strategies.AllwaysBetray import AllwaysBetray
from App.Strategies.AllwaysCooperate import AllwaysCooperate
from App.RewardMatricies.BasicReward import BasicReward
from App.Game.Duel import Duel
from App.Strategies.TitForTat import TitForTat
from App.Strategies.TitForTwoTats import TitForTwoTats


def main():

    strategy1 = TitForTat()
    strategy2 = TitForTwoTats()

    matrix = BasicReward()

    rounds = 100

    duel= Duel([strategy1, strategy2], matrix, rounds)

    results = duel.run()
    print(results)


if __name__ == '__main__':
    main()
