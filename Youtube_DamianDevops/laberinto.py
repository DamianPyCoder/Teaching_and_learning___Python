import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 40  # Tamaño de cada celda del laberinto
PLAYER_SPEED = 1  # Velocidad del jugador (celdas por iteración)

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Definir el laberinto
maze = [
    "XXXXXXXXXXXXXXXXXXXX",
    "X       X    X    X X",
    "X XXXXX X XX X XX X X",
    "X    X  X X  X X    X",
    "XXX X XX  XX  X XXX X",
    "X X X X X    X X X X",
    "X X XXX XXXX X X X X",
    "X X   X       X X X X",
    "X X X X XXXXX X X X X",
    "X     X        X X  X",
    "XXX XXXXXXX XXXXXX X",
    "X                X X",
    "X XXXXXXXXXXXX X X X",
    "X                X X",
    "XXXXXXXXXXXXXX XXX X",
    "X  X          X   X ",
    "X  X XXXXXXXX XXX X",
    "X     X         X X",
    "XXXXX XXXXXXXXX X X",
    "X       X        SX",
    "XXXXXXXXXXXXXXXXXX",
]

# Función para dibujar el laberinto
def draw_maze(screen):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == "X":
                pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif cell == "S":
                pygame.draw.rect(screen, RED, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Función principal del juego
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Laberinto")

    clock = pygame.time.Clock()

    player_x = player_y = 2  # Posición inicial del jugador

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if maze[player_y - PLAYER_SPEED][player_x] != "X":
                player_y -= PLAYER_SPEED
        elif keys[pygame.K_DOWN]:
            if maze[player_y + PLAYER_SPEED][player_x] != "X":
                player_y += PLAYER_SPEED
        elif keys[pygame.K_LEFT]:
            if maze[player_y][player_x - PLAYER_SPEED] != "X":
                player_x -= PLAYER_SPEED
        elif keys[pygame.K_RIGHT]:
            if maze[player_y][player_x + PLAYER_SPEED] != "X":
                player_x += PLAYER_SPEED

        screen.fill(WHITE)
        draw_maze(screen)
        pygame.draw.circle(screen, RED, (player_x * CELL_SIZE + CELL_SIZE // 2, player_y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2)
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
