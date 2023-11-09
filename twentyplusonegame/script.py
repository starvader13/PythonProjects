from TwentyPlusOneGame import TwentyPLusOneGame

def WaitingMessage():
    print("Welcome to the \"TWENTY PLUS ONE GAME\".")
    print("You are Player 1.Computer is Player 2", end="\n\n")

    print("Do you want to start the game?")
    print("> ",end="")

def userGame():
    game.userChance()
    game.user_playing_position = "S"

def computerGame():
    game.computerChance()
    game.user_playing_position = "F"


if __name__ == "__main__":
    game = TwentyPLusOneGame()

    WaitingMessage()

    game.start = str(input())
    game.checkStart()

    print("\nIf you want to start first press F otherwise press S: ")
    game.printStatementForInput()
    game.user_playing_position = str(input())

    while game.checkListElement():
        if game.user_playing_position == True:
            userGame()
        else:
            computerGame()
        
        print(game.count_list)
        game.checkLoseGame()
