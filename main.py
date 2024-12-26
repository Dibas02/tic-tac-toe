theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' ',}

board_keys = []

for key in theBoard:
    board_keys.append(key)


def printBoard(board):
    print(board['7'] + '|' + board['8'] + "|" + board['9'] )
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + "|" + board['6'] )
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + "|" + board['3'] )
    

def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("It's your turn " + turn + " Where do you want to move?")


        move = input()


        if theBoard[move] == ' ':
            theBoard[move] = turn
            count+=1

        else:
            print("Your selected cell is already filled. Please choose another one...")
            continue


        if count >=5:
            if theBoard['7'] == theBoard['8'] ==theBoard['9'] == ' ':
                print("Game Over")
                print('****' + turn + " has won****")
                break

            elif theBoard['4'] == theBoard['5'] ==theBoard['6'] == ' ':
                print("Game Over")
                print('****' + turn + " has won****")
                break

            elif theBoard['1'] == theBoard['2'] ==theBoard['3'] == ' ':
                print("Game Over")
                print('****' + turn + " has won****")
                break

            elif theBoard['1'] == theBoard['4'] ==theBoard['7'] == ' ':
                print("Game Over")
                print('****' + turn + " has won****")
                break

            elif theBoard['2'] == theBoard['5'] ==theBoard['8'] == ' ':
                print("Game Over")
                print('****' + turn + " has won****")
                break

            elif theBoard['3'] == theBoard['6'] ==theBoard['9'] == ' ':
                print("Game Over")
                print('****' + turn + " has won****")
                break

            elif theBoard['1'] == theBoard['5'] ==theBoard['9'] == ' ':
                print("Game Over")
                print('****' + turn + " has won****")
                break

            elif theBoard['3'] == theBoard['5'] ==theBoard['7'] == ' ':
                print("Game Over")
                print('****' + turn + "has won ****")
                break

        if count == 9:
            print("It's a tie")
            break

        if turn == 'X':
            turn = 'O'
        else:
            turn = "X"

    restart = input("Would you like to restart?: ")
    if restart.lower() == 'y':
        print("Game restarted...")
        for key in board_keys:
            theBoard[key] = ' '
        game()
game()
