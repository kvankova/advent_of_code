fn main() {
    let data: String = std::fs::read_to_string("../../input.txt").unwrap();
    let chunks: Vec<&str> = data.split("\n").collect();

    let mut safe_sequences = 0;

    for chunk in &chunks {  
        if chunk.is_empty() {
            continue;
        }
        let line: Vec<i32> = chunk.split_whitespace().map(|s| s.parse().unwrap()).collect();
        println!("{:?}", line);
        if check_sequence(line) {
            safe_sequences += 1;
        }
    }
    println!("{}", safe_sequences);
}

fn check_sequence(line: Vec<i32>) -> bool {
    let diffs: Vec<i32> = line.iter().zip(line.iter().skip(1)).map(|(a, b)| a - b).collect();
    if diffs.iter().all(|&diff| diff >= 1 && diff <= 3) || diffs.iter().all(|&diff| diff <= -1 && diff >= -3) { 
        return true;
    }
    false
}
