from TwentyPlusOneGame import TwentyPLusOneGame

def WaitingMessage():
    print("Welcome to the \"TWENTY PLUS ONE GAME\".")
    print("You are Player 1.Computer is Player 2", end="\n\n")

    print("Do you want to start the game?")
    print("> ",end="")


game = TwentyPLusOneGame()

WaitingMessage()

game.start = str(input())
game.checkStart()

print("\nIf you want to start first press F otherwise press S: ")
print("> ",end="")
game.user_playing_position = str(input())

# if game.user_playing_position == True:
#     game.userChance()
# else:
#     game.computerChance()

while game.checkListElement():
    if game.user_playing_position == True:
        game.userChance()
        game.user_playing_position = "S"
    else:
        game.computerChance()
        game.user_playing_position = "F"

    game.checkLoseGame()
    print(game.count_list)