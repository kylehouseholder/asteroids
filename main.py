import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    black = (0, 0, 0)
    white = (255, 255, 255)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(black)

        player.update(dt)
        player.draw(screen)
        
        dt = clock.tick()/1000
        pygame.display.flip()
    
if __name__ == "__main__":
    main()