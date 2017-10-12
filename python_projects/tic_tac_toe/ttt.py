board = [[' ',' ',' '],
         [' ',' ',' '],
         [' ',' ',' ']]


def pb(board):
    for i in board:
        print i

def full_board(board):
    for row in board:
        for element in row:
            if element == ' ':
                return False

    return True

def check_board(board,marker):
    #row check
    for lst in board:
        if lst.count(marker) == 3:
            print "row check"
            return True

    #col check
    colmat =[[row[i] for row in board] for i in range(3)]
    for lst in colmat:
        if lst.count(marker) == 3:
            print "colcheck"
            return True

    #down diag checks
    if (board[0][0]== marker and board[1][1])==marker and board[2][2]==marker:
        print "diag1"
        return True
    #up diag check
    if (board[2][0]==marker and board[1][1]==marker and board[0][2]==marker):
        print "diag2"
        return True


def start_game():
    print "Welcome to tic-tac-toe!"
    player1 = raw_input('Enter Player 1 name: ')
    player2 = raw_input("Enter Player 2 name: ")

    while(True):
        #Player 1
        move1 = (raw_input("%s's move: " %player1))

        move1 = move1.split(",")
        row1=int(move1[0])
        col1=int(move1[1])

        if (board[row1][col1]==' '):
            board[row1][col1]='X'
            pb(board)
            print "\n"

        if(check_board(board,'X')):
            print "%s Wins!" %player1
            return 0

        if full_board(board):
            print "no winners, board is full"
            return 0

        #Player 2
        move2 = (raw_input("%s's move: " %player2))
        move2 = move2.split(",")
        row1=int(move2[0])
        col1=int(move2[1])

        if (board[row1][col1] == ' '):
            board[row1][col1] = 'O'
            pb(board)
            print ""

        if (check_board(board,'O')):
            print "%s Wins!" %player2
            return 0;

        if full_board(board):
            print "no winners, board is full"
            return 0

start_game()
pb(board)

