import pygame
from game.constants import *

class Board:
    def __init__(self):
        self.size = BOARD_SIZE
        self.cell_size = CELL_SIZE
        self.offset = ((SCREEN_WIDTH - self.size) // 2, 
                      (SCREEN_HEIGHT - self.size) // 2)
        
    def draw(self, screen):
        # Draw main board background
        pygame.draw.rect(screen, BOARD_COLOR,
                        (self.offset[0], self.offset[1], 
                         self.size, self.size))
        
        # Draw colored home areas
        self._draw_home_areas(screen)
        
        # Draw grid lines
        self._draw_grid(screen)
        
        # Draw paths
        self._draw_paths(screen)
        
    def _draw_home_areas(self, screen):
        # Red home (top-left)
        pygame.draw.rect(screen, RED,
                        (self.offset[0], self.offset[1],
                         self.cell_size * 6, self.cell_size * 6))
                        
        # Blue home (top-right)
        pygame.draw.rect(screen, BLUE,
                        (self.offset[0] + self.cell_size * 9, self.offset[1],
                         self.cell_size * 6, self.cell_size * 6))
                         
        # Green home (bottom-left)
        pygame.draw.rect(screen, GREEN,
                        (self.offset[0], self.offset[1] + self.cell_size * 9,
                         self.cell_size * 6, self.cell_size * 6))
                         
        # Yellow home (bottom-right)
        pygame.draw.rect(screen, YELLOW,
                        (self.offset[0] + self.cell_size * 9,
                         self.offset[1] + self.cell_size * 9,
                         self.cell_size * 6, self.cell_size * 6))
                         
    def _draw_grid(self, screen):
        for i in range(16):
            # Vertical lines
            pygame.draw.line(screen, BLACK,
                           (self.offset[0] + i * self.cell_size, self.offset[1]),
                           (self.offset[0] + i * self.cell_size,
                            self.offset[1] + self.size))
            # Horizontal lines
            pygame.draw.line(screen, BLACK,
                           (self.offset[0], self.offset[1] + i * self.cell_size),
                           (self.offset[0] + self.size,
                            self.offset[1] + i * self.cell_size))
                            
    def _draw_paths(self, screen):
        # Draw colored paths to center
        for pos in RED_PATH:
            x = self.offset[0] + pos[0] * self.cell_size
            y = self.offset[1] + pos[1] * self.cell_size
            pygame.draw.rect(screen, ACCENT,
                           (x, y, self.cell_size, self.cell_size), 1)
