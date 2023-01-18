from board import *
from frontend.menu_utils import *
from frontend.board_print_utils import *

import random

print_greeting()
player_names = get_player_names()
player_symbols = get_player_symbols(player_names)
still_playing = True


while still_playing:
    board_size = get_board_size()
    board = initialize_board(board_size)
    current_player_number = random.randint(0, 1)
    current_player = player_names[current_player_number]
    winner = None
    draw = False

    while winner is None and not draw:
        display_current_board(board, board_size)
        display_turn_prompt(player_names, current_player_number)
        move = get_user_turn(board, board_size)
        board = update_board_with_turn(board, move, player_symbols[current_player])
        winner = get_winner(board)
        draw = no_moves_left(board)
        if current_player_number == 1:
            current_player_number = 0
        else:
            current_player_number = 1
        current_player = player_names[current_player_number]
    display_current_board(board, board_size)
    if draw:
        print_draw_msg()
    elif winner is not None:
        for player in player_names:
            if player_symbols[player] == winner.upper():
                print_win_msg(player)

    still_playing = is_still_playing()
