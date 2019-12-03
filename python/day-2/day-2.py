from typing import List
from enum import Enum, auto


class Opcode(Enum):
    ADD = 1
    MULTIPLY = 2
    EXIT = 99


def extract_program_from_file(path_to_intcode_program: str) -> List[int]:
    with open(path_to_intcode_program) as program_file:
        raw_program = next(program_file)
    return [int(intcode) for intcode in raw_program.split(',')]


def process_program(intcode_program: List[int]):
    program_length = len(intcode_program)
    current_index = 0

    while current_index < program_length:
        current_opcode = Opcode(intcode_program[current_index])
        print(f'Current opcode: {current_opcode}')
        if current_opcode == Opcode.ADD:
            first_input_position, second_input_position, output_position = intcode_program[current_index + 1: current_index + 4]
            intcode_program[output_position] = intcode_program[first_input_position] + intcode_program[second_input_position]
            current_index += 4
        elif current_opcode == Opcode.MULTIPLY:
            first_input_position, second_input_position, output_position = intcode_program[current_index + 1: current_index + 4]
            intcode_program[output_position] = intcode_program[first_input_position] * intcode_program[second_input_position]
            current_index += 4
        else:
            break


def main():
    path_to_program = 'day-2/day-2_input.txt'
    intcode_program = extract_program_from_file(path_to_program)
    
    # fudge the input program for part 1
    intcode_program[1] = 12
    intcode_program[2] = 2

    process_program(intcode_program)
    print(intcode_program)





if __name__ == '__main__':
    main()
