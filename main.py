import pygame
from constants import *
from shot import Shot
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

# comment block for testing purposes
def main():
    pygame.init()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    update_G = pygame.sprite.Group()
    draw_G = pygame.sprite.Group()
    asteroid_G = pygame.sprite.Group()
    shots_G = pygame.sprite.Group()

    Player.containers = (update_G, draw_G)
    Asteroid.containers = (asteroid_G, update_G, draw_G)
    AsteroidField.containers = (update_G)
    Shot.containers = (shots_G, update_G, draw_G)

    ship = Player(x, y)
    field = AsteroidField()

    while True:
        screen.fill(BLACK)
        dt = clock.tick()/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        update_G.update(dt)

        for asteroid in asteroid_G:
            if ship.hasCollision(asteroid):
                print("Game over!")
                raise SystemExit
            for shot in shots_G:
                if asteroid.hasCollision(shot):
                    shot.kill()
                    asteroid.split()        

        for entity in draw_G:
            entity.draw(screen)
            
        pygame.display.flip()
if __name__ == "__main__":
    main()