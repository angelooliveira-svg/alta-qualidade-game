import pygame
from src.ship import Ship
from tests.doubles import StubSettings


def test_ship_move_com_stub_settings():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))

    ship = Ship(screen, StubSettings())

    x_inicial = ship.x

    ship.moving_right = True
    ship.update()

    assert ship.x == x_inicial + 5


def test_ship_blitme_com_mock_screen(mocker):
    mock_screen = mocker.Mock() # Criar mock da tela
    mock_screen.get_rect.return_value = pygame.Rect(0, 0, 800, 600) # Definir comportamento do mock

    ship = Ship(mock_screen, StubSettings()) # Injetar mock na nave
    ship.blitme() # Executar método

    mock_screen.blit.assert_called_once_with(ship.image, ship.rect) # verifica se a nave foi desenhada uma única vez na tela
