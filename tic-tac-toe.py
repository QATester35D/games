####################################################################################################
#Tic Tac Toe
####################################################################################################
def drawBoard(spots):
    board=(f"|{spots[1]}|{spots[2]}|{spots[3]}|\n|{spots[4]}|{spots[5]}|{spots[6]}|\n|{spots[7]}|{spots[8]}|{spots[9]}|")
    print(board)

def check_turn(turn):
    if turn % 2 == 0:
        return "O"
    else:
        return "X"

spots={1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9"}
playing=True
turn = 0
while playing:
    # os.system("cls" if os.name == "nt" else "clear")
    os.system("cls")
    drawBoard(spots)
    choice=input("Select a spot or type q to quit: ")
    if choice == "q":
        playing = False
    elif str.isdigit(choice) and int(choice) in spots:
        if not spots[int(choice)] in {"X","O"}:

    turn+=1
    spots[int(choice)] = check_turn(turn)