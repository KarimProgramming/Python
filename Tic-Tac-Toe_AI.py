#This is an AI that can play XO with the minimax algorithm
#This is the game
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

def game_computer():
    human=int(input('Type 1 to be X, 2 to be O '))
    comp=3-human
    game_over = False
    player = 2
    while not game_over:
        player = invert(player)
        w = a[player]
        if player==human:
            x = int(input(f'{w} say a number: '))
        elif player==comp:
            x=get_move(board)
            print(f'The computer played {x} ')
        row = x - 1
        if row < 0 or row >= 9 or board[row] != '-':
            print('Invalid move')
            player=invert(player)
        else:
            board[row] = a[player]
            if check_win():
                print(f'Game Over {w} won')
                game_over = True
def game():
    game_over = False
    player = 2
    while not game_over:
        player = invert(player)
        w = a[player]
        x=int(input(f'Player {w}, say a number: '))
        row = x - 1
        if row < 0 or row >= 9 or board[row] != '-':
            print('Invalid move')
            player=invert(player)
        else:
            board[row] = a[player]
            if check_win():
                print(f'Game Over, {w} won')
                game_over = True
def evaluate(board):
    if check_win():
        return 1  # The computer wins
    elif '-' not in board:
        return 0  # It's a draw
    else:
        return -1  # The computer didn't win, and it's not a draw

def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    if score != -1:  # Terminal node
        return score

    if is_maximizing:
        best_score = float('-inf')
        for i in range(len(board)):
            if board[i] == '-':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = '-'
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(len(board)):
            if board[i] == '-':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = '-'
                best_score = min(score, best_score)
        return best_score

def get_move(board):
    best_score = float('-inf')
    best_move = -1
    for i in range(len(board)):
        if board[i] == '-':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = '-'
            if score > best_score:
                best_score = score
                best_move = i
    return best_move + 1
game_computer()
