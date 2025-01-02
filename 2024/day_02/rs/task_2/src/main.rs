fn main() {
    let data: String = std::fs::read_to_string("../../input.txt").unwrap();
    let chunks: Vec<&str> = data.split("\n").collect();

    let mut safe_sequences = 0;

    for (i, chunk) in chunks.iter().enumerate() {  
        if chunk.is_empty() {
            continue;
        }
        let line: Vec<i32> = chunk.split_whitespace().map(|s| s.parse().unwrap()).collect();
        if check_sequence(line.clone()) {
            safe_sequences += 1;
        }
    }
    println!("{}", safe_sequences);
}

fn check_sequence(line: Vec<i32>) -> bool {
    let diffs: Vec<i32> = line.iter().zip(line.iter().skip(1)).map(|(a, b)| a - b).collect();

    if check_strict_sequence(diffs.clone()) { 
        return true;
    }


    for i in 0..diffs.len()+1 {
        
        let mut modified_diffs = diffs.clone();
        if i == 0 {
            modified_diffs = modified_diffs[1..].to_vec(); 
        } else if i == diffs.len() {
            modified_diffs = modified_diffs[..diffs.len()-1].to_vec();
        } else {
            modified_diffs = [modified_diffs[..i-1].to_vec(), vec![modified_diffs[i-1] + modified_diffs[i]], modified_diffs[i+1..].to_vec()].concat();
        }
        if check_strict_sequence(modified_diffs) {
            return true;
        }
    }
    false
}

fn check_strict_sequence(diffs: Vec<i32>) -> bool {
    if diffs.iter().all(|&diff| diff >= 1 && diff <= 3) || diffs.iter().all(|&diff| diff <= -1 && diff >= -3) { 
        return true;
    }
    false
}