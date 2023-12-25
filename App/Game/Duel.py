from App.Game.Dilemma import Dilemma
from App.RewardMatricies.MatrixInterface import MatrixInterface
from App.Strategies.StrategyInterface import StrategyInterface


class Duel:
    """

    This class is used to run a duel between two strategies

    The class is instantiated with the strategies, reward matrix, and number of rounds

    It will return the total number of points each strategy received, and the moves each strategy made

    """

    def __init__(self, strategies: list[StrategyInterface], matrix: MatrixInterface, rounds: int):
        """

        Initialize the class with the strategies, reward matrix, and number of rounds

        """

        self.strategies = strategies
        self.matrix = matrix
        self.max_rounds = rounds


    def run(self) -> tuple[list[int], list[list[bool]]]:

        """

        Run the duel between the strategies

        """

        moves = [[], []]
        points = [0, 0]

        for i in range(self.max_rounds):
            new_points = Dilemma.run(self.matrix, self.strategies, moves)
            points[0] += new_points[0]
            points[1] += new_points[1]

        return points, moves
