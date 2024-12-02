def read_input_file(filename):
    with open(filename, "r") as file:
        return file.read()

def check_sequence(line, min_diff = 1, max_diff = 3):
    if line == "":
        return False
    line_array = [int(number) for number in line.split(" ")]
    diffs = [line_array[i] - line_array[i + 1] for i in range(len(line_array) - 1)]
    if all(diff >= min_diff and diff <= max_diff for diff in diffs) or all(diff <= -min_diff and diff >= -max_diff for diff in diffs):
        return True
    return False

if __name__ == "__main__":
    data = read_input_file("../input.txt")
    lines = data.split("\n")
    safe_sequences = len([line for line in lines if check_sequence(line)])
    
    print(safe_sequences)
