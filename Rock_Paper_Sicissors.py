import random


def get_choices():
    player_choice = input("Enter a choice (Rock, Paper or Scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"Player": player_choice, "Computer": computer_choice}
    return choices

def check_win(player, computer):
    player = player.lower()
    if player == computer:
        return ("It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            return ("Rock smashes scissors!You win!")
        else:
            return ("Paper covers Rock!You lose.")
    elif player == "paper":
        if computer == "rock":
            return ("Paper covers rock!You win!")
        else:
            return ("Scissors cuts paper!You lose.")
    elif player == "scissors":
        if computer == "paper":
            return ("Scissors cuts paper!You win!")
        else:
            return ("Rock smashes scissors! You lose")

def main():        
    while True:       
        choices = get_choices()
        result = check_win(choices ["Player"], choices ["Computer"])
        print (result)

        while True:
            replay = input("Do you want to play again? ").lower()
            if replay == "yes":
                break
            elif replay == "no":
                print("Bye!")
                return
            else:
                print("Enter Yes or No!")

main()