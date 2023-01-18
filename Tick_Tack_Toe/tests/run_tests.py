from tests.board_tests import *
from tests.validators_tests import *

if __name__ == '__main__':
    print("Running board tests\n.\n.\n.")
    test_initialize_board()
    test_is_valid_board_size_input1()
    test_is_valid_board_size_input2()
    test_is_valid_board_size_input3()
    test_is_valid_board_size_input4()
    test_is_valid_board_size_input5()
    test_is_valid_player_name_input1()
    test_is_valid_player_name_input2()
    test_is_valid_player_name_input3()
    test_is_valid_player_name_input4()
    test_is_valid_player_name_input5()
    print(".\n.\n.\nFinished all tests")

# I could have written a lot of other tests, I wanted to practice more but had very little time to code until sunday
# I think I get the hang of it now and will add in the future special cases for different board combinations
# And also special cases for different input validation combinations
# With this said, I did test a lot of cases manually and hopefully the program is bug-free

