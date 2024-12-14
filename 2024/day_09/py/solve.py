from pathlib import Path

def read_input_file(filename):
    with open(filename, "r") as file:
        return file.read()

puzzle = read_input_file(Path(__file__).parents[1] / "input.txt").replace("\n", "")

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

def move_files1(sequence: list) -> list:
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

def get_free_spaces(sequence: list) -> list[tuple[int, int]]:
    # get positions of free spaces
    free_spaces = []
    new_free_space = False
    start, end = None, None
    for i, item in enumerate(sequence):
        if item == "." and not new_free_space:
            start = i
            new_free_space = True
        elif item == "." and new_free_space:
            end = i
        elif item != ".":
            new_free_space = False
            if start is not None:
                free_spaces.append((start, end if end is not None else i-1))
            start, end = None, None
    return free_spaces

def get_files(sequence: list) -> list:
    files = {}
    for i, item in enumerate(sequence):
        if item != ".":
            if item not in files:
                files[item] = []
            files[item].append(i)

    for file in files:
        files[file] = (min(files[file]), max(files[file]))

    return files

def move_files2(sequence: list) -> list:
    files = get_files(sequence)
    for file in sorted(files, reverse=True):
        free_spaces = get_free_spaces(sequence)
        file_length = files[file][1] - files[file][0] + 1
        for free_space in free_spaces:
            if free_space[1] - free_space[0] + 1 >= file_length and free_space[0] < files[file][0]:
                sequence[free_space[0]: free_space[0]+file_length] = [file] * file_length
                sequence[files[file][0]:files[file][1]+1] = ["."] * file_length
                break
    return sequence
    
    
    
    return sequence

def get_checksum(sequence: list) -> int:
    return sum(int(sequence[i]) * i for i in range(len(sequence)) if sequence[i] != ".")

# first task
transformed_puzzle_1 = transform_puzzle_to_sequence(puzzle)
moved_puzzle_1 = move_files1(transformed_puzzle_1)
print(get_checksum(moved_puzzle_1))

# second task
transformed_puzzle_2 = transform_puzzle_to_sequence(puzzle)
moved_puzzle_2 = move_files2(transformed_puzzle_2)
print(get_checksum(moved_puzzle_2))
