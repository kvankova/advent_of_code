puzzle_sum = 0
with open('puzzle.txt') as f:
    for line in f.readlines():
        print(line)
        found_digits = []
        for x in line:
            if x.isdigit():
                found_digits.append(int(x))
        print(found_digits)
        if len(found_digits) > 0:
            two_digit_number = 10*found_digits[0] + found_digits[-1]
            print(two_digit_number)
            puzzle_sum += two_digit_number
        