from checkmate import checkmate 
from checkmate import is_within_board
from checkmate import find_king_position

def find_legal_moves(board):

    board_matrix = [list(row) for row in board.splitlines()]
    king_row, king_col = find_king_position(board_matrix)
    king_dir = [(-1,0), (1,0), (0,1), (0,-1), (-1,-1), (-1,1), (1,1), (1,-1)]
    aval_legal_moves = 0
    print("ALL MOVES SIMULATED!")
    for row, col in king_dir:
        board_matrix = [list(row) for row in board.splitlines()]
        newking_row, newking_col = king_row+row, king_col+col
        if not is_within_board(newking_row, newking_col, len(board_matrix)):
            continue
        board_matrix[king_row][king_col] = "."

        board_matrix[newking_row][newking_col] = "K"
        
        new_board = construct_board(board_matrix)
        print("\n" + new_board)
        if not checkmate(new_board):
            aval_legal_moves += 1
    print("\nYou have", aval_legal_moves, "available legal move." if aval_legal_moves == 1 else "available legal moves.")

def construct_board(board_matrix):
    return '\n'.join("".join(row) for row in board_matrix)


