import math


def print_board(board):
    board_format =" "

    for i in range(0, len(board)):
        if i % (math.sqrt(len(board))) == 0:
            board_format = board_format + "\n"
        board_format = board_format + prepend_zeroes(board[i],2) +"|"
        #board_format = board_format + board[i] +"|"

    print(board_format)


def row(board, start, mark):

    count = 1
    for i in range(1, int(math.sqrt(len(board)))):
        if board[start + i] == mark and board[start + i] == board[start + i - 1]:
            count += 1
    return count == math.sqrt(len(board))

def column(board, start, mark):

    count = 1
    for i in range(1, int(math.sqrt(len(board)))):

        if  board[start + i * int(math.sqrt(len(board)))] == mark and board[start + i * int(math.sqrt(len(board)))] == board[start + (i - 1) * int(math.sqrt(len(board)))]:
            count += 1



    return count == math.sqrt(len(board))

def diagonal_1(board, start, mark):

    count = 1
    for i in range(1, int(math.sqrt(len(board)))):
        if board[start + i*(int(math.sqrt(len(board))+1))] == mark and board[start + i*(int(math.sqrt(len(board)))+1)] == board[start + (i-1)*(int(math.sqrt(len(board))+1))]:
            count += 1
    return count == math.sqrt(len(board))

def diagonal_2(board, start, mark):

    count = 1
    for i in range(1, int(math.sqrt(len(board)))):

        if  board[(start + i * (int(math.sqrt(len(board)))-1))] == mark and board[(start + i * (int(math.sqrt(len(board)))-1))] == board[start + (i-1) * (int(math.sqrt(len(board)))-1)]:
            count += 1
    return count == math.sqrt(len(board))
def is_draw(board):
    for i in range(0, len(board)):
        if board[i] != "O" and board[i] != "X":
            return False
    return True

def game_continue(board):
    for mark in ["O","X"]:
        for i in range(0, int(math.sqrt(len(board)))):
            if row(board, i * int(math.sqrt(len(board))) ,mark) :
                return False
            if column(board, i , mark) :
                return False
        if diagonal_1 (board, 0 , mark):

            return False
        if diagonal_2 (board, int(math.sqrt(len(board))) - 1 , mark):
            return False


    return not is_draw(board) # return True

def prepend_zeroes(num,digit):


     if digit == len(num):
         return num
     if digit >= len(num):
         a = digit - len(num)
         for i in range (0, a ):
             num = " " + num
         return num


if __name__ == "__main__" :

    #tạo 2 người chơi, tại dòng

    print("Welcome to Tic Tac Toe")
    print("Choose player, type X or O \nChoose X if you want go first")
    """Get Player """

    while True:
        player_1= input().upper()
        if player_1 == "X":
            player_2 = "O"
            current_player = player_1
            break
        elif player_1== "O":
            player_2 = "X"
            current_player = player_2
            break
        else:
            print("Please Choose Again !!!")
            continue

    print("Player 1 : ", player_1)
    print("Player 2 : ", player_2)

    #Nhập và Hiển thị board lên màn hình
    print("ENTER YOUR SIZE ")

    size = int(input())
    board = [" "] *size *size

    #tạo số hiển thị trên board

    for i in range(0, len(board)):
        board[i] = str(i+1)



    print_board(board)

    print("\nType from 1-"+ str(len(board)) +" to mark your move\n")

    print_board(board)

    while game_continue(board):

        print("Player",current_player,"turn :")
        try :
            move = int(input())
        except Exception as e:

            print("Choose 1 - "+ str(len(board)) +" for each turn")

            print_board(board)
            continue


        if move >=1 and move <= len(board) :
            if board[move - 1] == "O" or board[move -1] == "X":

                print("Your place had been chosen")
                print("Pls , choose again !")

                print_board(board)

                continue
            board[move - 1] = current_player

        else:
            print("Eror, Try Again!!")
            print_board(board)
            continue




        print(move)
        # hien thi bảng để add số vào vị trí :

        print_board(board)

        if not game_continue(board):
            break

        #luân phiên 2 ng chơi
        if current_player == player_1:
            current_player = player_2
        elif current_player == player_2:
            current_player = player_1

        #trường hợp - thắng/thua/hòa -
    if is_draw(board):
        print("\nDRAW")
    else:
        print("\nWinner is : ",current_player)
