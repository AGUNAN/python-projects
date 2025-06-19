# chess_game.py

# Simple terminal chess
# No check/checkmate logic yet

class Piece:
    def __init__(self, name, color):
        self.name = name  # 'P', 'R', 'N', etc.
        self.color = color  # 'w' or 'b'

    def __str__(self):
        return f'{self.color}{self.name}'

def create_board():
    board = [[None] * 8 for _ in range(8)]

    # Place pawns
    for i in range(8):
        board[1][i] = Piece('P', 'b')
        board[6][i] = Piece('P', 'w')

    # Place major pieces
    layout = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
    for i, piece in enumerate(layout):
        board[0][i] = Piece(piece, 'b')
        board[7][i] = Piece(piece, 'w')

    return board

def print_board(board):
    print("\n    a  b  c  d  e  f  g  h")
    print("   ------------------------")
    for i in range(8):
        row = f"{8-i} |"
        for j in range(8):
            piece = board[i][j]
            row += f" {str(piece) if piece else '..'}"
        print(row + f" | {8-i}")
    print("   ------------------------")
    print("    a  b  c  d  e  f  g  h\n")

def parse_position(pos):
    col = ord(pos[0]) - ord('a')
    row = 8 - int(pos[1])
    return row, col

def is_valid_move(board, start, end, turn):
    piece = board[start[0]][start[1]]
    target = board[end[0]][end[1]]

    if not piece or piece.color != turn:
        return False

    if target and target.color == turn:
        return False

    # Simplified movement for demo
    if piece.name == 'P':
        direction = -1 if turn == 'w' else 1
        if start[1] == end[1]:
            if end[0] - start[0] == direction and not target:
                return True
        if abs(start[1] - end[1]) == 1 and end[0] - start[0] == direction and target:
            return True
    else:
        return True  # Allow any move for non-pawn pieces (you can improve this)

    return False

def move_piece(board, start, end):
    board[end[0]][end[1]] = board[start[0]][start[1]]
    board[start[0]][start[1]] = None

def main():
    board = create_board()
    turn = 'w'

    while True:
        print_board(board)
        print(f"{'White' if turn == 'w' else 'Black'}'s move:")
        move = input("Enter move (e.g. e2 e4 or 'exit'): ").strip()
        if move.lower() == 'exit':
            break

        try:
            src, dst = move.split()
            start = parse_position(src)
            end = parse_position(dst)

            if is_valid_move(board, start, end, turn):
                move_piece(board, start, end)
                turn = 'b' if turn == 'w' else 'w'
            else:
                print("❌ Invalid move. Try again.")
        except Exception as e:
            print("⚠️ Error:", e)
            print("Please enter a valid move like 'e2 e4'.")

if __name__ == '__main__':
    main()
