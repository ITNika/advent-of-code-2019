class IntcodeComputer:

    def perform_addition(self, operand_one_position, operand_two_position, result_position):
        operand_one = self.read_memory(operand_one_position)
        operand_two = self.read_memory(operand_two_position)
        self.set_memory(result_position, operand_one + operand_two)

    def perform_multiplication(self, operand_one_position, operand_two_position, result_position):
        operand_one = self.read_memory(operand_one_position)
        operand_two = self.read_memory(operand_two_position)
        self.set_memory(result_position, operand_one * operand_two)

    opcodes = {
        1: {"function": perform_addition, "arguments": 3},
        2: {"function": perform_multiplication, "arguments": 3},
        99: {"function": "halt"}
    }

    def get_argument_positions(self, arguments):
        arg_positions = []
        i = 1
        while i <= arguments:
            arg_positions.append(self.read_memory(self.instruction_pointer + i))
            i += 1
        return arg_positions

    def execute_instruction(self):
        opcode = self.memory[self.instruction_pointer]
        if opcode in IntcodeComputer.opcodes:
            function = IntcodeComputer.opcodes.get(opcode).get("function")
            number_arguments = IntcodeComputer.opcodes.get(opcode).get("arguments")
            # execute function
            if function == "halt":
                # halt execution
                self.running = False
            else:
                function(self, *self.get_argument_positions(number_arguments))
                # increment instruction_pointer to next instruction
                self.instruction_pointer = self.instruction_pointer + number_arguments + 1
        else:
            print("Program found unknown opcode {} at address {}".format(
                self.memory[self.instruction_pointer],
                self.instruction_pointer)
            )
            self.running = False

    def set_memory(self, address, value):
        self.memory[address] = value

    def read_memory(self, address):
        return self.memory[address]

    @staticmethod
    def initialize_memory(input_file):
        file = open(input_file, 'r')
        input_string = str(file.readline())
        file.close()
        return list(map(int, input_string.split(',')))

    def run_program(self):
        while self.running:
            self.execute_instruction()

    def __init__(self, input_file):
        self.input_file = input_file
        self.memory = IntcodeComputer.initialize_memory(input_file)
        self.instruction_pointer = 0
        self.running = True
