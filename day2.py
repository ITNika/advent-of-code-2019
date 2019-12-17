import IntcodeComputer
divider = "----------------------------------"
print(divider)
print("Day two part one")
print(divider)

intcode_computer = IntcodeComputer.IntcodeComputer("input-files/input_day2_1.txt")
intcode_computer.set_memory(1, 12)
intcode_computer.set_memory(2,2)
intcode_computer.run_program()
print("The value at address 0 is {}".format(intcode_computer.read_memory(0)))

print(divider)
print("Day two part two")
print(divider)

verb = 0
noun = 0
while verb <= 99:
    while noun <= 99:
        intcode_computer = IntcodeComputer.IntcodeComputer("input-files/input_day2_1.txt")
        intcode_computer.set_memory(1, noun)
        intcode_computer.set_memory(2, verb)
        intcode_computer.run_program()
        if intcode_computer.read_memory(0) == 19690720:
            print("The noun is {} and the verb is {}".format(noun, verb))
            exit(0)
        noun += 1
    noun = 0
    verb += 1
