from .constants import WHITE, BLACK, WHITE_PIECE, BLACK_PIECE, WHITE_KING, BLACK_KING, SQUARE_SIZE

class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True
    
    def draw(self, win):
        if self.color == WHITE:
            if self.king:
                win.blit(WHITE_KING, (self.x - WHITE_KING.get_width()//2, self.y - WHITE_KING.get_height()//2))
            else:
                win.blit(WHITE_PIECE, (self.x - WHITE_PIECE.get_width()//2, self.y - WHITE_PIECE.get_height()//2))
        else:
            if self.king:
                win.blit(BLACK_KING, (self.x - BLACK_KING.get_width()//2, self.y - BLACK_KING.get_height()//2))
            else:
                win.blit(BLACK_PIECE, (self.x - BLACK_PIECE.get_width()//2, self.y - BLACK_PIECE.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()