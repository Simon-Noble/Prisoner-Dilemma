from MatrixInterface import MatrixInterface

class BasicReward(MatrixInterface):

    def play(self, decisionA: bool, decisionB: bool) ->(int, int):
        """
        Takes the decisions of two players and returns the reward for each player.
        """
        if decisionA and decisionB:
            return (3, 3)
        elif decisionA and not decisionB:
            return (0, 5)
        elif not decisionA and decisionB:
            return (5, 0)
        else:
            return (1, 1)