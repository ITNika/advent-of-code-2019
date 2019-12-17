import unittest
import IntcodeComputer


class TestIntcodeComputer(unittest.TestCase):

    def test_initialize_memory(self):
        f = open("test_initialize_memory.txt", "w+")
        f.write("2,2,3,0,99")
        f.close()
        expected = [2, 2, 3, 0, 99]
        intcode_computer = IntcodeComputer.IntcodeComputer(f.name)
        self.assertEqual(expected, intcode_computer.memory)

    def test_perform_multiplication(self):
        f = open("test_perform_multiplication.txt", "w+")
        f.write("2,1,2,0,99")
        f.close()
        intcode_computer = IntcodeComputer.IntcodeComputer(f.name)
        intcode_computer.run_program()
        self.assertEqual(2, intcode_computer.read_memory(0))

    def test_perform_addition(self):
        f = open("test_perform_multiplication.txt", "w+")
        f.write("1,0,0,0,99")
        f.close()
        intcode_computer = IntcodeComputer.IntcodeComputer(f.name)
        intcode_computer.run_program()
        self.assertEqual(2, intcode_computer.read_memory(0))

    def test_multiple_instructions(self):
        f = open("test_multiple_instructions.txt", "w+")
        f.write("1,9,10,3,2,3,11,0,99,30,40,50")
        f.close()
        intcode_computer = IntcodeComputer.IntcodeComputer(f.name)
        intcode_computer.run_program()
        expected = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        self.assertEqual(expected, intcode_computer.memory)
