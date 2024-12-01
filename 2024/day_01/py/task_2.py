from task_1 import read_input_file, parse_number_series

def calculate_similarity_score(left_series: list[int], right_series: list[int]) -> int:
    left_series_dict = {}
    right_series_dict = {}

    for number in left_series:
        left_series_dict[number] = left_series_dict.get(number, 0) + 1

    for number in right_series:
        right_series_dict[number] = right_series_dict.get(number, 0) + 1

    similarity_score = 0

    for number in left_series_dict:
        similarity_score += number * left_series_dict[number] * right_series_dict.get(number, 0)

    return similarity_score

if __name__ == "__main__":  
    data = read_input_file("./input.txt")
    left_series, right_series = parse_number_series(data)
    print(calculate_similarity_score(left_series, right_series))


