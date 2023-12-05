import re
part_numbers = []
asterisk_positions = {}
digit_positions = {}

def process_line(line):
    digit_positions = []
    asterisk_positions = []

    for position, line_item in enumerate(line):
        if line_item == '.':
            continue
        elif line_item.isdigit():
            digit_positions.append(position)
        elif line_item=="*":
            asterisk_positions.append(position)
    return digit_positions, asterisk_positions


with open('puzzle.txt') as puzzle:
    lines = puzzle.readlines()

    for line in range(len(lines)-2):
        
        top_line = lines[line]
        middle_line = lines[line+1]
        bottom_line = lines[line+2]
        print(top_line, middle_line, bottom_line)

        part_numbers_positions = []

        digit_positions[line], asterisk_positions[line] = process_line(top_line)
        digit_positions[line+1], asterisk_positions[line+1] = process_line(middle_line)
        digit_positions[line+2], asterisk_positions[line+2] = process_line(bottom_line)

        