from frontend.validators import *


def print_greeting():
    """
    The functions prints greeting to the users at the beginning
    of the game
    """
    print("Welcome to a Tic-Tac-Toe Game!")


def get_player_names() -> tuple:
    """
    The functions receive the names of the players
    """
    is_valid_player_one_name = False
    is_valid_player_two_name = False
    print("Please enter player 1 name: ", end="")
    while not is_valid_player_one_name:
        player_one_name = input()
        is_valid_player_one_name = is_valid_player_name_input(player_one_name)
    print("Please enter player 2 name: ", end="")
    while not is_valid_player_two_name:
        player_two_name = input()
        is_valid_player_two_name = is_valid_player_name_input(player_two_name)
    return player_one_name, player_two_name


def get_player_symbols(player_names: tuple[str]) -> dict:
    ret_dict = {player_names[0]: "X", player_names[1]: "O"}
    return ret_dict


def get_board_size() -> int:
    """
    Get board size from the input including validations
    """
    while True:
        board_size = input(
            "Board sizes options: 3x3, 4x4, ..., 9x9\nPlease enter a single number (#) to represent board size (#x#): ")
        if is_valid_board_size_input(board_size):
            return int(board_size)


def display_turn_prompt(players_names: tuple[str], current_player: int):
    """
    Ask relevant player to insert his move.
    Consider the best way to display the board to the user
    and how the user should indicate where he wants to put X or O
    """
    print(f"{players_names[current_player]}'s turn\nPlease insert your move (Ex: B,3): ")
    return


def get_user_turn(board: list[list[str]], board_size: int) -> tuple:
    """
    Receive user's move including validations.
    Note, you should validate that the input is correct, and
    the cell in the board is available (empty)
    """
    col_index_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9}
    valid_input = False
    while not valid_input:
        move_merged = input()
        valid_input = is_valid_turn_input(move_merged, board, board_size)
    move_c, move_l = move_merged.split(",")
    return col_index_dict[str(move_c).upper()]-1, int(move_l)-1


def print_win_msg(player_name):
    """
    Print a beautiful win message to the winner
    :param player_name:
    :return:
    """
    print(f"{player_name} is the winner!")
    return None


def print_draw_msg():
    """
    Print a beautiful draw message
    :return:
    """
    print("The game is a draw")
    return


def is_still_playing() -> bool:
    valid_choice = False
    print("Would you like to play again? (Y/N): ", end="")
    while not valid_choice:
        choice = input()
        valid_choice = is_valid_is_still_playing_choice_input(choice)
    if choice.upper() == "Y":
        return True
    else:
        return False
