#!/usr/bin/env python3

board = [["_" for i in range(3)] for j in range(3)]
characters_to_replace = [" ", ",", "."]
turn_number = 0
players = ["O", "X"]
win = False
def check_for_win(board):
    if board[0][0] == board[0][1] and board[0][0] == board[0][2] and (not board[0][0] ==  "_"):
        return True
    elif board[1][0] == board [1][1] and board[1][0] == board[1][2] and (not board[1][0] ==  "_"):
        return True
    elif board[2][0] == board [2][1] and board[2][0] == board[2][2] and (not board[2][0] ==  "_"):
        return True
    elif board[0][0] == board[1][1] and board[0][0] == board[2][2] and (not board[0][0] == "_"):
        return True
    elif board[2][0] == board[1][1] and board[2][0] == board[0][2] and (not board[2][0] == "_"):
        return True
    elif board[0][0] == board[1][0] and board[0][0] == board[2][0] and (not board[0][0] == "_"):
        return True
    elif board[0][1] == board[1][1] and board[0][1] == board[2][1] and (not board[0][1] == "_"):
        return True
    elif board[0][2] == board[1][2] and board[0][2] == board[2][2] and (not board[2][2] == "_"):
        return True
    else:
        return False


def check_for_free(board, row, column):
    if board[row][column] == "_":
        return True
    else:
        return False


while not win:
    player_input = input(f"Player {(turn_number % 2)+1} chose position to mark. First row then column: ")
    row = int(player_input[0])-1
    column = int(player_input[-1])-1
    if check_for_free(board, row, column):
        board[row][column] = players[turn_number % 2]
        if check_for_win(board=board):
            print(f"Player {(turn_number % 2)+1} won. Well Done!")
            win == True
            break
        else:
            turn_number += 1
            print(board)
    else:
        print("Oops! Sorry This Space is Already occupied")
        print(board)