def invert(num):
    return 3 - num

board = ['-'] * 9
a = {1: 'X', 2: 'O'}

def check_win():
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != '-':
            return True
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != '-':
            return True
    if board[0] == board[4] == board[8] != '-' or board[2] == board[4] == board[6] != '-':
        return True
    return False

def game():
    game_over = False
    player = 2
    while not game_over:
        player = invert(player)
        w = a[player]
        x = int(input(f'{w} say a number: '))
        row = x - 1
        if row < 0 or row >= 9 or board[row] != '-':
            print('Invalid move')
            player=invert(player)
        else:
            board[row] = a[player]
            if check_win():
                print(f'Game Over {w} won')
                game_over = True

# Start the game

print(game())



    

