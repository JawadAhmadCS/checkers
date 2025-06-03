import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Load images
BOARD_IMG = pygame.transform.scale(pygame.image.load('assets/board.png'), (WIDTH, HEIGHT))
WHITE_PIECE = pygame.transform.scale(pygame.image.load('assets/white_piece.png'), (SQUARE_SIZE-10, SQUARE_SIZE-10))
WHITE_KING = pygame.transform.scale(pygame.image.load('assets/white_king_piece.png'), (SQUARE_SIZE-10, SQUARE_SIZE-10))
BLACK_PIECE = pygame.transform.scale(pygame.image.load('assets/black_piece.png'), (SQUARE_SIZE-10, SQUARE_SIZE-10))
BLACK_KING = pygame.transform.scale(pygame.image.load('assets/black_king_piece.png'), (SQUARE_SIZE-10, SQUARE_SIZE-10))
MOVE_MARKER = pygame.transform.scale(pygame.image.load('assets/marking.png'), (30, 30))
CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))