def perform_addition(program, operand_one_position, operand_two_position, result_position):
	program[result_position] = (int(program[operand_one_position]) + int(program[operand_two_position]))

def perform_multiplication(program, operand_one_position, operand_two_position, result_position):
	program[result_position] = int(program[operand_one_position]) * int(program[operand_two_position])


def run_program(program):
	running = True
	current_position = 0
	current_value = int(program[current_position])
	while running:
		print(program)
		if current_value == 99:
			print("Program reached the end.")
			running = False
		elif current_value == 1:
			perform_addition(program, program[current_position + 1], program[current_position + 2], program[current_position + 3])
			current_position += 4
			current_value = int(program[current_position])
		elif current_value == 2:
			perform_multiplication(program, program[current_position + 1], program[current_position + 2], program[current_position + 3])
			current_position +=4
			current_value= int(program[current_position])
		else:
			print("Program found unknown opcode")
			running = False


file = open('input-files/input_day2_1.txt', 'r')
input_string = str(file.readline())
program = input_string.split(',')

program[1] = 12
program[2] = 2
run_program(program)
print("The value on position 0 is {}.".format(program[0]))
