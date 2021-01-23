def print_board(board):
    #Hien thi board len man hinh
    board_format = ""
    for i in range(0, len(board)):
        if i % 3 == 0:
            board_format = board_format + "\n"
        board_format = board_format + board[i] + "|"
    print(board_format)
    #ket thuc hien thi
def row(board,start, mark):
    #1,4,7

    return board[start] == mark and board[start + 1] == mark and board[start + 2] == mark

def column(board,start, mark):
    #1,2,3
    return board[start] == mark and board[start + 3] == mark and board[start + 6] == mark
def diagonal_1(board, start, mark):
    #1, 3
    return board[start] == mark and board[start + 4] == mark and board[start + 8] == mark
def diagonal_2(board, start, mark):
    return board[start] == mark and board[start + 2] == mark and board[start + 4] == mark

def is_draw(board):
        for mark in board:
            if mark != "X" and mark != "O":
                return False
        return True

def game_continue(board):
    for mark in ["O", "X"]:
        if row(board, 0, mark) or row(board, 3, mark) or row(board, 6,mark):
            return False
        if column(board, 0, mark) or column(board, 1, mark) or column(board, 2,mark):
            return False
        if diagonal_1(board, 0, mark) or diagonal_2(board, 2, mark):
            return False
    if is_draw(board):
        return False

    return True
if __name__ =="__main__":
        print("Welcome to Tic Tac Toe")

        print("Choose player, typy X or O")
        player_1 = input().upper()

        if player_1 == "X":
            player_2 = "O"
            current_player = player_1
        elif player_1 == "O":
            player_2 = "X"
            current_player = player_2

        print("player_1:",player_1)
        print("player_2:",player_2)

        board = [" "] * 9
        for i in range(0,9):
            board[i]  = str(i + 1)
        print_board(board)
        print("Type from 1 - 9 to mark your move")
        while True :
            print("Player", current_player, "turn:")

            move = int(input())

            board[move - 1 ] = current_player

            print_board(board)

            if not game_continue(board):
                break

            if current_player == player_1:
                current_player = player_2
            elif current_player == player_2:
                current_player = player_1
        print ("Winner is Player", current_player)
            if is_draw()
