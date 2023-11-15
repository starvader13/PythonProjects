from RockPaperScissorGame import RockPaperScissorGame

def welcomeMessage():
    print("Welcome to the Rock, Paper and Scissor Game", end="\n\n")

def rulesOfGame():
    print("Rules of the Game !!!")
    print("Rock vs Paper -> Paper Wins")
    print("Rock vs Scissor -> Rock Wins")
    print("Scissor vs Paper -> Scissor Wins.", end="\n\n")

def gameOption():
    print("\nUser's Turn ... ", end="\n\n")
    print("Choose From the option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")
    print("> ", end="")

if __name__ == "__main__":
    welcomeMessage()
    rulesOfGame()

    game = RockPaperScissorGame()

    print("To start the game, Please Enter Your First Name: ", end="")
    game.username = str(input())

    while game.next_turn:
        gameOption()

        game.userTurn()

        game.computerTurn()

        game.gameDetails()

        game.chooseWinner()

        game.setValueForNextTurn()
