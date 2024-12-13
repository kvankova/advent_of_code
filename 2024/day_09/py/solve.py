from pathlib import Path

def read_input_file(filename):
    with open(filename, "r") as file:
        return file.read()

puzzle = read_input_file(Path(__file__).parents[1] / "input.txt").replace("\n", "")
#puzzle = "2333133121414131402"

def transform_puzzle_to_sequence(puzzle: str) -> list:
    result = []
    id = -1
    for i, item in enumerate(puzzle):
        # if it's a file
        if i%2 == 0:
            id += 1
            for _ in range(int(item)):
                result.append(id)
        # else it's a free space
        else:
            for _ in range(int(item)):
                result.append(".")
    return result

def move_files(sequence: list) -> list:
    all_files_moved = False
    while not all_files_moved:
        for i in range(len(sequence)):
            if sequence[i] == ".":
                leftmost_free_space = i
                break
        for i in range(len(sequence)-1, -1, -1):
            if sequence[i] != ".":
                rightmost_file = i
                break
        if leftmost_free_space > rightmost_file:
            all_files_moved = True
        else:
            sequence[leftmost_free_space] = sequence[rightmost_file]
            sequence[rightmost_file] = "."
        
    return sequence

def get_checksum(sequence: list) -> int:
    return sum(int(sequence[i]) * i for i in range(len(sequence)) if sequence[i] != ".")


transformed_puzzle = transform_puzzle_to_sequence(puzzle)
moved_puzzle = move_files(transformed_puzzle)
print(get_checksum(moved_puzzle))
