from pathlib import Path
from dataclasses import dataclass
from typing import Callable
def read_input_file(filename):
    with open(filename, "r") as file:
        return file.read()

puzzle = read_input_file(Path(__file__).parents[1] / "input.txt").split("\n")[:-1]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

@dataclass
class Trailhead:
    location: tuple[int, int]
    path: list[tuple[int, int]]
    trailhead_start: tuple[int, int]
    current_value: int
    score: int = 0

def find_trailhead(puzzle: list[list[str]]) -> list[Trailhead]:
    trailheads = []
    for row in range(len(puzzle)):
        for col in range(len(puzzle[row])):
            if puzzle[row][col] == "0":
                trailheads.append(Trailhead(location=(row, col), trailhead_start=(row, col), current_value=0, path=[(row, col)]))
    return trailheads

puzzle = [list(row) for row in puzzle]

all_trailheads = find_trailhead(puzzle)
def move_trailhead(trailhead: Trailhead, puzzle: list[list[str]], directions: list[tuple[int, int]]) -> list[Trailhead]:
    def is_valid_location(loc: tuple[int, int]) -> bool:
        row, col = loc
        return 0 <= row < len(puzzle) and 0 <= col < len(puzzle)
    
    def create_new_location(direction: tuple[int, int]) -> tuple[int, int]:
        return (trailhead.location[0] + direction[0], trailhead.location[1] + direction[1])
        
    def is_next_value(loc: tuple[int, int]) -> bool:
        return puzzle[loc[0]][loc[1]] == str(trailhead.current_value + 1)
        
    def create_trailhead(loc: tuple[int, int]) -> Trailhead:
        return Trailhead(
            location=loc,
            path=trailhead.path + [loc],
            score=trailhead.score + (1 if puzzle[loc[0]][loc[1]] == "9" else 0),
            current_value=trailhead.current_value + 1,
            trailhead_start=trailhead.trailhead_start
        )

    possible_moves = []
    for direction in directions:
        new_loc = create_new_location(direction)
        if is_valid_location(new_loc) and is_next_value(new_loc):
            possible_moves.append(create_trailhead(new_loc))
            
    return possible_moves

# run recursively
def run_recursively(trailhead: Trailhead, puzzle: list[list[str]], directions: list[tuple[int, int]]) -> Trailhead:
    results = []
    possible_moves = move_trailhead(trailhead, puzzle, directions)
    if len(possible_moves) == 0:
        return trailhead
    for move in possible_moves:
        results.append(run_recursively(move, puzzle, directions))
    return results

def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list


def process_trailhead_results_task1(trailhead: Trailhead, puzzle: list[list[str]], directions: list[tuple[int, int]]) -> set[tuple[int, int]]:
    results = run_recursively(trailhead, puzzle, directions)
    flattened_results = flatten(results)
    return {result.location for result in flattened_results if result.score == 1} 


def process_trailhead_results_task2(trailhead: Trailhead, puzzle: list[list[str]], directions: list[tuple[int, int]]) -> set[tuple[int, int]]:
    results = run_recursively(trailhead, puzzle, directions)
    flattened_results = flatten(results)
    return {tuple(result.path) for result in flattened_results if result.score == 1} 

def calculate_total_score(trailheads: list[Trailhead], puzzle: list[list[str]], directions: list[tuple[int, int]], process_trailhead_results: Callable[[Trailhead, list[list[str]], list[tuple[int, int]]], set[tuple[int, int]]]) -> int:
    trailhead_scores = {}
    for trailhead in trailheads:
        trailhead_scores[trailhead.trailhead_start] = process_trailhead_results(trailhead, puzzle, directions)
    
    return sum(len(locations) for locations in trailhead_scores.values())

total_score_task1 = calculate_total_score(all_trailheads, puzzle, directions, process_trailhead_results_task1)
print(total_score_task1)

total_score_task2 = calculate_total_score(all_trailheads, puzzle, directions, process_trailhead_results_task2)
print(total_score_task2)
