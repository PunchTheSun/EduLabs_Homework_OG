def initialize_board(board_size: int) -> list[list[str]]:
    """
    Initialize the game board according to the board size
    received from the user
    """
    board = []
    columns = []
    for row in range(board_size):
        for col in range(board_size):
            columns.append(" ")
        board.append(columns)
        columns = []
    return board


def update_board_with_turn(board: list[list[str]], move: tuple, char: str) -> list[list[str]]:
    """
    Update game board with new user turn
    """
    board[move[1]][move[0]] = char.upper()
    return board


def no_moves_left(board) -> bool:
    """
    Check whether the game is finished (no more moves left - the board is full)
    """
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == " ":
                return False
    return True


def get_winner(board) -> str | None:
    """
    Check whether there is a winner.
    The function returns the winning char if exists, otherwise None.
    This function should use the following functions to detect
    whether there is a winner:
    row_wins()
    column_wins()
    diagonal_wins()
    """
    row_winner = get_row_winner(board)
    col_winner = get_column_winner(board)
    diag_winner = get_diagonal_winner(board)
    if row_winner is not None:
        return row_winner
    elif col_winner is not None:
        return col_winner
    elif diag_winner is not None:
        return diag_winner
    return None


def get_row_winner(board: list[list[str]]) -> str | None:
    """
    Check whether there is a winner in a row
    """
    for line in range(len(board)):
        line_counter_x = 0
        line_counter_o = 0
        for col in range(len(board[line])):
            if board[line][col].upper() == "X":
                line_counter_x += 1
            elif board[line][col].upper() == "O":
                line_counter_o += 1
        if line_counter_x == len(board[0]):
            return "X"
        elif line_counter_o == len(board[0]):
            return "O"
    return None


def get_column_winner(board: list[list[str]]) -> str | None:
    """
    Check whether there is a winner in a column
    """
    for col in range(len(board)):
        col_counter_x = 0
        col_counter_o = 0
        for line in range(len(board[col])):
            if board[line][col].upper() == "X":
                col_counter_x += 1
            elif board[line][col].upper() == "O":
                col_counter_o += 1
        if col_counter_x == len(board[0]):
            return "X"
        elif col_counter_o == len(board[0]):
            return "O"
    return None


def get_diagonal_winner(board: list[list[str]]) -> str | None:
    """
    Check whether there is a winner in one of the diagonals
    :return:
    """
    diag_counter_x = 0
    diag_counter_o = 0
    line = 0
    col = 0
    while line < len(board) and col < len(board):
        if board[line][col].upper() == "X":
            diag_counter_x += 1
        elif board[line][col].upper() == "O":
            diag_counter_o += 1
        line += 1
        col += 1
    if diag_counter_x == len(board[0]):
        return "X"
    elif diag_counter_o == len(board[0]):
        return "O"

    line -= 1
    col = 0
    diag_counter_x = 0
    diag_counter_o = 0
    while line >= 0 and col < len(board):
        if board[line][col].upper() == "X":
            diag_counter_x += 1
        elif board[line][col].upper() == "O":
            diag_counter_o += 1
        line -= 1
        col += 1
    if diag_counter_x == len(board[0]):
        return "X"
    elif diag_counter_o == len(board[0]):
        return "O"
    return None


# bonus
def game_stuck():
    """
    Bonus: check whether the game is stuck (it is useless to
    continue a game if no one can win - the board is not full,
    but every row, column, and diagonal is filled both with X and O)
    """
    pass
