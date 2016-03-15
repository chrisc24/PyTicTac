from enum import Enum

class GameStateProcessor:
    
    def __init__(self, parentGameState, move):
        self.CurrentPlayer = PlayerName((parentGameState.CurrentPlayer.value + 1)%2)
        self.OccupiedSpaces = dict(parentGameState.OccupiedSpaces)
        CalculateNewWinner()

    def IsValid(self, move):
        if self.GameWinner != GameWinner.InProgress:
           return (False, "The game is over, final outcome goes to {0}.".format(self.GameWinner))
        elif move.Player != self.CurrentPlayer:
            return (False, "It is not your turn; it is {0}'s turn.".format(self.CurrentPlayer))
        elif move.Space in self.OccupiedSpaces:
            return (False, "There is already a symbol in space {0}.".format(move.location))
        else:
            return (True, "")

print("hello")