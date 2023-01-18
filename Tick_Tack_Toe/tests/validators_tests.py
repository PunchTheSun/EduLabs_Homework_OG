from frontend.menu_utils import *


def test_is_valid_board_size_input1():
    board_size = "5"
    result = is_valid_board_size_input(board_size)
    expected = True

    assert result == expected, f"Incorrect board size validation process\nExpected: {expected}\nReceived: {result}"


def test_is_valid_board_size_input2():
    board_size = "2"
    result = is_valid_board_size_input(board_size)
    expected = False

    assert result == expected, f"Incorrect board size validation process\nExpected: {expected}\nReceived: {result}"


def test_is_valid_board_size_input3():
    board_size = "-1"
    result = is_valid_board_size_input(board_size)
    expected = False

    assert result == expected, f"Incorrect board size validation process\nExpected: {expected}\nReceived: {result}"


def test_is_valid_board_size_input4():
    board_size = "words"
    result = is_valid_board_size_input(board_size)
    expected = False

    assert result == expected, f"Incorrect board size validation process\nExpected: {expected}\nReceived: {result}"


def test_is_valid_board_size_input5():
    board_size = "10"
    result = is_valid_board_size_input(board_size)
    expected = False

    assert result == expected, f"Incorrect board size validation process\nExpected: {expected}\nReceived: {result}"


def test_is_valid_player_name_input1():
    player_name = "Georgio"
    result = is_valid_player_name_input(player_name)
    expected = True

    assert result == expected, f"Incorrect player name validation process\nExpected: {expected}\nReceived: {result}"


def test_is_valid_player_name_input2():
    player_name = ""
    result = is_valid_player_name_input(player_name)
    expected = False

    assert result == expected, f"Incorrect player name validation process\nExpected: {expected}\nReceived: {result}"


def test_is_valid_player_name_input3():
    player_name = "banana1"
    result = is_valid_player_name_input(player_name)
    expected = False

    assert result == expected, f"Incorrect player name validation process\nExpected: {expected}\nReceived: {result}"


def test_is_valid_player_name_input4():
    player_name = "banana 1"
    result = is_valid_player_name_input(player_name)
    expected = False

    assert result == expected, f"Incorrect player name validation process\nExpected: {expected}\nReceived: {result}"


def test_is_valid_player_name_input5():
    player_name = "banana one"
    result = is_valid_player_name_input(player_name)
    expected = True

    assert result == expected, f"Incorrect player name validation process\nExpected: {expected}\nReceived: {result}"