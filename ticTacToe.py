def printGameBoard(board):
    print("\n")
    print("   0   1   2")
    print("0 ", board[0][0], " ", board[0][1], " ", board[0][2])
    print("1 ", board[1][0], " ", board[1][1], " ", board[1][2])
    print("2 ", board[2][0], " ", board[2][1], " ", board[2][2], "\n")
    return

def playerTurn(board, player, name):
    print("Player ", name, " please input the coordinates of your move, in the format Row Column (Example: 0 1)")
    x, y = [int(x) for x in input().split()]
    while True:
        if board[x][y] != "-" or x > 2 or y > 2:
            print("Invalid location, please try again")
            x, y = [int(x) for x in input().split()]
            continue
        else:
            board[x][y] = player
            printGameBoard(board)
            break
    return checkVictory(board,player,x,y)

def checkVictory(board, player, x, y):
    #Check if previous move casued a vertical victory
    if board[0][y] == board[1][y] == board[2][y]:
        return True
    
    #Check if previous move caused a horizontal victory
    if board[x][0] == board[x][1] == board[x][2]:
        return True
    
    #Check if previous move caused a main diagonal victory
    if x == y and board[0][0] == board[1][1] == board[2][2]:
        return True
    
    #Check if previous move caused a secondary diagonal victory
    if x+y == 2 and board[0][2] == board[1][1] == board [2][0]:
        return True

    return False

def playTicTacToe():
    #Establish who is X and who is O
    print("Player 1, would you like to be X or O?")
    playerOne = input()

    #Check for valid input
    while True:
        if playerOne != "X" and playerOne != "O":
            print("Invalid input, Player 1, please select X or O.")
            playerOne = input()
            continue
        else:
            if(playerOne == "X"):
                playerTwo = "O"
            else:
                playerTwo = "X"
            break
        
    #Create the initial game board
    gameBoard = [["-","-","-"],["-","-","-"],["-","-","-"]]

    #Print initial game board to console
    printGameBoard(gameBoard)

    #Create the victory check
    victory = False
    moveCount = 0

    #Until someone wins or 9 moves have been played
    while True:
        #Have player one make a move
        victory = playerTurn(gameBoard, playerOne, "One")
        printGameBoard(gameBoard)
        if(victory == True):
            print("Player One is the victor!")
            break
        moveCount += 1

        #Check if there has been a tie, which will only ever occur after player 1 goes
        if moveCount >= 9:
            print("The game ends in a tie.")
            break

        #Have player two make a move
        victory = playerTurn(gameBoard, playerTwo, "Two")
        printGameBoard(gameBoard)
        if(victory == True):
            print("Player Two is the victor!")
            break
        moveCount += 1

    return

playTicTacToe()



