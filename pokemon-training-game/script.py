from PokemonTrainingGame import PokemonTrainingGame

def welcomeMessage():
    print("Welcome to the Pokemon Training Game", end="\n\n")
    print("You will get two options as you move forward.")
    print("1. Catch The Pokemon [C]")
    print("2. Exit The Program [E]")

if __name__ == "__main__":
    welcomeMessage()

    game = PokemonTrainingGame()

    while True:
        print("\nPlease enter your choice [C/E]")
        print("> ", end="")
        game.user_choice = str(input())

        if game.user_choice == True:
            print("\nEnter the power of the pokemon you caught: ", end="")
            game.powers = int(input())
            game.calculateMinimumMaximumPower()
            print(f"\nMimumum Power: {game.min_power}, Maximum Power: {game.max_power}")
        else:
            print("Exiting the game ...")
            exit()