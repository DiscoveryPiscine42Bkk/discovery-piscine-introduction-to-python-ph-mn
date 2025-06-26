def checkmate(board):
    if not is_board_valid(board):
        print("Error")
        exit()
    board_matrix = [list(row) for row in board.splitlines()]
    board_size = len(board_matrix)
    king_row, king_col = find_king_position(board_matrix)

    
    def is_within_board(row, col):
        return 0 <= row < board_size and 0<= col < board_size
    
    straight_dir = [(-1,0), (1,0), (0,1), (0,-1)]
    diagonal_dir = [(-1,-1), (-1,1), (1,1), (1,-1)]
    pawn_dir = [(1,-1), (1,1)]

    for row_dir, col_dir in straight_dir:
        row, col = king_row + row_dir, king_col + col_dir
        while is_within_board(row, col):
            piece = board_matrix[row][col]
            if piece in ['R', 'Q']:
                print("Success!")
                return True
            elif piece in ['B','P']:
                break
            row += row_dir
            col += col_dir

    for row_dir, col_dir in diagonal_dir:
        row, col = king_row + row_dir, king_col + col_dir
        while is_within_board(row, col):
            piece = board_matrix[row][col]
            if piece in ['B', 'Q']:
                print("Success!")
                return True
            elif piece in ['R','P']:
                break
            row += row_dir
            col += col_dir

    for row_dir, col_dir in pawn_dir:
        row, col = king_row + row_dir, king_col + col_dir
        
        if is_within_board(row, col) and board_matrix[row][col] == 'P':
            print("Success!")
            return True

    print("Fail")
    return False
                
            

    














def find_king_position(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col].upper() == 'K':
                return (row,col)
    return None

def is_board_valid(board):
    try:
        if len(board) == 0:
            return False
        board_matrix = [list(row) for row in board.splitlines()]
        if not all(len(row) == len(board_matrix) for row in board_matrix):
            return False
        if "K" not in board.upper() or board.upper().count("K") > 1:
            return False
        if not any(piece in board for piece in ["Q", "R", "B", "P"]):
            return False
    except:
        return False


    return True