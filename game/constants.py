# Colors
RED = (255, 65, 54)      # #FF4136 - Bright red
BLUE = (0, 116, 217)     # #0074D9 - Deep blue
GREEN = (46, 204, 64)    # #2ECC40 - Bright green
YELLOW = (255, 220, 0)   # #FFDC00
BOARD_COLOR = (245, 245, 245)  # #F5F5F5
ACCENT = (127, 219, 255)  # #7FDBFF
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen dimensions
SCREEN_WIDTH = 600  # Reduced from 800
SCREEN_HEIGHT = 600  # Reduced from 800

# Board dimensions
BOARD_SIZE = 500  # Reduced from 600 to fit better in smaller screen
CELL_SIZE = BOARD_SIZE // 15  # 15x15 grid

# Token dimensions
TOKEN_RADIUS = CELL_SIZE // 2 - 5

# Path coordinates for each color
RED_PATH = [(6, 13), (6, 12), (6, 11), (6, 10), (6, 9), (5, 8), (4, 8), (3, 8), (2, 8), (1, 8), (0, 8),
            (0, 7), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 5), (6, 4), (6, 3), (6, 2), (6, 1),
            (6, 0), (7, 0), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (9, 6), (10, 6), (11, 6),
            (12, 6), (13, 6), (14, 6), (14, 7), (14, 8), (13, 8), (12, 8), (11, 8), (10, 8), (9, 8),
            (8, 9), (8, 10), (8, 11), (8, 12), (8, 13), (8, 14), (7, 14), (7, 13), (7, 12), (7, 11),
            (7, 10), (7, 9)]

# Starting positions for each color
START_POSITIONS = {
    'red': [(2, 2), (2, 3), (3, 2), (3, 3)],
    'blue': [(2, 11), (2, 12), (3, 11), (3, 12)],
    'green': [(11, 2), (11, 3), (12, 2), (12, 3)],
    'yellow': [(11, 11), (11, 12), (12, 11), (12, 12)]
}

# Player colors
PLAYERS = ['red', 'blue', 'green', 'yellow']