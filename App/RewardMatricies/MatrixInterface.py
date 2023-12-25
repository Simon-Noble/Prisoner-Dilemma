class MatrixInterface:

    def play(self, decisionA: bool, decisionB: bool)->(int, int):
        """
        Takes the decisions of two players and returns the reward for each player.
        """
        raise NotImplementedError("MatrixInterface.play() not implemented")