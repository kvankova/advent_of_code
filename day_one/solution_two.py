import re

puzzle_sum = 0
lookup_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
with open('puzzle.txt') as f:
    for line in f.readlines():
        print(line)
        found_digits = ''
        parts = re.findall(r'\D+|\d+', line)
        for x in parts:
            if x.isdigit():
                found_digits += x
            else:
                found_matches = re.findall(r"(?=("+'|'.join(lookup_digits)+r"))", x)
                for match in found_matches:
                    found_digits += str(lookup_digits.index(match)+1)

        if len(found_digits) > 0:
            puzzle_sum += 10*int(found_digits[0]) + int(found_digits[-1]) 

puzzle_sum