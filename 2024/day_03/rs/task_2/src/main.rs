use regex::Regex;

fn main() {
    let data: String = std::fs::read_to_string("../../input.txt").unwrap();
    let chunks: Vec<&str> = data.split("\n").collect();

    let mut sum_of_multiplied_numbers = 0;
    sum_of_multiplied_numbers = multiply_numbers(chunks);

    println!("{}", sum_of_multiplied_numbers);
}

fn multiply_numbers(chunks: Vec<&str>) -> i32 {
    let re = Regex::new(r"do\(\)|don't\(\)|mul\([0-9]{1,3},[0-9]{1,3}\)").unwrap();
    let mut sum_of_multiplied_numbers = 0;
    let mut flag = true;

    for line in chunks {
        let all_matches = re.find_iter(line);
        for found_match in all_matches {
            let match_str = found_match.as_str();
            if match_str == "do()" {
                flag = true;
            } else if match_str == "don't()" {
                flag = false;
            } else {
                if flag {
                    let numbers = match_str.replace("mul(", "").replace(")", "").split(",").map(|s| s.parse::<i32>().unwrap()).collect::<Vec<i32>>();
                    sum_of_multiplied_numbers += numbers[0] * numbers[1];
                }
            }
        }
    }

    return sum_of_multiplied_numbers;
}

