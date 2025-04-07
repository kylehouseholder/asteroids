import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, position):
        super().__init__(position.x, position.y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt