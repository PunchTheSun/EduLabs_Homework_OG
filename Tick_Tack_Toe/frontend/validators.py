def is_valid_turn_input(move_merged: str, board: list[list[str]], board_size: int) -> bool:
    """
    Return true if the input is a valid player turn input, false otherwise
    :return:
    """
    col_index_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9}
    if len(move_merged) != 3:
        print(
            "Invalid input, please enter your move in the following format\n#Col,#Line\nFor example: A,5\nPlease try "
            "again: ")
    else:
        if ',' in move_merged:
            move_c, move_l = move_merged.split(",")
            if len(move_c) != 1 and len(move_l) != 1:
                print("Please enter a single digit column number and line number\nFor example: A,5\nPlease try again: ")
            elif str(move_c).upper().isalpha():
                if col_index_dict[str(move_c).upper()] in range(1, board_size + 1):
                    if str(move_l).isnumeric():
                        if int(move_l) in range(1, board_size + 1):
                            if board[int(move_l) - 1][col_index_dict[str(move_c).upper()] - 1] == " ":
                                return True
                            else:
                                print("Board slot isn't empty\nPlease try again: ")
                        else:
                            print(
                                f"Line index needs to be within board range {board_size}x{board_size}\nPlease try again: ")
                    else:
                        print("Line index has to be a number\nPlease try again: ")
                else:
                    print(f"Column index needs to be within board range {board_size}x{board_size}\nPlease try again: ")
            else:
                print("Column index has to be a letter\nPlease try again: ")
        else:
            print("Please separate Column index and Line index by using ','\nFor example: A,5\nPlease try again: ")
    return False


def is_valid_board_size_input(board_size: str) -> bool:
    if board_size.isnumeric():
        if 10 > int(board_size) > 2:
            return True
        else:
            print("Please enter a board size between 3 and 9")
    else:
        print("Invalid input, Please enter a number")
    return False


def is_valid_is_still_playing_choice_input(choice: str) -> bool:
    if choice.upper() == "Y" or choice.upper() == "N":
        return True
    else:
        print("Invalid choice, Please enter 'Y' or 'N': ")
        return False


def is_valid_player_name_input(player_name: str) -> bool:
    if " " in player_name:
        first_name, last_name, *leftover = player_name.split(" ")
        if leftover:
            print(
                "Invalid player name\nName must consist of two words maximum\nName must consist of letters and spaces "
                "only\nFor example: 'Israel Israeli'\nPlease try again: ")
            return False
        if str(first_name).isalpha() and str(last_name).isalpha():
            return True
    elif player_name.isalpha():
        return True
    print("Invalid player name\nName must consist of letters and spaces only\nFor example: 'Israel Israeli'\nPlease "
          "try again: ")
    return False
