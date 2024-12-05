####################################################################################################
# Rock Paper Scissors game run through the console.
####################################################################################################
import os, random
from art import draw

choices = ["rock","paper","scissors"]

def determine_winner(player, opp):
    # Check if its a tie
    if player == opp:
        return ("It's a tie game!")
    # Check if the player won
    elif ((player == "rock" and opp == "scissors") or 
          (player == "paper" and opp == "rock") or 
          (player == "scissors" and opp == "paper")):
            return ("You won, congrats!")
    else:
        return("You lost, sorry!") 

playing, invalid = True, False

while playing:
    if not invalid:
        #Clear the screen
        os.system('cls')
        print("Choose rock, paper or scissors") # Ask the player to make a selection
    else:
        # Let them know if their choice was invalid
        print("Invalid input, please type rock, paper or scissors")
        invalid = False

    print("Or enter q to quit")

    player_choice = input().lower().strip() #Get the player input, make lowercase and remove any whitespace
    # Generate a random choice for the computer using our list of values
    opp_choice = random.choice(choices)
    # Check and see if the player made a valid entry
    if player_choice in choices:
        print("You chose: "+ player_choice + draw(player_choice))
        print("The opponent chose: "+ opp_choice + draw(opp_choice))
        print(determine_winner(player_choice, opp_choice))
    # End the loop if the player wants to leave
    elif player_choice == "q":
        playing = False
    else:
        invalid = True

    if playing and not invalid:
        replay = input("Do you want to play again? \"yes\" to replay, enter anything else to end the game\n").lower().strip()
        print()
        playing = replay == "yes"
    
    #Clear the screen
    os.system('cls')
print("Thanks for playing.")