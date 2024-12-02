def read_input_file(filename):
    with open(filename, "r") as file:
        return file.read()

def sum_odd_element(diffs, odd_element):
    modified_diffs = []
    skip_index = -1
    for idx, diff in enumerate(diffs):
        if skip_index == idx:
            continue
        elif diff == odd_element:
            modified_diffs.append(diff + diffs[idx + 1])
            skip_index = idx + 1 
        else:
            modified_diffs.append(diff)
    return modified_diffs

def condition_met(diffs, min_diff = 1, max_diff = 3):
    return (
        all(diff >= min_diff and diff <= max_diff for diff in diffs) or 
        all(diff <= -min_diff and diff >= -max_diff for diff in diffs)
    )

def check_sequence(line):
    if line == "":
        return False
    line_array = [int(number) for number in line.split(" ")]
    diffs = [line_array[i] - line_array[i + 1] for i in range(len(line_array) - 1)]
    
    # is strictly increasing or decreasing
    if condition_met(diffs):
        return True
    else:
        for i in range(len(diffs)+1):
            if i == 0:
                modified_diffs = diffs[1:]
            elif i == len(diffs):
                modified_diffs = diffs[:-1]
            else:
                modified_diffs = diffs[:i-1] + [diffs[i-1] + diffs[i]] + diffs[i+1:]
            if condition_met(modified_diffs):
                return True
        return False
        

if __name__ == "__main__":
    data = read_input_file("./input.txt")
    lines = data.split("\n")
    safe_sequences = [line for line in lines if check_sequence(line)]
    unsafe_sequences = [line for line in lines if not check_sequence(line)]
    for i, line in enumerate(unsafe_sequences):
        print(line)
    print(len(safe_sequences))
