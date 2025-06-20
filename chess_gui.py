import pygame
import chess
import sys

# Initialize pygame and chess
pygame.init()
board = chess.Board()

# GUI settings
WIDTH, HEIGHT = 640, 640
SQUARE_SIZE = WIDTH // 8
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Chess Game")

# Colors
LIGHT = (240, 217, 181)
DARK = (181, 136, 99)
HIGHLIGHT = (66, 135, 245)

# Fonts
font = pygame.font.SysFont("Arial", 44)

# Unicode characters for pieces
UNICODE_PIECES = {
    'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚', 'p': '♟',
    'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔', 'P': '♙'
}

# Selected square and move log
selected_square = None
move_log = []

def draw_board():
    for rank in range(8):
        for file in range(8):
            square_color = LIGHT if (rank + file) % 2 == 0 else DARK
            pygame.draw.rect(screen, square_color, pygame.Rect(file * SQUARE_SIZE, rank * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces():
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            file = chess.square_file(square)
            rank = 7 - chess.square_rank(square)
            symbol = UNICODE_PIECES[piece.symbol()]
            piece_text = font.render(symbol, True, (0, 0, 0))
            screen.blit(piece_text, (file * SQUARE_SIZE + 20, rank * SQUARE_SIZE + 10))

def highlight_square(square):
    if square is None:
        return
    file = chess.square_file(square)
    rank = 7 - chess.square_rank(square)
    pygame.draw.rect(screen, HIGHLIGHT, pygame.Rect(file * SQUARE_SIZE, rank * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 4)

def get_square_from_mouse(pos):
    x, y = pos
    file = x // SQUARE_SIZE
    rank = 7 - (y // SQUARE_SIZE)
    return chess.square(file, rank)

def main():
    global selected_square
    clock = pygame.time.Clock()
    running = True

    while running:
        draw_board()
        highlight_square(selected_square)
        draw_pieces()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                square = get_square_from_mouse(pygame.mouse.get_pos())

                if selected_square is None:
                    # Select a piece
                    if board.piece_at(square) and board.piece_at(square).color == board.turn:
                        selected_square = square
                else:
                    move = chess.Move(selected_square, square)
                    if move in board.legal_moves:
                        board.push(move)
                        move_log.append(move)
                    selected_square = None

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u and move_log:
                    board.pop()
                    move_log.pop()
                    selected_square = None

        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
