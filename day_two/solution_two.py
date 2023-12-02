import re
result = 0

def process_game(game):
    game_info = {}
    game_list = game.replace(' ', '').replace('\n', '').split(',')
    
    for reveal in game_list:
        amount = re.findall(r'\d+', reveal)
        color = re.findall(r'\D+', reveal)
        game_info[color[0]] = int(amount[0])

    return game_info


with open('puzzle.txt') as puzzle:
    for line in puzzle.readlines():
        possible_stock = {"red": 0, "green": 0, "blue": 0}
        game_name = line.split(':')[0]
        game_id = int(game_name.replace('Game ', ''))
        games = line.split(':')[1]
        games_list = games.split(';')
        
        for game in games_list:
            game_dict = process_game(game)
            for key, value in game_dict.items():
                if value > possible_stock[key]:
                    possible_stock[key] = value

        result += possible_stock['red'] * possible_stock['green'] * possible_stock['blue']
        
 