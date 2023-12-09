import re

with open('small_example_2.txt') as puzzle:
    lines = puzzle.readlines()

gear_ratios = 0

for line in range(len(lines)-2):
    top_line = lines[line]
    middle_line =  lines[line+1]
    bottom_line = lines[line+2]

    top_numbers = re.findall(r'\d+', top_line)
    top_numbers_start_position = [(m.start(0), m.end(0)) for m in re.finditer(r'\d+', top_line)]
    
    top_line_numbers_positions = dict(zip(top_numbers, top_numbers_start_position))
    
    middle_numbers  = re.findall(r'\d+', middle_line)
    middle_numbers_start_position = [(m.start(0), m.end(0)) for m in re.finditer(r'\d+', middle_line)]

    middle_line_numbers_positions = dict(zip(middle_numbers, middle_numbers_start_position))

    bottom_numbers = re.findall(r'\d+', bottom_line)
    bottom_numbers_start_position = [(m.start(0), m.end(0)) for m in re.finditer(r'\d+', bottom_line)]
    
    bottom_line_numbers_positions = dict(zip(bottom_numbers, bottom_numbers_start_position))

    middle_asterisks_positions = [m.start(0) for m in re.finditer(r'\*', middle_line)]


    asterisk_numbers = {position:[] for position in middle_asterisks_positions}
    for number in top_line_numbers_positions:
        number_included = False
        for position in range(top_line_numbers_positions[number][0], top_line_numbers_positions[number][1]):
            if (position in middle_asterisks_positions) and (not number_included):
                asterisk_numbers[position].append(number)
                number_included = True
            elif (position-1 in middle_asterisks_positions) and (not number_included):
                asterisk_numbers[position-1].append(number)
                number_included = True
            elif (position+1 in middle_asterisks_positions) and (not number_included):
                asterisk_numbers[position+1].append(number)
                number_included = True

    for number in bottom_line_numbers_positions:
        number_included = False
        for position in range(bottom_line_numbers_positions[number][0], bottom_line_numbers_positions[number][1]):
            if (position in middle_asterisks_positions) and (not number_included):
                asterisk_numbers[position].append(number)
                number_included = True
            elif (position-1 in middle_asterisks_positions) and (not number_included):
                asterisk_numbers[position-1].append(number)
                number_included = True
            elif (position+1 in middle_asterisks_positions) and (not number_included):
                asterisk_numbers[position+1].append(number)
                number_included = True
        
    for number in middle_line_numbers_positions:
        number_included = False
        for position in range(middle_line_numbers_positions[number][0], middle_line_numbers_positions[number][1]):
            if (position-1 in middle_asterisks_positions) and (not number_included):
                asterisk_numbers[position-1].append(number)
                number_included = True
            elif (position+1 in middle_asterisks_positions) and (not number_included):
                asterisk_numbers[position+1].append(number)
                number_included = True

    # if list's length is 2 then multiply numbers 
    for asterisk in asterisk_numbers:
        if len(asterisk_numbers[asterisk]) == 2:
            print(asterisk_numbers[asterisk])
            gear_ratios+= (int(asterisk_numbers[asterisk][0])*int(asterisk_numbers[asterisk][1]))
    print(gear_ratios)


    