import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir los colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)

# Definir las dimensiones de la pantalla
ANCHO = 600
ALTO = 600

# Definir la velocidad de movimiento del jugador
VELOCIDAD = 5

# Definir la clase del jugador (Pac-Man)
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(AMARILLO)
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO // 2, ALTO // 2)
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Controlar los límites de la pantalla
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO
        if self.rect.top < 0:
            self.rect.top = 0

# Definir la clase del muro
class Muro(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Inicializar la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pac-Man")

# Crear al jugador (Pac-Man)
jugador = Jugador()

# Crear muros
muros = pygame.sprite.Group()
# Definir la posición de los muros (x, y, width, height)
posiciones_muros = [
    (100, 50, 400, 20),
    (100, 50, 20, 400),
    (100, 430, 400, 20),
    (480, 50, 20, 400)
]
# Crear instancias de muros y añadirlos al grupo de muros
for pos in posiciones_muros:
    muro = Muro(*pos)
    muros.add(muro)

# Crear un grupo para el jugador y añadirlo al grupo de sprites
jugador_grupo = pygame.sprite.Group()
jugador_grupo.add(jugador)

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador.vel_x = -VELOCIDAD
                jugador.vel_y = 0
            elif evento.key == pygame.K_RIGHT:
                jugador.vel_x = VELOCIDAD
                jugador.vel_y = 0
            elif evento.key == pygame.K_UP:
                jugador.vel_x = 0
                jugador.vel_y = -VELOCIDAD
            elif evento.key == pygame.K_DOWN:
                jugador.vel_x = 0
                jugador.vel_y = VELOCIDAD

    # Actualizar la posición del jugador
    jugador_grupo.update()

    # Limpiar la pantalla
    pantalla.fill(NEGRO)

    # Dibujar muros en la pantalla
    muros.draw(pantalla)

    # Dibujar al jugador en la pantalla
    jugador_grupo.draw(pantalla)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad del juego
    pygame.time.Clock().tick(30)
