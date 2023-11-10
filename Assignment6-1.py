def show():
    for row in game_board:
        for cell in row:
            print(cell, end=" ")
        print()

def check():
    if game_board[0][0] == "O" and game_board[0][1] == "O" and game_board[0][2] == "O":
        print("Player1 win!")
    if game_board[1][0] == "O" and game_board[1][1] == "O" and game_board[1][2] == "O":
        print("Player1 win!")
    if game_board[2][0] == "O" and game_board[2][1] == "O" and game_board[2][2] == "O":
        print("Player1 win!")
    if game_board[0][0] == "O" and game_board[1][0] == "O" and game_board[2][0] == "O":
        print("Player1 win!")
    if game_board[0][1] == "O" and game_board[1][1] == "O" and game_board[2][1] == "O":
        print("Player1 win!")
    if game_board[0][2] == "O" and game_board[1][2] == "O" and game_board[2][2] == "O":
        print("Player1 win!")
    if game_board[0][0] == "O" and game_board[1][1] == "O" and game_board[2][2] == "O":
        print("Player1 win!")
    if game_board[0][2] == "O" and game_board[1][1] == "O" and game_board[2][0] == "O":
        print("Player1 win!")
# ------------------------------------------------------------------------------------------
    if game_board[0][0] == "X" and game_board[0][1] == "X" and game_board[0][2] == "X":
        print("Player2 win!")
    if game_board[1][0] == "X" and game_board[1][1] == "X" and game_board[1][2] == "X":
        print("Player2 win!")
    if game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X":
        print("Player2 win!")
    if game_board[0][0] == "X" and game_board[1][0] == "X" and game_board[2][0] == "X":
        print("Player2 win!")
    if game_board[0][1] == "X" and game_board[1][1] == "X" and game_board[2][1] == "X":
        print("Player2 win!")
    if game_board[0][2] == "X" and game_board[1][2] == "X" and game_board[2][2] == "X":
        print("Player2 win!")
    if game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X":
        print("Player2 win!")
    if game_board[0][2] == "X" and game_board[1][1] == "X" and game_board[2][0] == "X":
        print("Player2 win!")

game_board = [["-","-","-"],
              ["-","-","-"],
              ["-","-","-"]]
# print(game_board)
show()
while True:
    print("Player1") # => O
    while True:
            row = int(input("Enter row: "))
            col = int(input("Enter col: "))
            if 0<= row <=2 and 0<= col <=2:
                if game_board[row][col] == "-":
                    game_board[row][col] = "O" 
                    show()
                    check()
                    break
                else:
                    print("Enter another numbers!")
            else:
                print("Enter a number between 0 & 2 !")

    if game_board[0][0] != "-" and game_board[0][1] != "-" and game_board[0][2] != "-" and game_board[1][0] != "-" and game_board[1][1] != "-" and game_board[1][2] != "-" and game_board[2][0] != "-" and game_board[2][1] != "-" and game_board[2][2] != "-" and check() != True:
                print("It's a draw!")
                break

    print("Player2") # => X
    while True:
            row = int(input("Enter row: "))
            col = int(input("Enter col: "))
            if 0<= row <=2 and 0<= col <=2:
                if game_board[row][col] == "-":
                    game_board[row][col] = "X"
                    show()
                    check()
                    break
                else:
                    print("Enter another numbers!")
            else:
                print("Enter a number between 0 & 2 !")

    if game_board[0][0] != "-" and game_board[0][1] != "-" and game_board[0][2] != "-" and game_board[1][0] != "-" and game_board[1][1] != "-" and game_board[1][2] != "-" and game_board[2][0] != "-" and game_board[2][1] != "-" and game_board[2][2] != "-" and check() != True:
        print("It's a draw!")
    if check() == True:
        break