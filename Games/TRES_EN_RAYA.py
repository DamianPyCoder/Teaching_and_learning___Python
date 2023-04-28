import os
import random
from colorama import init, Fore

# Inicializar colorama
init()

# Definir los colores para los jugadores
player_one_color = Fore.BLUE
player_two_color = Fore.GREEN
play = True

def print_board(board):
    print("  0 1 2")
    for i in range(len(board)):
        row = str(i) + " "
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
        row = int(input("Ingrese la fila: "))
        col = int(input("Ingrese la columna: "))
        if board[row][col] == 0:
            board[row][col] = 1
            break
        else:
            print("Posición ya utilizada. Intente de nuevo.")
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la pantalla después del movimiento

def computer_move(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == 0:
            board[row][col] = 2
            break
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la pantalla después del movimiento

while play==True:
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    while True:
        print_board(board)

        player_move(board)

        if check_win(board, 1):
            print(player_one_color + "Felicidades, ¡ganaste!" + Fore.RESET)
            break

        computer_move(board)

        if check_win(board, 2):
            print(player_two_color + "Lo siento, has perdido!" + Fore.RESET)
            break

    play_again = input("¿Quieres jugar de nuevo? (Y/N)")

    if play_again.upper() == 'Y':
        os.system('cls' if os.name == 'nt' else 'clear')
    elif play_again.upper()=='N':
        play= False

