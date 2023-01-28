from backend.board import *

def test_initialize_board():
    board = initialize_board(5)
    expected_board = [[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "]]

    assert board == expected_board, \
    f"Incorrect Board size recieved\nExpected size:{5}x{5}\nRecieved:{len(board)}x{len(board[0])}"

