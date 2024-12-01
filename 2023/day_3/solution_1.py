import re
part_numbers = []
symbol_positions = {}
digit_positions = {}

def process_line(line):
    digit_positions = []
    symbol_positions = []

    for position, line_item in enumerate(line):
        if line_item == '.':
            continue
        elif line_item.isdigit():
            digit_positions.append(position)
        elif line_item.isspace() == False:
            symbol_positions.append(position)
    return digit_positions, symbol_positions

def check_symbol_nearby(digit_position, symbol_positions, line):
    number_positions = []
    # symbol before digit
    if digit_position-1 in symbol_positions[line+1]:
        number_positions.append(digit_position)
    # symbol after digit
    if digit_position+1 in symbol_positions[line+1]:
        number_positions.append(digit_position)
    # symbol above digit
    if digit_position in symbol_positions[line]:
        number_positions.append(digit_position)
    # symbol below digit
    if digit_position in symbol_positions[line+2]:
        number_positions.append(digit_position)
    # symbol at top left of digit
    if digit_position-1 in symbol_positions[line]:
        number_positions.append(digit_position)
    # symbol at top right of digit
    if digit_position+1 in symbol_positions[line]:
        number_positions.append(digit_position)
    # symbol at bottom left of digit
    if digit_position-1 in symbol_positions[line+2]:
        number_positions.append(digit_position)
    # symbol at bottom right of digit
    if digit_position+1 in symbol_positions[line+2]:
        number_positions.append(digit_position)
    return number_positions

with open('puzzle.txt') as puzzle:
    lines = puzzle.readlines()

    for line in range(len(lines)-2):
        
        top_line = lines[line]
        middle_line = lines[line+1]
        bottom_line = lines[line+2]
        print(top_line, middle_line, bottom_line)

        part_numbers_positions = []

        digit_positions[line], symbol_positions[line] = process_line(top_line)
        digit_positions[line+1], symbol_positions[line+1] = process_line(middle_line)
        digit_positions[line+2], symbol_positions[line+2] = process_line(bottom_line)


        for digit_position in digit_positions[line+1]:
            part_numbers_positions+=check_symbol_nearby(digit_position, symbol_positions, line)

        # keep digit start index only
        part_numbers_starts = []
        for position in part_numbers_positions:
            if position-1 not in part_numbers_positions:
                part_numbers_starts.append(position)
        

        # find all numbers and their starting position in string middle_line
        all_numbers = re.findall(r'\d+', middle_line)
        numbers_start_position = [(m.start(0), m.end(0)) for m in re.finditer(r'\d+', middle_line)]

        for number, position_tuple in zip(all_numbers, numbers_start_position):
            for position in range(position_tuple[0], position_tuple[1]):
                if position in part_numbers_starts:
                    part_numbers.append(number)
            print(part_numbers)
    
    print(sum([int(number) for number in part_numbers]))