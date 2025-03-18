import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, drawable, updateable)
    asteroid_field = AsteroidField()

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updateable.update(dt)

        for obj in asteroids:
            if obj.collisions(player) == True:
                sys.exit("Game over!")
            for bullet in shots:
                if obj.collisions(bullet) == True:
                    obj.split()
                    bullet.kill()

        screen.fill("#000000")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # framerate
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()