import random
def get_choices():
    player_choice = input("Enter a choice (rock, paper, or scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}.")
    if player == computer:
        return "It's a tie."  #If a return statement runs true, every other line of code or action under that function is abolished.
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"  #return statements must not have brackets. They are optional.
        else:
            return "Paper covers rock! You lose."
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose."
    else:
        if computer == "rock":
            return "Rock smashes scissors! You lose."
        else:
            return "Scissors cuts paper! You win!"

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
# choices["player"] is a way to call or refer to a dictionary key-value pair 
# It follows the syntax convention --> name_of_dictionary[name_of_key]
print(result)

