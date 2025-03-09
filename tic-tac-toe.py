####################################################################################################
# Tic-Tac-Toe game run through the console.
####################################################################################################
import os
from helpers import drawBoard, check_turn, check_for_win

#Dictionary for each spot on the game board (key/value pairs)
spots={1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9"}
playing=True
complete=False
turn = 0
prevTurn= -1
while playing:
    os.system("cls") #"clear screen" on the windows platform; applies to the console
    drawBoard(spots)
    if prevTurn == turn: #if an invalid turn occurred, let the player know
        print("Invalid spot selected, please pick another.")
    prevTurn = turn
        # Next print line: uses the modulo (mod or %) operation - it is the remainder when dividng
        # On the first turn the mod will evaluate to zero, add 1 to identify player "1".
        #   Thereafter all even numbers have a remainder of zero, adding 1 identifies player "1"
        #   All odd numbers have a remainder of 1, adding a 1 identifies Player "2"
    # print("Player " + str((turn % 2) +1 ) + "'s turn: Pick your spot or press q to quit")
    print("Player " + str((turn % 2) +1 ) + "'s turn: ")  
    spotSelection=input("Select a tic-tac-toe spot on the board OR type q to quit: ") #Get a value from the player in the console
        #elif line below: str.isdigit() checks if all the characters in a string are digits(0-9)
        #  int(spotSelection) checks to make sure the digit is in the spots dictionary
    if spotSelection in ("q","Q"):
        playing = False #done playing, exit the game
    elif str.isdigit(spotSelection) and int(spotSelection) in spots:
        if not spots[int(spotSelection)] in {"X","O"}: #Check if the spot has already been taken/used
            turn+=1
            spots[int(spotSelection)] = check_turn(turn) #get the X or O value to enter in the spot
    
    #Check if the game has ended with someone winning or not, if True we're done
    if check_for_win(spots):
        playing, complete = False, True
    
    if turn > 8: playing = False

#Outside of the loop, print the results. Draw the board one last time for end of game
os.system("cls")
drawBoard(spots)
#If there was a winner then say who won the game
if complete:
    if check_turn(turn) == "X":
        print ("Player 1 WINS!")
    else:
        print ("Player 2 WINS!")
else:
    #There was a tie game
    print("The game ended in a tie, there was no winner (sad face)")

print("Thanks for playing, come again (tips are greatly appreciated).")