import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            splitAngle = random.uniform(18.0, 45.0)
            vecL = self.velocity.rotate(-splitAngle)
            vecR = self.velocity.rotate(splitAngle)
            spawnRadius = self.radius - ASTEROID_MIN_RADIUS

            asteroidL = Asteroid(self.position.x, self.position.y, spawnRadius)
            asteroidL.velocity = random.uniform(1.2, 2.1) * vecL
            asteroidR = Asteroid(self.position.x, self.position.y, spawnRadius)
            asteroidR.velocity = random.uniform(1.2, 2.1) * vecR
            self.kill()
