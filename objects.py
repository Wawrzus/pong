import pygame
from random import choice
from dataclasses import dataclass

@dataclass
class Padle:
    position: list[int, int, int, int]
    color: tuple[int, int, int]
    points: int
    velocity_y: float

    def draw(self, screen):
        pygame.draw.rect(surface=screen, color=self.color, rect=self.position)

    def move_up(self):
        if self.position[1] >= 0:
            self.position[1] -= self.velocity_y

    def move_down(self):
        if self.position[1] <= 570:
            self.position[1] += self.velocity_y

    def add_point(self):
        self.points += 1


@dataclass
class Ball:
    position: list[int, int]
    radius: float
    color: tuple[int, int, int]
    velocity_x: float
    velocity_y: float

    def draw(self, screen):
        pygame.draw.circle(screen, color=self.color, center=self.position, radius=self.radius)

    def move(self):
        self.position[0] += self.velocity_x
        self.position[1] += self.velocity_y

    def reset(self, screen_width, screen_height):
        self.position[0] = screen_width // 2
        self.position[1] = screen_height // 2
        self.velocity_x = 4 * choice([-1, 1])

    def bounce_vertical(self):
        self.velocity_y *= -1