import random


def draw_board(board):
    print("-------------")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("-------------")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("-------------")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    print("-------------")


def check_win(board, player):
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True

    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True

    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

def get_user_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move >= 1 and move <= 9 and board[move-1] == " ":
                return move - 1
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_computer_move(board):
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_win(board, "O"):
                return i
            else:
                board[i] = " "

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_win(board, "X"):
                return i
            else:
                board[i] = " "

    while True:
        move = random.randint(0, 8)
        if board[move] == " ":
            return move


def play_game():
    board = [" "] * 9
    current_player = "X"

    while True:
        draw_board(board)

        if current_player == "X":
            move = get_user_move(board)
            board[move] = "X"
        else:
            move = get_computer_move(board)
            board[move] = "O"

        if check_win(board, current_player):
            draw_board(board)
            print(current_player + " wins!")
            break
        elif " " not in board:
            draw_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"


play_game()
