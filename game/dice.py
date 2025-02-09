import pygame
import random
from game.constants import *

class Dice:
    def __init__(self):
        self.value = 1
        self.rolling = False
        self.roll_time = 0
        self.roll_duration = 1000  # 1 second
        self.size = 60
        self.position = (SCREEN_WIDTH - 100, SCREEN_HEIGHT // 2)
        
    def roll(self):
        if not self.rolling:
            self.rolling = True
            self.roll_time = pygame.time.get_ticks()
            self.value = random.randint(1, 6)
            
    def update(self):
        if self.rolling:
            current_time = pygame.time.get_ticks()
            if current_time - self.roll_time >= self.roll_duration:
                self.rolling = False
                
    def draw(self, screen):
        # Draw dice background
        pygame.draw.rect(screen, WHITE, 
                        (self.position[0], self.position[1], 
                         self.size, self.size))
        pygame.draw.rect(screen, BLACK, 
                        (self.position[0], self.position[1], 
                         self.size, self.size), 2)
        
        # Draw dots based on dice value
        if self.rolling:
            value = random.randint(1, 6)
        else:
            value = self.value
            
        dot_radius = 5
        positions = self._get_dot_positions(value)
        
        for pos in positions:
            x = self.position[0] + pos[0] * (self.size // 4)
            y = self.position[1] + pos[1] * (self.size // 4)
            pygame.draw.circle(screen, BLACK, (x, y), dot_radius)
            
    def _get_dot_positions(self, value):
        if value == 1:
            return [(2, 2)]
        elif value == 2:
            return [(1, 1), (3, 3)]
        elif value == 3:
            return [(1, 1), (2, 2), (3, 3)]
        elif value == 4:
            return [(1, 1), (1, 3), (3, 1), (3, 3)]
        elif value == 5:
            return [(1, 1), (1, 3), (2, 2), (3, 1), (3, 3)]
        else:  # value == 6
            return [(1, 1), (1, 2), (1, 3), (3, 1), (3, 2), (3, 3)]
