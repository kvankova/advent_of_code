from pathlib import Path
from dataclasses import dataclass
import itertools

def read_input_file(filename):
    with open(filename, "r") as file:
        return file.read()

@dataclass
class Input:
    test_case: int
    numbers: list[int]

puzzle = read_input_file(Path(__file__).parents[1] / "input.txt").split("\n")[:-1]

def parse_puzzle(puzzle):
    return [Input(int(line.split(":")[0]), [int(x) for x in line.split(":")[1].split(" ") if x]) for line in puzzle]

def generate_operations(input: Input) -> list[str]:
    operations = []
    operators = ['+', '*']
    for permutation in itertools.product(operators, repeat=len(input.numbers)):
        operations.append(permutation)
    return operations

def verify_operations(operations: list[str], input: Input) -> bool:
    found = False
    for operation in operations:
        result = 0
        for i in range(len(input.numbers)):
            if operation[i] == '+':
                result = result + input.numbers[i]
            elif operation[i] == '*':
                result = result * input.numbers[i]
        if result == input.test_case:
            found = True
            break
    return found

solution = 0
for input in parse_puzzle(puzzle):
    operations = generate_operations(input)
    if verify_operations(operations, input):
        solution += input.test_case
print(solution)
