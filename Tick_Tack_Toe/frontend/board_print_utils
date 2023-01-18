def display_current_board(board: list[list[str]], board_size: int):
    """
    Display current game board in a user-friendly way
    """

    char_index_dict = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I'}
    print("   |  ", end="")
    for col_index in range(1, board_size):
        print(f"{char_index_dict[col_index]}  |  ", end="")
    print(f"{char_index_dict[board_size]}  |")
    print("   -"+"-"*6*board_size)
    for line_index in range(1, board_size+1):
        print(f"{line_index}  |  ", end="")
        for board_val in board[line_index-1]:
            print(f"{board_val}  |  ", end="")
        print("\n   -"+"-"*6*board_size)
