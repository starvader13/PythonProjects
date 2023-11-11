from flames import Flames

def welcomeMessage():
    print("Welcome to the FLAMES.")
    print("To start the game. Enter the details as needed.", end="\n\n")

if __name__ == "__main__": 
    welcomeMessage()
    game = Flames()

    print("Enter the name of the first user:", end=" ")
    game.first_user = str(input())

    print("Enter the name of the second user:", end=" ")
    game.second_user = str(input())
    
    print("\nOutput:\nRELATIONSHIP STATUS: ", end="")
    game.calculateFlames()    