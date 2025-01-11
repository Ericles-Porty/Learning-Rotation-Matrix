import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulação de Rotação nos Eixos X, Y e Z (3D)")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Pontos iniciais (cubo em 3D)
points = [
    [-50, -50, -50], [50, -50, -50], [50, 50, -50], [-50, 50, -50],  # Frente
    [-50, -50, 50], [50, -50, 50], [50, 50, 50], [-50, 50, 50]       # Trás
]

# Arestas que conectam os pontos, os valores são os índices dos pontos
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # Frente
    (4, 5), (5, 6), (6, 7), (7, 4),  # Trás
    (0, 4), (1, 5), (2, 6), (3, 7)   # Conexões entre frente e trás
]


'''
Função para aplicar rotação
Rotação em torno do eixo X:
    y' = y * cos(θx) - z * sin(θx)
    z' = y * sin(θx) + z * cos(θx)

Rotação em torno do eixo Y:
    x' = x * cos(θy) + z * sin(θy)
    z' = -x * sin(θy) + z * cos(θy)

Rotação em torno do eixo Z:
    x' = x * cos(θz) - y * sin(θz)
    y' = x * sin(θz) + y * cos(θz)

Onde θ é o ângulo de rotação respectivo ao eixo
x', y', z' são as coordenadas após a rotação	
'''


def rotate(points, angle_x, angle_y, angle_z):
    rotated = []
    for x, y, z in points:
        # Rotação no eixo X
        y, z = y * math.cos(angle_x) - z * math.sin(angle_x), y * math.sin(angle_x) + z * math.cos(angle_x)

        # Rotação no eixo Y
        x, z = x * math.cos(angle_y) + z * math.sin(angle_y), - x * math.sin(angle_y) + z * math.cos(angle_y)

        # Rotação no eixo Z
        x, y = x * math.cos(angle_z) - y * math.sin(angle_z), x * math.sin(angle_z) + y * math.cos(angle_z)

        rotated.append([x, y, z])
    return rotated


'''
Projeção 3D para 2D
Formula para projeção: 
    x' = (x / z)*d, 
    y' = (y / z)*d

Onde d é a distância do plano de projeção, imaginando como a distância de uma câmera ao plano
'''


def project(points):
    d = 500  # Distância do plano de projeção
    projected = []
    for x, y, z in points:
        z += 200  # Deslocar para frente para evitar z negativo
        x, y = (x/z)*d, (y/z) * d
        projected.append([x, y])
    return projected


# Centro do cubo
center = (WIDTH // 2, HEIGHT // 2)

# Ângulos de rotação
angle_x = 0
angle_y = 0
angle_z = 0

# Loop principal
running = True
clock = pygame.time.Clock()
color_counter = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_w]:
    #     angle_x -= 0.01
    # if keys[pygame.K_s]:
    #     angle_x += 0.01
    # if keys[pygame.K_a]:
    #     angle_y += 0.01
    # if keys[pygame.K_d]:
    #     angle_y -= 0.01
    # if keys[pygame.K_q]:
    #     angle_z -= 0.01
    # if keys[pygame.K_e]:
    #     angle_z += 0.01

    # Atualizar ângulos em cada iteração
    angle_x += 0.01
    angle_y += 0.02
    angle_z += 0.01

    # Rotacionar os pontos
    rotated_points = rotate(points, angle_x, angle_y, angle_z)
    projected_points = project(rotated_points)

    # Desenhar
    screen.fill(WHITE)
    for edge in edges:
        x1, y1 = projected_points[edge[0]]
        x2, y2 = projected_points[edge[1]]
        pygame.draw.line(
            screen,
            RED,
            (x1 + center[0], y1 + center[1]),
            (x2 + center[0], y2 + center[1]),
            2
        )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
