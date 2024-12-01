def read_input_file(filename):
    with open(filename, "r") as file:
        return file.read()

def parse_number_series(data):
    left_series = []
    right_series = []
    
    for line in data.split("\n"):
        if line == "":
            continue
        left, right = line.split("  ")
        left_series.append(int(left))
        right_series.append(int(right))
        
    return left_series, right_series

def calculate_difference_sum(left_series, right_series):
    left_series.sort()
    right_series.sort()
    return sum(abs(left - right) for left, right in zip(left_series, right_series))

def main():
    data = read_input_file("../input.txt")
    left_series, right_series = parse_number_series(data)
    result = calculate_difference_sum(left_series, right_series)
    print(result)

if __name__ == "__main__":
    main()
