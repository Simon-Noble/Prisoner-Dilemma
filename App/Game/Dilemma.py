from App.RewardMatricies.MatrixInterface import MatrixInterface
from App.Strategies.StrategyInterface import StrategyInterface
"""
This class is used to run the dilemma with the given matrix and strategies

The method is static so it can be called without instantiating the class

This is used to give the matrix and strategies an adapter
"""

class Dilemma:

    @staticmethod
    def run(matrix: MatrixInterface, strategies: list[StrategyInterface], moves: list[list[bool]]) -> list[int]:
        """
        Run the dilemma with the given matrix and strategies

        Append the moves to the moves list
        """

        move = []
        move.append(strategies[0].execute(moves[1], moves[0]))
        move.append(strategies[1].execute(moves[0], moves[1]))

        moves[0].append(move[0])
        moves[1].append(move[1])

        return matrix.play(move[0], move[1])
