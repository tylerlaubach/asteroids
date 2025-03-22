import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    containers = None

    def __init__(self, x, y, radius, velocity=None):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            # Small asteroids just disappear
            return
        else:
            # Bigger asteroids respawn
            random_angle = random.uniform(20, 50)
            vector1, vector2 = self.velocity.rotate(random_angle), self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = vector1 * 1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = vector2 * 1.2