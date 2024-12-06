from pathlib import Path

def read_input_file(filename):
    with open(filename, "r") as file:
        return file.read()

def parse_report(report: str) -> dict:
    report = report.split(",")
    return {int(j): i for i, j in enumerate(report)}

def parse_rules(rules: list[str]) -> list[tuple[int, int]]:
    parsed_rules = []
    for rule in rules:
        parsed_rules.append((int(rule.split('|')[0]), int(rule.split('|')[1])))
    return parsed_rules

def filter_relevant_rules(report: dict, rules: list[tuple[int, int]]) -> list[tuple[int, int]]:
    return [rule for rule in rules if rule[0] in report and rule[1] in report]

def check_report(report: dict, rules: list[tuple[int, int]]) -> bool:
    rules_satisfied = 0
    for rule in rules:
        if report[rule[0]] < report[rule[1]]:
            rules_satisfied += 1
    return rules_satisfied == len(rules)

def retrieve_middle(report: dict) -> int:
    middle_index = len(report) // 2

    for key, value in report.items():
        if value == middle_index:
            return key


puzzle = read_input_file(Path(__file__).parents[1] / "input.txt")

rules = puzzle.split("\n\n")[0].split("\n")
reports = puzzle.split("\n\n")[1].split("\n")[:-1]

parsed_rules = parse_rules(rules)

correct_reports = 0

for report in reports:
    parsed_report = parse_report(report)
    relevant_rules = filter_relevant_rules(parsed_report, parsed_rules)
    if check_report(parsed_report, relevant_rules):
        correct_reports += retrieve_middle(parsed_report)
print(correct_reports)