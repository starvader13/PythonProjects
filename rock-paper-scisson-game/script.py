from RockPaperScissorGame import RockPaperScissorGame

def welcomeMessage():
    print("Welcome to the Rock, Paper and Scissor Game", end="\n\n")

def rulesOfGame():
    print("Rules of the Game !!!")
    print("Rock vs Paper -> Paper Wins")
    print("Rock vs Scissor -> Rock Wins")
    print("Scissor vs Paper -> Scissor Wins.", end="\n\n")

if __name__ == "__main__":
    welcomeMessage()
    rulesOfGame()

    game = RockPaperScissorGame()

    print("Choose From the option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")
    print("> ", end="")

    game.user_input = int(input())
    game.computer_input = game.intializeComputerInput()

    print(game.user_input)
    print(game.computer_input)

