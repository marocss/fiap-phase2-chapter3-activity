import unittest
from unittest.mock import patch
from RM94562_EX01 import get_user_input


class TestBiduProgram(unittest.TestCase):
    # test valid input
    @patch('builtins.input', side_effect=['5'])
    def test_get_user_input_valid(self, _mock_input):
        self.assertEqual(get_user_input('Enter number: '), 5)

    # test invalid 0 input
    @patch('builtins.input', side_effect=['0', '3'])    # decorator provided by the unittest.mock module, used to
    # temporarily replace the input function in the builtins module with a mock object during the test
    def test_get_user_input_zero_then_valid(self, _mock_input):
        self.assertEqual(get_user_input('Enter number: '), 3)

    # test invalid negative input
    @patch('builtins.input', side_effect=['-1', '4'])
    def test_get_user_input_negative_then_valid(self, _mock_input):
        self.assertEqual(get_user_input('Enter number: '), 4)

    # test invalid string input
    @patch('builtins.input', side_effect=['abc', '6'])
    def test_get_user_input_string_then_valid(self, _mock_input):
        self.assertEqual(get_user_input('Enter number: '), 6)

    # test invalid float input
    @patch('builtins.input', side_effect=['2.2', '2'])
    def test_get_user_input_float_then_valid(self, _mock_input):
        self.assertEqual(get_user_input('Enter number: '), 2)

    # def test_get_collaborators_votes(self):
    #     print()
    #     # Add test cases...
    #
    # def test_get_preferred_week_day_or_days(self):
    #     self.assertEqual(get_preferred_week_day_or_days(['segunda-feira', 'terça-feira', 'segunda-feira']),
    #                      ['segunda-feira'])
    #     # Add more test cases...
    #
    # def test_check_best_week_day(self):
    #     print()
    #     # Add test cases...


if __name__ == '__main__':
    unittest.main()
