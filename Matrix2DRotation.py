import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulação de Rotação no Eixo Z (2D)")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Pontos iniciais (cubo em 2D)
points = [[-150, -150], [150, -150], [150, 150], [-150, 150]]

'''
Rotação em torno do eixo Z:
    x' = x * cos(θz) - y * sin(θz)
    y' = x * sin(θz) + y * cos(θz)

Onde θ é o ângulo de rotação respectivo ao eixo
z' são as coordenadas após a rotação	
'''
def rotate(points: list, angle_z: float ) -> list:
    """Função para aplicar rotação 2D
    
    Args:
        points (list): Lista de pontos a serem rotacionados
        angle_z (float): Ângulo de rotação no eixo Z

    Returns:
        list: Lista de pontos após a rotação
    """
    rotated = []
    for x, y in points:
        x, y = x * math.cos(angle_z) - y * math.sin(angle_z), x * math.sin(angle_z) + y * math.cos(angle_z)
        rotated.append([x, y])
    return rotated


# Centro do cubo
center = (WIDTH // 2, HEIGHT // 2)

# Ângulo de rotação
angle_z = 0

# Loop principal
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Method 1: Rotate using keys
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_a]:
    #     angle_z -= 0.01
    # if keys[pygame.K_d]:
    #     angle_z += 0.01

    # Method 2: Rotate automatically
    angle_z += 0.01

    # Rotacionar os pontos
    rotated_points = rotate(points, angle_z)

    # Desenhar
    screen.fill(WHITE)
    pygame.draw.polygon(
        screen,
        RED,
        [(x + center[0], y + center[1]) for x, y in rotated_points],
        5
    )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
