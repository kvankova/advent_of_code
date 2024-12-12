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

def generate_operations(input: Input, operators: list[str]) -> list[str]:
    operations = []
    for permutation in itertools.product(operators, repeat=len(input.numbers)-1):
        operations.append(permutation)
    return operations

def verify_operations(operations: list[tuple[str]], input: Input) -> bool:
    found = False
    for operation in operations:
        result = input.numbers[0]
        for i, operator in enumerate(operation):
            if operator == '+':
                result = result + input.numbers[i+1]
            elif operator == '*':
                result = result * input.numbers[i+1]
            elif operator == '||':
                result = int(str(result) + str(input.numbers[i+1]))
        if result == input.test_case:
            found = True
            break
    return found

def apply_elephant_operator(numbers: list[int], operation: tuple[str]) -> list[int]:
    numbers_str = ' '.join(map(str, numbers))
    for op in operation:
        numbers_str = numbers_str.replace(' ', op, 1)
    numbers_str = numbers_str.replace('||', '')
    return numbers_str


def solve1(puzzle):
    solution = 0
    for input in parse_puzzle(puzzle):
        operations = generate_operations(input, operators = ['+', '*'])
        if verify_operations(operations, input):
            solution += input.test_case
    return solution

def solve2(puzzle):
    solution = 0
    for input in parse_puzzle(puzzle):
        operations = generate_operations(input, operators = ['+', '*', '||'])
        if verify_operations(operations, input):
            solution += input.test_case
    return solution

print(solve1(puzzle))
print(solve2(puzzle))