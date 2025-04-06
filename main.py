import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    black = (0, 0, 0)
    white = (255, 255, 255)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    dt = 0
    
    update_G = pygame.sprite.Group()
    draw_G = pygame.sprite.Group()              
    Player.containers = (update_G, draw_G)
    ship = Player(x, y)  

    while True:
        screen.fill(black)
        dt = clock.tick()/1000
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                return

        update_G.update(dt)
        
        for entity in draw_G:
            entity.draw(screen)
            
        pygame.display.flip()
if __name__ == "__main__":
    main()