import pygame
from src.ship import Ship
from src.settings import Settings

def test_ship_move_direita():
    # Inicializa o Pygame
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    settings = Settings()

    # Cria uma instância de Ship
    ship = Ship(screen, settings)

    # Define a posição inicial da nave
    x_inicial = ship.x

    # Move a nave para a direita
    ship.moving_right = True
    ship.update()

    assert ship.x > x_inicial 