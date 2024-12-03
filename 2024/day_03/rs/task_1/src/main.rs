use regex::Regex;

fn main() {
    let data: String = std::fs::read_to_string("../../input.txt").unwrap();
    let chunks: Vec<&str> = data.split("\n").collect();
    let mut sum_of_multiplied_numbers = 0;

    for chunk in chunks {
        sum_of_multiplied_numbers += multiply_numbers(chunk);
    }

    println!("{}", sum_of_multiplied_numbers);
}

fn multiply_numbers(line: &str) -> i32 {
    let re = Regex::new(r"mul\([0-9]{1,3},[0-9]{1,3}\)").unwrap();
    let all_matches = re.find_iter(line);
    
    let mut all_matches_vec: Vec<Vec<i32>> = Vec::new();
    for found_match in all_matches {
        let match_str = found_match.as_str();
        let match_str_without_mul = match_str.replace("mul(", "").replace(")", "");
        let match_str_without_mul_split = (
            match_str_without_mul.split(",")
                .map(|s| s.parse::<i32>().unwrap())
                .collect::<Vec<i32>>()
        );
        all_matches_vec.push(match_str_without_mul_split);
    }

    let multiplied_numbers = all_matches_vec.iter().map(|v| v[0] * v[1]).collect::<Vec<i32>>(); 
    return multiplied_numbers.iter().sum::<i32>();
}

