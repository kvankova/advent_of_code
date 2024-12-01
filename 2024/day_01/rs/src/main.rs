fn main() {
    let data: String = std::fs::read_to_string("../input.txt").unwrap();
    
    let chunks: Vec<&str> = data.split("\n").collect();
    let mut left_series: Vec<i32> = Vec::new();
    let mut right_series: Vec<i32> = Vec::new();

    for chunk in &chunks {
        if chunk.is_empty() {
            continue;
        }
        let parts: Vec<i32> = chunk.split_whitespace().map(|s| s.parse().unwrap()).collect();
        left_series.push(parts[0]);
        right_series.push(parts[1]);
    }

    left_series.sort();
    right_series.sort();

    let mut distance: i32 = 0;

    for i in 0..left_series.len() {
        distance += (left_series[i] - right_series[i]).abs();
    }

    println!("{}", distance);
}
