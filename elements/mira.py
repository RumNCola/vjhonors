"""
Hola este es modulo Jorge,
este modulo manejara la creacion y movimiento de Jorge
"""

if __name__ == "__main__": # Solo para que no ejecutes este archivo
    import sys
    print(
        "\033[38;2;255;0;0mESTE MODULO NO DEBE EJECUTARSE. EJECUTAR main.py\033[0m\n"
        * 3
    )
    sys.exit()

import pygame
from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT, RLEACCEL)
import math

from elements.projectile import Projectile


crosshair = pygame.image.load('assets/crosshair.png')
crosshair = pygame.transform.scale(crosshair, (40, 40))

class Mira(pygame.sprite.Sprite):
    
    def __init__(self):
        super(Mira, self).__init__()
        self.surf = crosshair
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()
        
    def update(self):
        self.rect = crosshair.get_rect()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.rect.center = (mouse_x, mouse_y)
        # POR HACER (2.3): Actualizar la posición de los proyectiles
    
    