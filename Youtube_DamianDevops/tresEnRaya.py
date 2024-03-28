import os
import random
from colorama import init, Fore
import getpass

# Inicializar colorama
init()

# Definir los colores para los jugadores
player_one_color = Fore.BLUE
player_two_color = Fore.GREEN
play = True

def print_board(board):
    print("  0 1 2")
    rows = ['A', 'B', 'C']
    for i in range(len(board)):
        row = rows[i] + " "
        for j in range(len(board[i])):
            if board[i][j] == 0:
                row += "-"
            elif board[i][j] == 1:
                row += player_one_color + "O" + Fore.RESET
            else:
                row += player_two_color + "O" + Fore.RESET
            if j != len(board[i]) - 1:
                row += "|"
        print(row)

def check_win(board, player):
    # Horizontal win
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    # Vertical win
    for j in range(3):
        if board[0][j] == player and board[1][j] == player and board[2][j] == player:
            return True
    # Diagonal win
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def player_move(board):
    while True:
        row_input = input("Ingrese la fila (A, B o C): ")
        row = ord(row_input.upper()) - ord('A')
        col = int(input("Ingrese la columna: "))
        if board[row][col] == 0:
            board[row][col] = 1
            break
        else:
            print("Posición ya utilizada. Intente de nuevo.")
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la pantalla después del movimiento

def computer_move(board):
    best_score = float('-inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = 2
                score = minimax(board, 0, False)
                board[i][j] = 0
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    if best_move is not None:
        row, col = best_move
        board[row][col] = 2
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la pantalla después del movimiento

def minimax(board, depth, is_maximizing):
    if check_win(board, 2):
        return 1
    elif check_win(board, 1):
        return -1
    elif check_draw(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 2
                    score = minimax(board, depth + 1, False)
                    board[i][j] = 0
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 1
                    score = minimax(board, depth + 1, True)
                    board[i][j] = 0
                    best_score = min(score, best_score)
        return best_score

def check_draw(board):
    for row in board:
        if 0 in row:
            return False
    return True

def get_username():
    if os.name == 'nt':  # Windows
        return os.environ.get('USERNAME')
    else:  # Linux
        return getpass.getuser()

while play:
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    while True:
        print_board(board)

        player_move(board)

        if check_win(board, 1):
            print(player_one_color + f"Felicidades, {get_username()}, ¡ganaste!" + Fore.RESET)
            break

        computer_move(board)

        if check_win(board, 2):
            print(player_two_color + f"Lo siento, {get_username()}, has perdido!" + Fore.RESET)
            break
        if check_draw(board):
            print("¡Empate!")
            break

    play_again = input("¿Quieres jugar de nuevo? (Y/N)")

    if play_again.upper() == 'Y':
        os.system('cls' if os.name == 'nt' else 'clear')
    elif play_again.upper() == 'N':
        play = False
