import pygame
from game.constants import *

class Token:
    def __init__(self, color, position, home_position):
        self.color = color
        self.position = position
        self.home_position = home_position
        self.is_active = False
        self.path_position = -1

    def draw(self, screen, board_offset):
        x = board_offset[0] + self.position[0] * CELL_SIZE + CELL_SIZE // 2
        y = board_offset[1] + self.position[1] * CELL_SIZE + CELL_SIZE // 2

        # Draw token circle
        pygame.draw.circle(screen, self.color, (x, y), TOKEN_RADIUS)
        pygame.draw.circle(screen, BLACK, (x, y), TOKEN_RADIUS, 2)

        # Draw inner circle for detail
        pygame.draw.circle(screen, WHITE, (x, y), TOKEN_RADIUS // 2)

    def move(self, steps):
        if not self.is_active and steps == 6:
            self.activate()
            return True

        if self.is_active:
            new_position = self.path_position + steps
            # Get the correct path based on token's color
            color_name = self._get_color_name()
            current_path = PLAYER_PATHS[color_name]

            if new_position < len(current_path):
                self.path_position = new_position
                self.position = current_path[new_position]
                return True
        return False

    def activate(self):
        if not self.is_active:
            self.is_active = True
            self.path_position = 0
            color_name = self._get_color_name()
            self.position = PLAYER_PATHS[color_name][0]

    def reset(self):
        self.is_active = False
        self.path_position = -1
        self.position = self.home_position

    def _get_color_name(self):
        # Convert RGB color tuple to color name
        for name, color in [('red', RED), ('blue', BLUE), ('green', GREEN), ('yellow', YELLOW)]:
            if self.color == color:
                return name
        return 'red'  # fallback to red if color not found