from game.token import Token
from game.constants import *

class Player:
    def __init__(self, color):
        self.color = color
        self.tokens = []
        self.initialize_tokens()
        
    def initialize_tokens(self):
        start_pos = START_POSITIONS[self.color]
        for pos in start_pos:
            self.tokens.append(Token(self.get_color_tuple(), pos, pos))
            
    def get_color_tuple(self):
        if self.color == 'red':
            return RED
        elif self.color == 'blue':
            return BLUE
        elif self.color == 'green':
            return GREEN
        else:
            return YELLOW
            
    def draw_tokens(self, screen, board_offset):
        for token in self.tokens:
            token.draw(screen, board_offset)
            
    def has_won(self):
        return all(token.path_position >= len(RED_PATH) - 1 for token in self.tokens)
    
    def get_valid_moves(self, dice_value):
        valid_moves = []
        for i, token in enumerate(self.tokens):
            if token.is_active:
                if token.path_position + dice_value < len(RED_PATH):
                    valid_moves.append(i)
            elif dice_value == 6:
                valid_moves.append(i)
        return valid_moves
