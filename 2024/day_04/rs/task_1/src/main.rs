fn main() {
    let data: String = std::fs::read_to_string("../../input.txt").unwrap();
    println!("{}", count_xmas(data));
}

fn is_valid_position(row: i32, col: i32, nrow: usize, ncol: usize) -> bool {
    if row >= 0 && row < nrow as i32 && col >= 0 && col < ncol as i32 {
        return true;
    }
    false
}

fn check_sequence(row: usize, col: usize, direction: (i32, i32), grid: &Vec<Vec<char>>, nrow: usize, ncol: usize) -> bool {
    let sequence = "XMAS";
    let mut current_row: i32 = row as i32;
    let mut current_col: i32 = col as i32;
    for char in sequence.chars() {
        if !is_valid_position(current_row, current_col, nrow, ncol) {
            return false;
        }
        let usize_current_row = current_row as usize;
        let usize_current_col = current_col as usize;   
        if grid[usize_current_row][usize_current_col] != char { 
            return false;
        }
        current_row += direction.0;
        current_col += direction.1;
    }
    true
}

fn count_xmas(puzzle: String) -> usize {
    let mut grid: Vec<Vec<char>> = puzzle.split("\n").map(|line| line.chars().collect()).collect();
    // remove last empty line
    grid.pop();
    
    let directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)];
    let mut count = 0;
    let nrow = grid.len();
    let ncol = grid[0].len();

    for row in 0..nrow {
        for col in 0..ncol {
            if grid[row][col] == 'X' {
                for direction in directions {
                    if check_sequence(row, col, direction, &grid, nrow, ncol) {
                        count += 1;
                    }
                }
            }
        }
    }
    count   
}

