'''LIBRARY FILE'''

import re

# ASSEMBLER CODE


class Assembler:
    # Fake assembling....

    @staticmethod
    def assemble_code(code):
        ln, assembly = 0, {}
        for line in code.strip().splitlines():
            if line != '':
                assembly[ln] = line.strip()
                ln += 1
        return assembly

# SIMULATOR CODE
def is_number(s):
    if s.isdigit():  # Integer
        return True
    elif re.match(r'\d+\.\d+', s):  # Float
        return True
    return False


class AssemblySimulation:

    NUMERICAL_INSTRUCTIONS = ('ADD', 'SUB', 'MUL', 'DIV', 'POW', 'MOD', 'FDV')

    def __init__(self):  # Constructor
        self.__variables = {}
        # Equal, Not Equal, Greater Than, Less Than
        self.__status_register = (None, None, None, None)

    def __fetch_variable(self, var):
        if var.isdigit():
            return int(var)
        elif is_number(var):
            return float(var)
        else:
            return self.__variables[var]

    # Method to execute assembly code
    def execute_assembly_code(self, assembly_code, input_func, output_func, debug=False):
        output = []
        ln = 0
        try:
            while True:
                ln = int(ln)
                line = assembly_code[ln]
                if debug:
                    yield ln, self.__variables, self.__status_register, output
                if line == 'HLT':
                    break
                opcode, operand = line.split(' ')[0], line.split(' ')[1:]
                if opcode in self.NUMERICAL_INSTRUCTIONS:  # Numerical instruction
                    var, op1, op2 = operand
                    num1, num2 = self.__fetch_variable(
                        op1), self.__fetch_variable(op2)
                    match opcode:
                        case 'ADD': self.__variables[var] = num1 + num2
                        case 'SUB': self.__variables[var] = num1 - num2
                        case 'MUL': self.__variables[var] = num1 * num2
                        case 'DIV': self.__variables[var] = num1 / num2
                        case 'POW': self.__variables[var] = num1 ** num2
                        case 'MOD': self.__variables[var] = num1 % num2
                        case 'FDV': self.__variables[var] = num1 // num2
                    ln += 1

                elif opcode == 'STO':  # Store instruction
                    var, op = operand
                    number = self.__fetch_variable(op)
                    self.__variables[var] = number
                    ln += 1

                elif opcode == 'CMP':  # Compare instruction
                    lhs, rhs = operand
                    num1, num2 = self.__fetch_variable(
                        lhs), self.__fetch_variable(rhs)
                    self.__status_register = (
                        num1 == num2, num1 != num2, num1 > num2, num1 < num2)
                    ln += 1

                elif opcode[0] == 'B':  # Branch instruction
                    address = float(operand[0])
                    if opcode == 'BAL':
                        ln = address
                    elif opcode == 'BEQ' and self.__status_register[0] or opcode == 'BNE' and self.__status_register[1] or \
                            opcode == 'BGT' and self.__status_register[2] or opcode == 'BLT' and self.__status_register[3]:
                        ln = address
                    else:
                        ln += 1

                elif opcode == 'OUT':  # Output instruction

                    if is_number(operand[0]):  # number
                        val = int(operand[0]) if operand[0].isdigit(
                        ) else float(operand[0])

                    else:  # variable
                        val = self.__variables[operand[0]]

                    output_func(val)
                    output.append(val)
                    ln += 1

                elif opcode == 'INP':  # Input instruction
                    variable_name = operand[0]
                    while True:
                        try:
                            self.__variables[variable_name] = int(
                                input_func('input: '))
                            break
                        except ValueError:
                            output_func('Only integers can be entered')
                    ln += 1

        except Exception as err:
            output_func(f'Error occurred on line {ln}: {err}')

