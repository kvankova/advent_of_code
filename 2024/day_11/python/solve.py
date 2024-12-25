from pathlib import Path

def read_input_file(filename):
    with open(filename, "r") as file:
        return file.read()

puzzle = [int(x) for x in read_input_file(Path(__file__).parents[1] / "input.txt").replace("\n", "").split(" ")]

def process_number(number: int) -> list[int]:
    if number == 0:
        return [1]  
    elif len(str(number)) % 2 == 0:
        return [int(str(number)[:len(str(number)) // 2]), int(str(number)[len(str(number)) // 2:])]
    else:
        return [number * 2024]

def process_line(line: list[int]) -> list[int]:
    result = []
    for number in line:
        result.extend(process_number(number))
    return result

for _ in range(25):
    puzzle = process_line(puzzle)

print(len(puzzle))