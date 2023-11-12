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
        # print("Please enter your choice [C/E]")
        # game.user_choice = str(input())

        game.powers = int(input())
        game.calculateMinimumMaximumPower()
        print(game.min_power, game.max_power)