import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    Shot.containers = (shots, updatable, drawable)

    while True:
        # Enable the ability to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Create background
        screen.fill("black")

        # Update objects
        updatable.update(dt)

        # Check for collisions
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                sys.exit()

        # Draw objects
        for item in drawable:
            item.draw(screen)

        # Update screen
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()