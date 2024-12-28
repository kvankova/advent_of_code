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
    
def process_memory(memory: dict[int, int]) -> dict[int, int]:
    tmp = {}
    for number, count in memory.items():
        processed_numbers = process_number(number)
        for processed_number in processed_numbers:
            tmp[processed_number] = tmp.get(processed_number, 0) + count
    return tmp

def calculate_result(iterations: int) -> int:
    memory = {i: 1 for i in puzzle}
    
    for _ in range(iterations):
        memory = process_memory(memory)
    
    return sum(memory.values())

print(calculate_result(75))
