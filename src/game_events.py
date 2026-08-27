import sys
import pygame

class GameEventHandler:
    """"Responsável apenas por ler e tratar os eventos no teclado/janela"""
    def __init__(self, ship, bullet_manager) -> None:
        self.ship = ship
        self.bullet_manager = bullet_manager

    def _check_events(self):
        # CORREÇÃO: Captura e percorre a lista de eventos gerados pelo Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._handle_keydown(event)
            # CORREÇÃO: Adicionada a chamada para quando o jogador solta a tecla
            elif event.type == pygame.KEYUP:
                self._handle_keyup(event)

    def _handle_keydown(self, event: pygame.event.Event) -> None:
        """Responde a eventos de pressionamento de teclas."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.bullet_manager._fire_bullet()
        # DICA: É comum usar a tecla 'Q' ou 'Esc' para fechar o jogo rapidamente
        elif event.key == pygame.K_q:
            sys.exit()

    def _handle_keyup(self, event: pygame.event.Event) -> None:
        """Responde a eventos de soltura de teclas."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
