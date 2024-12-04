import re

def read_input_file(filename):
    with open(filename, "r") as file:
        return file.read()

def test_case():
    return "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def multiply_numbers(content):
    regex = r"do\(\)|don't\(\)|mul\([0-9]{1,3},[0-9]{1,3}\)"
    flag = True
    cum_sum = 0
    for line in content: 
        matches = re.findall(regex, line)
        for match in matches:
            if match == "do()":
                flag = True
            elif match == "don't()":
                flag = False
            else:
                if flag:
                    numbers = match.replace("mul(", "").replace(")", "").split(",")
                    cum_sum += int(numbers[0]) * int(numbers[1])
    return cum_sum

if __name__ == "__main__":
    data = read_input_file("input.txt")
    lines = data.split("\n")
    print(multiply_numbers(lines))