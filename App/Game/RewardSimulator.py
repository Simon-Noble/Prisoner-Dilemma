from App.RewardMatricies.MatrixInterface import MatrixInterface
from App.Strategies.StrategyInterface import StrategyInterface


class RewardSimulator:
    """
    This class takes a set of strategies, a reward matrix, and a number of rounds to simulate
    and runs the simulation
    """

    def __init__(self, strategies: list[StrategyInterface], matrix: MatrixInterface, rounds: int):
        """
        Initialize the class with the strategies, reward matrix, and number of rounds
        """

        self.strategies = strategies
        self.matrix = matrix
        self.max_rounds = rounds

    def run(self):
        """
        Run the simulation
        """
        all_matchups = []
        for i in range(len(self.strategies)):
            for j in range(i, len(self.strategies)):
                current_strategies = [self.strategies[i], self.strategies[j]]
                all_matchups.append(current_strategies)

        return all_matchups