import unittest


import day2


class TestDay2(unittest.TestCase):

    def test_perform_multiplication(self):
        test_list = [2, 2, 3, 0]
        day2.perform_multiplication(test_list, 1,2,0)
        self.assertTrue(test_list[0] == 6)

    def test_perform_addition(self):
        test_list = [1, 0, 0, 0]
        day2.perform_addition(test_list, 0, 0, 0)
        self.assertTrue(test_list[0] == 2)

    def test_run_program(self):
        test_program = [1, 0, 0, 0, 99]
        expected_result = [2, 0, 0, 0, 99]
        day2.run_program(test_program)
        print(test_program)
        print(expected_result)
        self.assertEqual(test_program, expected_result)
