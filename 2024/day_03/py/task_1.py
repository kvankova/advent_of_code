import re

def read_input_file(filename):
    with open(filename, "r") as file:
        return file.read()

def test_case():
    return 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'

def multiply_numbers(line):
    all_matches = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', line)
    extract_numbers = lambda match: [int(num) for num in match.replace('mul(', '').replace(')', '').split(',')]
    extracted_numbers = list(map(extract_numbers, all_matches))
    multiplied_numbers = [a * b for a, b in extracted_numbers]

    return sum(multiplied_numbers)

if __name__ == "__main__":
    data = read_input_file("./input.txt")
    lines = data.split("\n")
    print(sum([multiply_numbers(line) for line in lines]))
