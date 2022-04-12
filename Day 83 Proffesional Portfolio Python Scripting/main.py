board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

print(f"{board[0]} | {board[1]} | {board[2]}         1 | 2 | 3\n"
      f"{board[3]} | {board[4]} | {board[5]}         4 | 5 | 6\n"
      f"{board[6]} | {board[7]} | {board[8]}         7 | 8 | 9")

def player_choice(player):
    choice = int(input(f"Please choose a number Player({player}): "))-1
    if board[choice] == "-":
        board[choice] = player
        print(f"{board[0]} | {board[1]} | {board[2]}         1 | 2 | 3\n"
              f"{board[3]} | {board[4]} | {board[5]}         4 | 5 | 6\n"
              f"{board[6]} | {board[7]} | {board[8]}         7 | 8 | 9")
    else:
        print("Choose another number:")
        player_choice(player)

def player_turn(player):
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"
    return player

def game_end(player):
    if board[0] == board[1] == board[2] != "-" or board[3] == board[4] == board[5] != "-" or board[6] == board[7] == board[8] != "-":
        print(f"Player:({player}) won!")
        return True
    elif board[0] == board[3] == board[6] !="-" or board[1] == board[4] == board[7] !="-" or board[2] == board[5] == board[8] !="-":
        print(f"Player:({player}) won!")
        return True
    elif board[0] == board[4] == board[8] !="-" or board[2] == board[4] == board[6] !="-":
        print(f"Player:({player}) won!")
        return True
    elif board[0] and board[1] and board[2] and board[3] and board[4] and board[5] and board[6] and board[7] and board[8] != "-":
        print("The Game is a Tie.")
        return True

def game_on():
    game = True
    player = "X"
    while game:
        player_choice(player)
        end = game_end(player)
        if end == True:
            game = False
        player = player_turn(player)

game_on()