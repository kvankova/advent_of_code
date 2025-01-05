use std::collections::HashSet;
fn main() {
    let data: String = std::fs::read_to_string("../../input.txt").unwrap();
    println!("{}", find_x_mas(data));
}

fn is_valid_position(row: i32, col: i32, nrow: usize, ncol: usize) -> bool {
    if row >= 0 && row < nrow as i32 && col >= 0 && col < ncol as i32 {
        return true;
    }
    false
}

fn check_diagonal(row: usize, col: usize, direction: Vec<(i32, i32)>, grid: &Vec<Vec<char>>) -> Vec<char> {
    let mut found_chars = Vec::new();
    for direction in direction {
        let current_row: i32 = row as i32 + direction.0;
        let current_col: i32 = col as i32 + direction.1;
        if !is_valid_position(current_row, current_col, grid.len(), grid[0].len()) {
            return Vec::new();
        }
        found_chars.push(grid[current_row as usize][current_col as usize]);
    }
    found_chars
}

fn check_mas_sequence(row: usize, col: usize, grid: &Vec<Vec<char>>) -> bool {
    let lr_found_chars = check_diagonal(row, col, vec![(1, 1), (-1, -1)], grid);
    let rl_found_chars = check_diagonal(row, col, vec![(1, -1), (-1, 1)], grid);
    // check if the found characters are "M" and "S" and only them 
    let lr_set: HashSet<char> = HashSet::from_iter(lr_found_chars.iter().cloned());
    let rl_set: HashSet<char> = HashSet::from_iter(rl_found_chars.iter().cloned());
    if lr_set == HashSet::from(['M', 'S']) && rl_set == HashSet::from(['M', 'S']) {
        return true;
    }
    false
}

fn find_x_mas(puzzle: String) -> usize {
    let mut grid: Vec<Vec<char>> = puzzle.split("\n").map(|line| line.chars().collect()).collect();
    // remove last empty line
    grid.pop();
    let nrow = grid.len();
    let ncol = grid[0].len();

    let mut count = 0;
    for row in 0..nrow {
        for col in 0..ncol {
            if grid[row][col] == 'A' {
                if check_mas_sequence(row, col, &grid) {
                    count += 1;
                }
            }
        }
    }
    count
}


