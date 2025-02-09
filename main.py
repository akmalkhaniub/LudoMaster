import pygame
import sys
import os
from game.board import Board
from game.player import Player
from game.dice import Dice
from game.constants import *

# Set SDL video driver to software rendering
os.environ['SDL_VIDEODRIVER'] = 'x11'
os.environ['SDL_RENDER_DRIVER'] = 'software'

class LudoGame:
    def __init__(self):
        # Initialize pygame with error handling
        try:
            pygame.init()
            # Use software rendering with multiple fallback options
            display_flags = pygame.SWSURFACE
            self.screen = None

            try:
                self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), display_flags)
            except pygame.error:
                print("Falling back to basic display mode...")
                self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

            pygame.display.set_caption("Ludo Game")
            print("Pygame initialized successfully")
            print(f"Display driver: {pygame.display.get_driver()}")
            print(f"Display size: {self.screen.get_size()}")

            # Force window position (for debugging)
            os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'
        except pygame.error as e:
            print(f"Failed to initialize display: {e}")
            sys.exit(1)

        self.board = Board()
        self.dice = Dice()
        self.players = [Player(color) for color in PLAYERS]
        self.current_player = 0
        self.game_state = "ROLL"  # States: ROLL, SELECT_TOKEN
        self.valid_moves = []
        print("Game components initialized")

    def run(self):
        clock = pygame.time.Clock()
        frame_count = 0
        print("Game loop starting...")

        while True:
            frame_count += 1
            if frame_count % 60 == 0:  # Log every second (assuming 60 FPS)
                print(f"Frame {frame_count}: Game State: {self.game_state}")

            self.handle_events()
            self.update()
            self.draw()
            clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    mouse_pos = pygame.mouse.get_pos()
                    print(f"Mouse click at position: {mouse_pos}")

                    if self.game_state == "ROLL" and not self.dice.rolling:
                        dice_rect = pygame.Rect(self.dice.position[0], self.dice.position[1],
                                                 self.dice.size, self.dice.size)

                        if dice_rect.collidepoint(mouse_pos):
                            print("Dice clicked!")
                            self.dice.roll()
                            self.game_state = "ROLLING"

                    elif self.game_state == "SELECT_TOKEN":
                        self.handle_token_selection(event.pos)

    def update(self):
        self.dice.update()

        if self.game_state == "ROLLING" and not self.dice.rolling:
            print(f"Dice roll complete. Value: {self.dice.value}")
            self.valid_moves = self.players[self.current_player].get_valid_moves(self.dice.value)
            print(f"Valid moves: {self.valid_moves}")
            if self.valid_moves:
                self.game_state = "SELECT_TOKEN"
            else:
                self.next_turn()

    def draw(self):
        try:
            # Clear screen with white background
            self.screen.fill(WHITE)

            # Draw debug info
            print(f"Drawing frame - Screen size: {self.screen.get_size()}")
            print(f"Board offset: {self.board.offset}")

            # Draw board and components
            self.board.draw(self.screen)

            # Draw all players' tokens
            for player in self.players:
                player.draw_tokens(self.screen, self.board.offset)

            # Draw dice
            self.dice.draw(self.screen)

            # Draw turn indicator
            self.draw_turn_indicator()

            pygame.display.flip()
            print("Frame rendered successfully")
        except pygame.error as e:
            print(f"Error during drawing: {e}")
            pygame.quit()
            sys.exit(1)

    def draw_turn_indicator(self):
        current_color = self.players[self.current_player].get_color_tuple()
        pygame.draw.circle(self.screen, current_color,
                             (50, 50), 20)
        pygame.draw.circle(self.screen, BLACK,
                             (50, 50), 20, 2)

    def handle_token_selection(self, mouse_pos):
        current_player = self.players[self.current_player]

        for i, token in enumerate(current_player.tokens):
            if i in self.valid_moves:
                token_x = self.board.offset[0] + token.position[0] * CELL_SIZE + CELL_SIZE // 2
                token_y = self.board.offset[1] + token.position[1] * CELL_SIZE + CELL_SIZE // 2

                # Check if click is within token bounds
                distance = ((mouse_pos[0] - token_x) ** 2 +
                            (mouse_pos[1] - token_y) ** 2) ** 0.5

                if distance <= TOKEN_RADIUS:
                    print(f"Token {i} selected and moved")
                    token.move(self.dice.value)
                    self.next_turn()
                    break

    def next_turn(self):
        if self.dice.value != 6:
            self.current_player = (self.current_player + 1) % len(self.players)
        self.game_state = "ROLL"
        print(f"Next turn: Player {self.players[self.current_player].color}")

    def check_winner(self):
        if self.players[self.current_player].has_won():
            print(f"Player {self.players[self.current_player].color} wins!")
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    game = LudoGame()
    game.run()