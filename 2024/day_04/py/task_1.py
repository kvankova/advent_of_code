from pathlib import Path

def read_input_file(filename):
    with open(filename, "r") as file:
        return file.read()

def is_valid_position(row, col, grid):
    return 0 <= row < len(grid) and 0 <= col < len(grid[row])

def check_sequence(row, col, direction, grid):
    sequence = "XMAS"
    current_row, current_col = row, col
    
    for char in sequence:
        if not is_valid_position(current_row, current_col, grid):
            return False
        if grid[current_row][current_col] != char:
            return False
        current_row += direction[0]
        current_col += direction[1]
    return True

def count_xmas(puzzle):
    count = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), 
                 (1, 1), (1, -1), (-1, 1), (-1, -1)]
    grid = puzzle.split("\n")
    
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "X":
                for direction in directions:
                    if check_sequence(row, col, direction, grid):
                        count += 1
    return count

puzzle = read_input_file(Path(__file__).parents[1] / "input.txt")

print(count_xmas(puzzle))