use std::collections::HashMap;

fn main() {
    let data: String = std::fs::read_to_string("../../input.txt").unwrap();
    
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

    let mut left_series_dict: HashMap<i32, i32> = HashMap::new();
    for number in left_series {
        left_series_dict.insert(number, left_series_dict.get(&number).unwrap_or(&0) + 1);
    }

    let mut right_series_dict: HashMap<i32, i32> = HashMap::new();
    for number in right_series {
        right_series_dict.insert(number, right_series_dict.get(&number).unwrap_or(&0) + 1);
    }

    let mut similarity_score: i32 = 0;
    for (number, count) in left_series_dict.iter() {
        similarity_score += number * count * right_series_dict.get(number).unwrap_or(&0);
    }

    println!("{}", similarity_score);
}
