from pathlib import Path

def read_input_file(filename):
    with open(filename, "r") as file:
        return file.read()

def is_valid_position(row, col, grid):
    return 0 <= row < len(grid) and 0 <= col < len(grid[row])

def check_diagonal(row, col, grid, direction):
    found_chars = []
    for direction in direction:
        current_row = row + direction[0]
        current_col = col + direction[1]
        if not is_valid_position(current_row, current_col, grid):
            return []
        found_chars.append(grid[current_row][current_col])
    return found_chars

def check_mas_sequence(row, col, grid):
    lr_found_chars = check_diagonal(row, col, grid, [(1, 1), (-1, -1)])
    rl_found_chars = check_diagonal(row, col, grid, [(1, -1), (-1, 1)])
    return set(["M", "S"]) == set(lr_found_chars) and set(["M", "S"]) == set(rl_found_chars)


def find_x_mas(puzzle):
    grid = puzzle.split("\n")
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "A":
                if check_mas_sequence(row, col, grid):
                    count += 1
    return count

puzzle = read_input_file(Path(__file__).parents[1] / "input.txt")

print(find_x_mas(puzzle))

