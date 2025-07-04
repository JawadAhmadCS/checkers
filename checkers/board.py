import pygame
from .constants import BOARD_IMG, MOVE_MARKER, BLACK, WHITE, ROWS, COLS, SQUARE_SIZE
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.red_left = self.white_left = 12  # Number of pieces left
        self.red_kings = self.white_kings = 0  # Number of kings
        self.create_board()
    
    def draw_squares(self, win):
        """Draw the checkerboard using an image"""
        win.blit(BOARD_IMG, (0, 0))

    def evaluate(self):
        """Evaluate the board position for AI"""
        return self.white_left - self.red_left + (self.white_kings * 0.5 - self.red_kings * 0.5)

    def get_all_pieces(self, color):
        """Get all pieces of a specific color"""
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    def move(self, piece, row, col):
        """Move a piece to a new position"""
        # Swap positions in the board array
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        # Check if piece should be kinged
        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.red_kings += 1

    def get_piece(self, row, col):
        """Get piece at specific row and column"""
        return self.board[row][col]

    def create_board(self):
        """Initialize the board with pieces in starting positions"""
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):  # Only place pieces on dark squares
                    if row < 3:  # White pieces at top
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:  # Black pieces at bottom
                        self.board[row].append(Piece(row, col, BLACK))
                    else:  # Middle empty rows
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
        
    def draw(self, win):
        """Draw the board and all pieces"""
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def remove(self, pieces):
        """Remove captured pieces from the board"""
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == BLACK:
                    self.red_left -= 1
                else:
                    self.white_left -= 1
    
    def winner(self):
        """Check if there's a winner"""
        if self.red_left <= 0:
            return WHITE
        elif self.white_left <= 0:
            return BLACK
        return None
    
    def get_valid_moves(self, piece):
        """Get all valid moves for a piece"""
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == BLACK or piece.king:
            moves.update(self._traverse_left(row - 1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row-3, -1), -1, piece.color, right))

        if piece.color == WHITE or piece.king:
            moves.update(self._traverse_left(row + 1, min(row+3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, min(row+3, ROWS), 1, piece.color, right))
    
        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        """Helper method to check moves to the left"""
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, left-1, skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, left+1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1
        
        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        """Helper method to check moves to the right"""
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break
            
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, right-1, skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, right+1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1
        
        return moves