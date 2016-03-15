from enum import Enum

class PlayerName(Enum):
    PlayerX = 1
    PlayerO = 2

class GameWinner(Enum):
    InProgress = 0
    PlayerX = 1
    PlayerO = 2
    Tie = 3

class GameState:

    # Who's turn is it
    CurrentPlayer = PlayerName.PlayerX
    
    # Who's the winner (or no winner)
    GameWinner = GameWinner.InProgress

    # Key Value pairs between "Spaces" and "Characters"
    #
    #
    # 0 1 2
    # 3 4 5
    # 6 7 8
    #
    # Example:
    # X - O
    # X - O
    # O - -
    #
    # will contain 
    # (0,X)(2,O)(3,X)(5,O)(6,O)
    #
    OccupiedSpaces = dict()

class GameMove:

    # Who I am
    Player

    # Where I'm moving
    Space

class TicTacToeGameInterface:

    def GetCurrentGameState(self):
        # TODO: wire this up
        return GameState()
    
    def IsValid(self, gameMove):
        # TODO: Wire this up
        return (False, "This functionality is TODO")

    def MakeMove(self, gameMove):
        # TODO: Wire this up
        return GameState()