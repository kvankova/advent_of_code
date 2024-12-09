from pathlib import Path
from dataclasses import dataclass

def read_input_file(filename):
    with open(filename, "r") as file:
        return file.read()

@dataclass
class Guard:
    position: tuple[int, int]
    direction: tuple[int, int]

@dataclass
class Board:
    size: tuple[int, int]
    crates: list[tuple[int, int]]
    guard: Guard
    end: bool = False

def get_crates(puzzle: list[str]) -> list[tuple[int, int]]:
    return [(row, col) for row, line in enumerate(puzzle) for col, crate in enumerate(line) if crate == "#"]

def get_guard(puzzle: list[str]) -> Guard:
    for row, line in enumerate(puzzle):
        for col, crate in enumerate(line):
            if crate == "^":
                return Guard(position = (row, col), direction = (-1, 0))
            elif crate == "v":
                return Guard(position = (row, col), direction = (1, 0))
            elif crate == "<":
                return Guard(position = (row, col), direction = (0, -1))
            elif crate == ">":
                return Guard(position = (row, col), direction = (0, 1))

def print_board(board: Board):
    for row in range(board.size[0]):
        for col in range(board.size[1]):
            if (row, col) in board.crates:
                print("#", end="")
            elif (row, col) == board.guard.position:
                if board.guard.direction == (-1, 0):
                    print("^", end="")
                elif board.guard.direction == (1, 0):
                    print("v", end="")
                elif board.guard.direction == (0, -1):
                    print("<", end="")
                elif board.guard.direction == (0, 1):
                    print(">", end="")
            else:
                print(".", end="")
        print()


puzzle = read_input_file(Path(__file__).parents[1] / "input.txt").split("\n")[:-1]

visited_positions = set()

board = Board(
    size = (len(puzzle[0]), len(puzzle)),
    crates = get_crates(puzzle),
    guard = get_guard(puzzle)
)

def move_guard(board: Board) -> Board:
    global visited_positions
    # crate in the way
    
    if (
        board.guard.position[0] + board.guard.direction[0], 
        board.guard.position[1] + board.guard.direction[1]
    ) in board.crates:
        if board.guard.direction[0] != 0: # up or down
            board.guard.direction = (0, - board.guard.direction[0])
        else: # left or right
            board.guard.direction = (board.guard.direction[1], 0)
    # end of board
    elif (
        board.guard.position[0] + board.guard.direction[0] < 0 or
        board.guard.position[1] + board.guard.direction[1] < 0 or
        board.guard.position[0] + board.guard.direction[0] > board.size[0] - 1 or 
        board.guard.position[1] + board.guard.direction[1] > board.size[1] - 1
    ):
        board.end = True
    # move guard
    else:
        
        board.guard.position = (
            board.guard.position[0] + board.guard.direction[0], 
            board.guard.position[1] + board.guard.direction[1]
        )

    visited_positions.add(board.guard.position)
    return board

while not board.end:
    visited_positions.add(board.guard.position)
    board = move_guard(board)
    

print(len(visited_positions))