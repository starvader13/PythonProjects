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

    print("To start the game, Please Enter Your First Name: ", end="")
    game.username = str(input())

    while game.next_turn:
        print("\nChoose From the option:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissor")
        print("> ", end="")

        game.user_input = int(input())
        print(f"\nUser Choice is: {game.user_input}")

        print("\n Computer's Turn ... ", end="\n\n")
        game.computer_input = game.intializeComputerInput()
        print(f"\nComputer Choice is: {game.computer_input}", end = "\n\n")

        print(f"Game: {game.user_input} vs {game.computer_input}", end = "\n\n")
        game.chooseWinner()

        game.setValueForNextTurn()
