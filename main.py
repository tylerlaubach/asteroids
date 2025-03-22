import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    font = pygame.font.SysFont('Arial', 20)
    title_font = pygame.font.SysFont('Arial', 36)
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    score = 0

    # Title display
    show_title = True
    title_duration_seconds = 3
    title_start_time = pygame.time.get_ticks()
    title_text = title_font.render("Starting ASTEROIDS!", True, "white")
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

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

        # Check for player colliding with asteroid
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                game_over_font = pygame.font.SysFont('Arial', 80)
                score_font = pygame.font.SysFont('Arial', 36)
                game_over_text = game_over_font.render("GAME OVER", True, "white")
                final_score_text = score_font.render(f"FINAL SCORE: {score}", True, "white")
                game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 30))
                final_score_rect = final_score_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 30))
                screen.fill("black")
                screen.blit(game_over_text, game_over_rect)
                screen.blit(final_score_text, final_score_rect)
                pygame.display.flip()
                pygame.time.wait(5000)
                sys.exit()

        # Check for shot colliding with asteroid
        for asteroid in asteroids:
            for shot in shots:
                if shot.check_collision(asteroid):
                    shot.kill()
                    score += asteroid.get_points()
                    asteroid.split()

        # Draw objects
        for item in drawable:
            item.draw(screen)

        # Update screen
        score_text = font.render(f"SCORE: {score}", True, "white")
        screen.blit(score_text, (20, 20))  # Position in top-left corner

        current_time = pygame.time.get_ticks()
        if show_title and current_time - title_start_time < (title_duration_seconds * 1000):
            screen.blit(title_text, title_rect)
        elif show_title:
            show_title = False

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()