import colorama
from colorama import init, Fore, Back, Style
init()

PLAYER_1_COLOR = Fore.GREEN
PLAYER_2_COLOR = Fore.YELLOW

# Inicializamos colorama para que podamos imprimir texto con colores
colorama.init()

# Definimos el tablero como una lista de listas, con 0 para las casillas vacías, 1 para las fichas blancas y 2 para las fichas rojas
board = [
    [0, 2, 0, 2, 0, 2, 0, 2],
    [2, 0, 2, 0, 2, 0, 2, 0],
    [0, 2, 0, 2, 0, 2, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0]
]

# Función para imprimir el tablero en la consola
def print_board():
    print(" ")
    print("  0  1 2 3 4 5 6 7")
    for row in range(len(board)):
        print(row, end=" ")
        for col in range(len(board[row])):
            if board[row][col] == 0:
                print(Back.BLACK + "  ", end="")
            elif board[row][col] == 1:
                print(Back.WHITE + "  ", end="")
            elif board[row][col] == 2:
                print(Back.RED + "  ", end="")
        print(Style.RESET_ALL)
    print(" ")


def get_move(player):
    while True:
        move = input(f"Jugador {player}, ingresa la posición de tu movimiento (fila,columna): ")
        
        try:
            row, col = move.split(",")
            row, col = int(row), int(col)
            if 0 <= row <= 7 and 0 <= col <= 7:
                if board[row][col] == player:
                    return row, col
                else:
                    print("Esa casilla no tiene una ficha tuya.")
            else:
                print("La posición ingresada está fuera del tablero.")
        except ValueError:
            print("Ingresa una posición válida en el formato fila,columna.")


# Función para mover una ficha
def move_piece(start_row, start_col, end_row, end_col):
    piece = board[start_row][start_col]
    board[start_row][start_col] = 0
    board[end_row][end_col] = piece

# Función para comprobar si un movimiento es válido
def is_valid_move(start_row, start_col, end_row, end_col, player):
    if board[end_row][end_col] != 0:
        return False
    if player == 1 and board[start_row][start_col] != 1:
        return False
    if player == 2 and board[start_row][start_col] != 2:
        return False
    if abs(start_row - end_row) != 1 or abs(start_col - end_col) != 1:
        return False
    return True

# Función para comprobar si un jugador ha ganado
def check_win(player):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == player:
                return False
    return True

# Función para cambiar de jugador
def switch_player(player):
    if player == 1:
        return 2
    else:
        return 1

# Función principal del juego
def play_game():
    player = 1
    while True:
        print_board()
        print(f"Turno del jugador {player}")
        start_row = int(input("Ingrese la fila de la ficha que desea mover: "))
        start_col = int(input("Ingrese la columna de la ficha que desea mover: "))
        end_row = int(input("Ingrese la fila a la que desea mover la ficha: "))
        end_col = int(input("Ingrese la columna a la que desea mover la ficha: "))
        if is_valid_move(start_row, start_col, end_row, end_col, player):
            move_piece(start_row, start_col, end_row, end_col)
            if check_win(player):
                print(f"¡El jugador {player} ha ganado!")
                break
            player = switch_player(player)
        else:
            print("Movimiento inválido, por favor intente de nuevo.")

# Función para preguntar si se quiere volver a jugar
def play_again():
    again = input("¿Desea volver a jugar? (S/N): ")
    if again.lower() == "s":
        play_game()
    else:
        print("¡Gracias por jugar!")

# Iniciamos el juego
play_game()

# Preguntamos si se quiere volver a jugar
play_again()
