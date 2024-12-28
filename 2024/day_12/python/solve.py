from pathlib import Path
import numpy as np
import copy 

def read_input_file(filename):
    with open(filename, "r") as file:
        return file.read()

puzzle = np.array(read_input_file(Path(__file__).parents[1] / "input.txt").split("\n")[:-1])

letter_locations = {}
for row_index, row in enumerate(puzzle):
    for letter_index, letter in enumerate(row):
        if letter not in letter_locations:
            letter_locations[letter] = []
        letter_locations[letter].append((row_index, letter_index))


def is_adjacent(location1, locations):
    for location2 in locations:
        if abs(location1[0] - location2[0]) + abs(location1[1] - location2[1]) == 1:
            return True
    return False

regions = {}
for letter, locations in letter_locations.items():
    for location in locations:
        applicable_regions = [region for region in regions if region.startswith(letter)]
        for region in applicable_regions:
            if is_adjacent(location, regions[region]):
                regions[region].append(location)
                break
        else:
            new_region_name = letter + str(location[0]) + str(location[1])
            regions[new_region_name] = [location]

def get_adjacent_locations(location):
    adjacent_locations = []
    for row_index, col_index in [(location[0] - 1, location[1]), (location[0] + 1, location[1]), (location[0], location[1] - 1), (location[0], location[1] + 1)]:
        adjacent_locations.append((row_index, col_index))
    return adjacent_locations

# merge regions if they are adjacent
def merge_adjacent_regions(regions):
    merged = copy.deepcopy(regions)
    
    def merge_single_region(target_region):
        merged_with = []
        target_locations = merged[target_region]
        
        for loc in target_locations:
            for adj_loc in get_adjacent_locations(loc):
                for other_region, other_locs in merged.items():
                    if (other_region != target_region and 
                        other_region not in merged_with and
                        other_region[0] == target_region[0] and
                        adj_loc in other_locs):
                            merged[target_region].extend(other_locs)
                            merged_with.append(other_region)
        
        return {r: locs for r, locs in merged.items() 
               if r not in merged_with}

    for region in merged:
        if region in merged:
            merged = merge_single_region(region)
            
    return merged

merged_regions = merge_adjacent_regions(regions)

def calculate_region_area(region, regions):
    return len(regions[region])


def calculate_region_boundary_length(region, regions):
    boundary_length = 0
    for location in regions[region]:
        for adjacent_location in get_adjacent_locations(location):
            if adjacent_location not in regions[region]:
                boundary_length += 1
    
    return boundary_length

def calculate_cost(region, regions):
    return (
        calculate_region_area(region, regions) * calculate_region_boundary_length(region, regions)
        )

total_cost = 0
for region in merged_regions:
    total_cost += calculate_cost(region, merged_regions)
print(total_cost)