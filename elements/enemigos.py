# Módulo para los enemigos del juego

#Posicion tamaño y tipos de ataque cuano daño hace, vida

import pygame
import random
from pygame.locals import (RLEACCEL)
from abc import ABC, abstractmethod

BUGpng = pygame.image.load('assets/bug.png')
BUGpng_scaled = pygame.transform.scale(BUGpng, (64, 64))

class Boss():
    pass

class Enemy(ABC):

    def __init__(self, hp: int, ap: int, speed: float):
        self.speed  = speed
        self.hp     = hp #health points
        self.ap     = ap #attack points

    @abstractmethod
    def attack(self, other):
        pass

    @abstractmethod
    def lose_health(self, health: int):
        pass

    @abstractmethod
    def move(self):
        pass
    
    @abstractmethod
    def update(self):
        pass