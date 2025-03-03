import  os


def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def show_board(board):
    print("-------")
    for i in range(3):
        for j in range(3):
            print(f"|{board[i][j]}", end='')
        print("|")
        print("-------")


def check_winner(board):
    # check rows
    for s in board:
        if s[0] == s[1] == s[2] and s[0] != ' ':
            return True

    # check cols
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return True

    #  check diagonals
    if board[0][0] == board[1][1] == board[2][2] \
            or board[0][2] == board[1][1] == board[2][0]:
        return True

def positional_number(num):
    if num == 7: return 1
    if num == 8: return 2
    if num == 9: return 3
    if num == 1: return 7
    if num == 2: return 8
    if num == 3: return 9
    return num

counter = 0
board = [[' '] * 3 for i in range(3)]
show_board(board)
user = 'X'
while counter < 9:
    print(f"Next move: {user}, Enter position [1-9]: ", end='')
    val = int(input())
    val = positional_number(val)
    clear_console()
    x = (val-1) // 3
    y = (val-1) % 3
    if x < 0 or x >= 3:
        print("Wrong input. try again.")
    else:
        if board[x][y] == ' ':
            board[x][y] = user
            if counter >= 4:
                if check_winner(board):
                    show_board(board)
                    print(f"{user} is winner.")
                    break
            counter += 1
        else:
            print("Already exist, try another position.")

    if counter%2:
        user = 'O'
    else: user = 'X'

    show_board(board)
    if counter == 9:
        print("Draw!")
