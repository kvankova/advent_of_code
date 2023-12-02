stock = {"red": 12, "green": 13, "blue": 14}
possible_game_ids = []
import re

def game_not_possible(game):
    game_info = {}
    game_list = game.replace(' ', '').replace('\n', '').split(',')
    for reveal in game_list:
        amount = re.findall(r'\d+', reveal)
        color = re.findall(r'\D+', reveal)
        game_info[color[0]] = int(amount[0])
    
    for key, value in game_info.items():
        if value > stock[key]:
            return True
    
    return False

with open('puzzle.txt') as puzzle:
    for line in puzzle.readlines():
        print(line)
        game_name = line.split(':')[0]
        game_id = int(game_name.replace('Game ', ''))
        games = line.split(':')[1]
        games_list = games.split(';')
        possible = True
        
        for game in games_list:
            if game_not_possible(game):
                possible=False
        print(possible)
        if possible:
            possible_game_ids.append(game_id)

sum(possible_game_ids)