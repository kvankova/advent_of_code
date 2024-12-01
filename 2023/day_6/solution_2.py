import re

hold_time_unit = 1
speed_increase_unit = 1
default_speed = 0
default_hold = 0

number_better_records = []
with open('puzzle.txt') as f:
    times = f.readline().split(':')[1].replace(' ', '').replace('\n', '')
    times = [int(times)]

    records = f.readline().split(':')[1].replace(' ', '').replace('\n', '')
    records = [int(records)]

    for time, record in zip(times, records):
        candidate_records = []
        for i in range(time):
            hold_time = default_hold + hold_time_unit*i
            remain_time = time - hold_time
            speed = default_speed + speed_increase_unit*i*remain_time
            distance = speed
            candidate_records.append(distance)
        
        better_records = [candidate_record if candidate_record > record else None for candidate_record in candidate_records]
        better_records = [better_record for better_record in better_records if better_record is not None]
        number_better_records.append(len(better_records))

# multiply all number_better_records
result = 1
for number_better_record in number_better_records:
    result *= number_better_record
print(result)
