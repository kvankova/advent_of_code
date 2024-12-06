from pathlib import Path

def read_input_file(filename):
    with open(filename, "r") as file:
        return file.read()

def parse_report(report: str) -> list[int]:
    report = report.split(",")
    return [int(i) for i in report]

def parse_rules(rules: list[str]) -> list[tuple[int, int]]:
    parsed_rules = []
    for rule in rules:
        parsed_rules.append((int(rule.split('|')[0]), int(rule.split('|')[1])))
    return parsed_rules

def filter_relevant_rules(report: list[int], rules: list[tuple[int, int]]) -> list[tuple[int, int]]:
    return [rule for rule in rules if (rule[0] in report) and (rule[1] in report)]

def retrieve_idx(num: int, report: list[int]) -> int:
    for i, report_num in enumerate(report):
        if num == report_num:
            return i
        
def check_report(report: list[int], rules: list[tuple[int, int]]) -> tuple[list[int], bool]:
    fixed_report = report.copy()
    is_wrong = False
    for rule in rules:
        left_idx = retrieve_idx(rule[0], fixed_report)
        right_idx = retrieve_idx(rule[1], fixed_report) 
        if right_idx < left_idx:
            is_wrong = True
            fixed_report.pop(left_idx)
            fixed_report.insert(left_idx, rule[1])
            fixed_report.pop(right_idx)
            fixed_report.insert(right_idx, rule[0])
        
    return fixed_report, is_wrong

def retrieve_middle(report: list[int]) -> int:
    middle_index = len(report) // 2
    return report[middle_index]


puzzle = read_input_file(Path(__file__).parents[1] / "input.txt")

rules = puzzle.split("\n\n")[0].split("\n")
reports = puzzle.split("\n\n")[1].split("\n")[:-1]

parsed_rules = parse_rules(rules)

middle_sum = 0

for report in reports:
    parsed_report = parse_report(report)
    relevant_rules = filter_relevant_rules(parsed_report, parsed_rules)
    fixed_report, is_wrong = check_report(parsed_report, relevant_rules)
    # Go through the report until it is correct
    is_not_correct = is_wrong
    while is_not_correct:
        fixed_report, is_not_correct = check_report(fixed_report, relevant_rules)

    if is_wrong:
        middle_sum += retrieve_middle(fixed_report)

print(middle_sum)