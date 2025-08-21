if __name__ == "__main__": # Solo para que no ejecutes este archivo
    import sys
    print(
        "\033[38;2;255;0;0mESTE MODULO NO DEBE EJECUTARSE. EJECUTAR main.py\033[0m\n"
        * 3
    )
    sys.exit()

import pygame


class Projectile(pygame.sprite.Sprite):
    
    def __init__(self, pos, direction, SCREEN_WIDTH, SCREEN_HEIGHT): 
        super(Projectile, self).__init__()
        
        # POR HACER (2.0): Aspecto y parámetros iniciales de la bala
        pass
    
        # POR HACER (2.1): Parámetros iniciales de la bala
        pass
    
        

    def update(self): 
        
        # POR HACER (2.2): Mover la bala y eliminarla si se sale de la pantalla
        pass
